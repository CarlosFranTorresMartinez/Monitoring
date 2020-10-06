from flask import Response, Flask, request
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time

app = Flask(__name__)
set

_INF = float("inf")

graphs = {}
graphs['c'] = Counter('python_request_operations_total',
                      'The total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds',
                        'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, _INF))

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')


@app.route("/")
def hello():
    start = time.time()
    graphs['c'].inc()

    time.sleep(0.600)
    end = time.time()
    graphs['h'].observe(end - start)
    return "Hello World!"


@app.route("/metrics")
def requests_count():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)
