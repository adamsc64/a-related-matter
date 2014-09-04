# All My Relations: Optimizing your webapp by using django-debug-toolbar, select_related(), and prefetch_related()

## Christopher Adams
## DjangoCon 2014

# Steps:
1. Create virtualenv
2. Install dependencies
  $ pip install -r requirements.txt
3. Write local_settings.py and assign DATABASES to use database of your choice
4. Run syncdb
  $ python manage.py syncdb
5. Load fixture.json
  $ python manage.py loaddata fixture.json
6. Run the development server
  $ python manage.py runserver
7. Request the URL /blog
8. Notice the SQL queries using django-debug-toolbar
9. To view with optimizations, use GET param: `?optimized=true`
