{
    "name": "SH Hello World",
    "summary": "Módulo de prueba",
    "version": "19.0.1.0.0",
    "author": "Salas",
    "website": "https://salas.plus",
    "category": "Salas",
    "depends": ["base", "web"],
    "data": [
        "security/security_data.xml",
        "security/ir.model.access.csv",
        "views/hello_world_views.xml",
        "views/res_users.xml",
        'data/sh_hello_world_data.xml',
        'data/sh.hello.world.tag.csv',
        'reports/hello_world_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'HelloWorld/static/src/components/todo_item/todo_item.xml',
            'HelloWorld/static/src/components/todo_item/todo_item.js',
        ],
    },
    "application": True,
}