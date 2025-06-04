from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [
    dict(
        name='Majo_12_2',
        num_demo_participants=14,
        app_sequence=['clerpay_start', 'Welcome_Majo_12_2', 'Majo_12_2', 'Survey_All', 'Thank_All', 'clerpay_end']
    ),
    dict(
        name='Cons_12_2',
        num_demo_participants=14,
        app_sequence=['clerpay_start', 'Welcome_Cons_12_2', 'Cons_12_2', 'Survey_All', 'Thank_All', 'clerpay_end']
    ),
    dict(
        name='Majo_12_3',
        num_demo_participants=15,
        app_sequence=['clerpay_start', 'Welcome_Majo_12_3', 'Majo_12_3', 'Survey_All', 'Thank_All', 'clerpay_end']
    ),
    dict(
        name='Cons_12_3',
        num_demo_participants=15,
        app_sequence=['clerpay_start', 'Welcome_Cons_12_3', 'Cons_12_3', 'Survey_All', 'Thank_All', 'clerpay_end']
    ),
    dict(
        name='Majo_O_12_2',
        num_demo_participants=14,
        app_sequence=['clerpay_start', 'Welcome_Majo_12_2', 'Majo_O_12_2', 'Survey_All', 'Thank_All', 'clerpay_end']
    ),   
    dict(
        name='Cons_O_12_2',
        num_demo_participants=14,
        app_sequence=['clerpay_start', 'Welcome_Cons_12_2', 'Cons_O_12_2', 'Survey_All', 'Thank_All', 'clerpay_end']
    ),  
    dict(
        name='Majo_O_12_3',
        num_demo_participants=15,
        app_sequence=['clerpay_start', 'Welcome_Majo_12_3', 'Majo_O_12_3', 'Survey_All', 'Thank_All', 'clerpay_end']
    ),   
    dict(
        name='Cons_O_12_3',
        num_demo_participants=15,
        app_sequence=['clerpay_start', 'Welcome_Cons_12_3', 'Cons_O_12_3', 'Survey_All', 'Thank_All', 'clerpay_end']
    )       
]

LANGUAGE_CODE = 'de'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
#ROOMS = [dict(name='CLER', display_name='CLER', participant_label_file='_rooms/CLER.txt')]
ROOMS = [dict(name='CLER', display_name='CLER', participant_label_file='_rooms/CLER.txt'), dict(name='CLER_ZOOM', display_name='CLER_ZOOM', participant_label_file='_rooms/CLER_ZOOM.txt')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


