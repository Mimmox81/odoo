{
    'name': 'IMAR Modern Theme',
    'version': '18.0.1.0.0',
    'category': 'Themes/Backend',
    'summary': 'Modern theme inspired by IMAR Training LMS',
    'description': '''
        Tema moderno per Odoo ispirato al design di IMAR Training.
        - Sidebar moderna
        - Card con ombre morbide
        - Colori IMAR (rosso/indigo)
        - Stile pulito e professionale
    ''',
    'author': 'IMAR Srl',
    'website': 'https://imarsrl.com',
    'license': 'LGPL-3',
    'depends': ['web', 'hr_recruitment'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'imar_theme/static/src/scss/variables.scss',
            'imar_theme/static/src/scss/layout.scss',
            'imar_theme/static/src/scss/kanban.scss',
            'imar_theme/static/src/scss/forms.scss',
            'imar_theme/static/src/scss/recruitment.scss',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
