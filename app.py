from flask import Flask
import threading
import multiprocessing
import os
from prometheus_client import start_http_server, Gauge

app = Flask(__name__)

# metrics
cpu_load_metric = Gauge('app_cpu_load', 'App CPU Load')
health_metric = Gauge('app_health_status', 'App Health')

health_metric.set(1)

load_started = False
# load generator
def cpu_stress():
    while True:
        pass

def start_load():
    global load_started

    if not load_started:
        load_started = True
        processes = []

        # use all CPU cores
        for _ in range(os.cpu_count()):
            p = multiprocessing.Process(target=cpu_stress)
            p.start()
            processes.append(p)

        cpu_load_metric.set(1)



@app.route('/')
def home():
    return "App running"

@app.route('/load')
def load():
    start_load()
    return "Load started"

if __name__ == '__main__':
    start_http_server(8000)   
    app.run(host='0.0.0.0', port=5000)
