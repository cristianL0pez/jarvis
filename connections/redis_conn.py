import redis
redis_client = redis.Redis(host='redis', port=6379, db=0, username='admin', password='1234')