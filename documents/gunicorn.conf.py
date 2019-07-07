bind = "unix:/tmp/titov.sock"
workers = 2
logfile = "/var/log/titov/gunicorn.log"
loglevel = "info"
proc_name = "titov"
pidfile = "/var/run/titov/gunicorn.pid"
pythonpath = "/home/nt/titov/"
