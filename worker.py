import redis
import time

r = redis.Redis(host="redis", port=6379)

while True:
    task = r.blpop("doc_queue")
    print("Processing document...")
    time.sleep(3)
