bind = '0.0.0.0:8000'
reload = True
daemon = False
debug = True
# accesslog = '/var/www/html/myapplication/gunicorn_access.log'
access_log_format = '"%({X-Real-IP}i)s" "%({X-Forwarded-For}i)s" %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" '
accesslog = '-'
# accesslog = path.join(getenv('FLASK_WEB_MONITORING_CWD'), 'gunicorn_access.log')
# errorlog = 'gunicorn_error.log'
errorlog = '-'
sendfile = None
loglevel = 'info'
workers = 1
