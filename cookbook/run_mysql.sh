docker run -d \
  -e MYSQL_ROOT_PASSWORD=ethosian \
  -e MYSQL_DATABASE=ethosian \
  -e MYSQL_USER=ethosian \
  -e MYSQL_PASSWORD=ethosian \
  -p 3306:3306 \
  -v mysql_data:/var/lib/mysql \
  -v $(pwd)/cookbook/mysql-init:/docker-entrypoint-initdb.d \
  --name mysql \
  mysql:8.0
