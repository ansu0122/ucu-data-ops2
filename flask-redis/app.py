from flask import Flask
from redis import Redis
import os

app = Flask(__name__)
with open('/run/secrets/redis-password', 'r') as file:
    redis_password = file.read().strip()

redis = Redis(host='redis', port=int(os.environ.get(
    'REDIS_PORT', 6379)), password=redis_password)


@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'), 'utf-8')
    return "This webpage has been viewed "+counter+" time(s)"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get(
        'FLASK_PORT', 8050)), debug=True)
