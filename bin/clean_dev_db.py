#!python
from django.contrib.sites.models import Site


def swap_site():
    site = Site.objects.get(pk=1)
    site.domain = '127.0.0.1:8000'
    if not site.name.endswith(' dev'):
        site.name += ' dev'
    site.save()


def main():
    swap_site()

if __name__ == '__main__':
    main()
