Swagger: http://localhost:8001/docs#/

Зайти в контейнер БД social_media

docker exec -it soa-postgresql psql -U postgres social_media

Зайти в контейнер БД post_service 

docker exec -it soa-postgresql psql -U postgres post_service

Запуск 

docker-compose -f tools/database-dev/docker-compose.yml build docker-compose -f



tony:   ab13c80d-d2e8-44f5-8e29-8a9866cefd23 
h: cf06bb24-64df-4cef-8b59-427d30d99633