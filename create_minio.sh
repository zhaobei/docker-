docker run \
  --name minio \
   -v /data/minio_data:/data \
   -p 9000:9000 \
   -e MINIO_ACCESS_KEY=admin \
   -e MINIO_SECRET_KEY=aA8RuVN0P5 \
   --privileged=true \
   -d minio/minio server /data
