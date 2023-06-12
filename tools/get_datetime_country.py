import pytz
from datetime import datetime


def get_datetime_country_(country):
    try:
        tz_by_country = pytz.country_timezones[country]

        tz_country = pytz.timezone(tz_by_country[0])

        current_datetime = datetime.now(tz_country)
        return current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    except KeyError:
        return "País no válido o no se encontró información sobre la zona horaria."
