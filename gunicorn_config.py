bind = "0.0.0.0:8006"
module = "config.wsgi:application"

workers = 1
worker_connections = 1000
threads = 4
