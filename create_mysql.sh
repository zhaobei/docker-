docker run \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=rdKUdffDDy \
  -p 3306:3306 \
  --restart=always \
  -v /data/mysql_db:/var/lib/mysql \
  -d  mysql:5.7 \
  --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
