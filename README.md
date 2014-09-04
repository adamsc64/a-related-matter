# All My Relations: Optimizing your webapp by using django-debug-toolbar, select_related(), and prefetch_related()

## Christopher Adams
## DjangoCon 2014

# Steps:
1. Create virtualenv
2. Install dependencies
  $ pip install -r requirements.txt
3. Create database
4. Run syncdb
5. Load fixture.json
6. Request the URL /blog
7. Notice the SQL queries using django-debug-toolbar
8. To view with optimizations, use GET param: `?optimized=true`
