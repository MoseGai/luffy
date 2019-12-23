# import redis
#
# r=redis.Redis(host='127.0.0.1',port=6379)

import redis
pool = redis.ConnectionPool(host='127.0.0.1',port=6379)
r = redis.Redis(connection_pool=pool)


# 二、采用连接池操作redis（支持并发）
pool = redis.ConnectionPool(db=12, max_connections=100)
rp = redis.Redis(connection_pool=pool)
rp.set('name', 'dahou')
print(rp.get('name'))


