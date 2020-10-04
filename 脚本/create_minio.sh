docker run \
  --name minio \
   -v /data/minio_data:/data \
   -p 9000:9000 \
   -e MINIO_ACCESS_KEY=<user_name> \
   -e MINIO_SECRET_KEY=<password> \
   --privileged=true \
   -d minio/minio server /data
