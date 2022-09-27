cd ./back
docker-compose up -d

cd ..
docker exec -i test_gz_back python manage.py migrate
docker exec -i test_gz_back python manage.py initadmin
docker exec -i test_gz_back python manage.py loaddata db.json
