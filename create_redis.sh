docker run \
  -p 6379:6379 \
  --name db_redis \
  -v /data/redis_data:/data \
  --restart=always \
  -d redis:4.0.14-alpine \
  --requirepass "<password>"
