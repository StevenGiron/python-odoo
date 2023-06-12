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
        "views/candadites_votes.views.xml",
    ],
    'qweb': [
        "views/voting_website_form.xml",
    ],
    'js': [
        'static/src/js/voting/voting_script.js',
    ],

    "assets": {
        "web.assets_backend": [

        ],
        'web.assets_frontend': [
            "static/src/js/voting/voting_script.js"
        ],
    },
    "application": True,
    "installable": True,
}