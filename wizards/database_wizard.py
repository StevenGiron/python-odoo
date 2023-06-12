from odoo import models, fields, api
import csv
import psycopg2

class ImportWizard(models.TransientModel):
    _name = 'import.wizard'

    data_file = fields.Binary(string='Archivo')
    model_id = fields.Many2one('ir.model', string='Modelo')

    def import_data(self):
        # se obtiene el contenido del archivo
        file_content = self.data_file.decode('base64')

        # leer el archivo CSV
        csv_data = csv.reader(file_content.splitlines(), delimiter=',')

        # se obtiene el nombre del modelo seleccionado
        model_name = self.model_id.model

        # Se establece la conexión a la base de datos de Odoo
        conn = self._cr.connection

        # se itera sobre las filas del archivo CSV y se hacen los inserts en la base de datos
        with conn.cursor() as cursor:
            for row in csv_data:
                # Obtener los campos a insertar del modelo seleccionado
                model = self.env[model_name]
                fields = model.fields_get()

                # se crea la lista de campos y valores para el insert
                insert_fields = []
                insert_values = []
                for field_name, field in fields.items():
                    if field_name in row:
                        insert_fields.append(field_name)
                        insert_values.append(row[field_name])

                # se construye la consulta SQL de insert
                query = f"INSERT INTO {model._table} ({', '.join(insert_fields)}) VALUES ({', '.join(['%s'] * len(insert_values))})"

                # Ejecutar la consulta SQL de insert
                cursor.execute(query, tuple(insert_values))

        # Commit para guardar los cambios en la base de datos
        conn.commit()

        # Cerrar la conexión a la base de datos
        conn.close()

        self.env.cr.execute(query)

        return {'type': 'ir.actions.act_window_close'}