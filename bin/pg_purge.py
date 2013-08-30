#!python
import os
import glob
import datetime

from django.conf import settings


class Backup(object):
    def __init__(self, filename):
        self.filename = filename

    def datetime_str(self):
        return self.filename.split('.')[1]

    def datetime(self):
        return datetime.datetime.strptime(self.datetime_str(),
                                          "%Y%m%d-%H%M%S")

    def date(self):
        return self.datetime().date()

    def __lt__(self, other):
        return self.datetime() < other.datetime()

    def delete(self):
        os.unlink(self.filename)


if __name__ == '__main__':
    pgdump_dir = os.path.join(settings.PROJECT_ROOT_DIR, 'var', 'pgdump')
    os.chdir(pgdump_dir)

    backup_prefix = settings.DATABASES['default']['NAME']

    backups = []
    for filename in glob.glob('%s.*' % backup_prefix):
        backups.append(Backup(filename=filename))

    backups.sort()

    # this is a real mess.
    last_backup = None
    last_kept_backup = None
    # need backups to be around once every...
    max_backup_diff = datetime.timedelta(days=7)

    # need to keep at least one backup each day up after this time:
    keep_every_since = datetime.datetime.now() - datetime.timedelta(days=7)
    for backup in backups:
        if last_backup is None:
            pass
        elif last_backup.date() == backup.date():
            # two backups on one day:
            last_backup.delete()
        elif last_backup.datetime() < keep_every_since:
            if last_backup.datetime() > (backup.datetime() - max_backup_diff):
                backup.delete()
                backup = last_backup
        last_backup = backup
