import os
bind = '0.0.0.0:' + environ.get('PORT', '8080')
# workers = cpu_count()

# Add the --reload option
reload = True

# Specify the default application
default_proc_name = 'news.wsgi:application'

# Add the Gevent worker class
worker_class = 'gevent'
