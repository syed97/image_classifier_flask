# script to run docker containers
echo killing old docker processes
docker-compose rm -fs

echo building docker containers
docker-compose up --build -d
