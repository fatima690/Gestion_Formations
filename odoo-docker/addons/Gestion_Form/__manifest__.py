{
    "name": "Gestion des Formations",
    "version": "1.0",
    "summary": "Module de gestion des formations académiques",
    "category": "Training",
    "author": "EMSI",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "data/partner_category.xml",
        "views/formation_views.xml",
        "views/session_views.xml",
        "views/inscription_views.xml",
        "views/participant_views.xml",
        "views/reporting_views.xml",
    ],
    "demo": [
        "data/demo.xml",
    ],
    "installable": True,
    "application": True,
}