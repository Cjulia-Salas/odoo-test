{
    "name": "SH Hello World",
    "summary": "Módulo de prueba",
    "version": "19.0.1.0.0",
    "author": "Salas",
    "website": "https://salas.plus",
    "category": "Salas",
    "depends": ["base", "web"],
    "data": [
        "security/ir.model.access.csv",
        'reports/hello_world_report.xml',
        "views/hello_world_views.xml",
        "views/res_users.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'HelloWorld/static/src/components/todo_item/todo_item.xml',
            'HelloWorld/static/src/components/todo_item/todo_item.js',
        ],
    },
    "application": True,
}