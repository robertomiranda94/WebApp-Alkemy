from django.conf import settings
from django_jinja.builtins import DEFAULT_EXTENSIONS

# Agrega la extensión de Jinja para archivos HTML
DEFAULT_EXTENSIONS.append('jinja2.ext.html')

# Configura el directorio de templates
TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'APP_DIRS': True,
        'DIRS': [str(settings.TEMPLATES_DIR)],
        'OPTIONS': {
            'extensions': DEFAULT_EXTENSIONS,
        },
    },
]