import os, multiprocessing
bind = '0.0.0.0:' + os.environ.get('PORT', '8080')

workers = multiprocessing.cpu_count()

print('Using Default Conf')

# Add the --reload option
reload = True
# Specify the default application
default_proc_name = 'news.wsgi:application'

# Add the Gevent worker class
worker_class = 'gevent'
