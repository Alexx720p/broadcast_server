import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

# redis_client.hset(f'Client: {self.channel_name}', mapping={
#     'username': user,
#     'connected_at': str(datetime.utcnow())
# })