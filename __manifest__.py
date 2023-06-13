{
    "name": "Universidad UNIACME",
    "summary": "Realice votaciones para la universidad UNIACME",
    "author": "Steven Giron Arcila",
    "depends": [
        "base",
        "base_geolocalize",
        "website",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/campus.views.xml",
        "views/student.views.xml",
        "views/voting_process_views.xml",
        "views/voting_website_form.xml",
        "views/number_votes_views.xml",
        "wizards/database_wizard_view.xml"
    ],
    'qweb': [
        "views/voting_website_form.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "static/src/js/voting_script.js"
        ],
        'web.assets_frontend': [

        ],
    },
    "application": True,
    "installable": True,
}
