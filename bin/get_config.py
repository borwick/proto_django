#!python
import sys

from django.conf import settings


CONFIG_MAP = {
    'db_name': settings.DATABASES['default']['NAME'],
    'db_user': settings.DATABASES['default']['USER'],
    'project_root_dir': settings.PROJECT_ROOT_DIR,
    }

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        print CONFIG_MAP[arg]
