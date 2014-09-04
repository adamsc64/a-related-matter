All My Relations: Optimizing your webapp by using django-debug-toolbar, select_related(), and prefetch_related()

Christopher Adams
DjangoCon 2014

# Steps:
## Create virtualenv
## Install dependencies
  $ pip install -r requirements.txt
## Create database
## Run syncdb
## Load fixture.json
## Request the URL /blog
## Notice the SQL queries using django-debug-toolbar
## To view with optimizations, use GET param: `?optimized=true`
