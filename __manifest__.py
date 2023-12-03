{
    'name': 'vendor',  # The name that will appear in the App list
    'version': '16.0',  # Version
    'application': True,  # This line says the module is an App, and not a module
    'depends': [
            'sale',
            'product',
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/vendor_forecast_view.xml',
        'views/vendor_adjustment_request_views.xml',
        # 'data/mail_template.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
