Проект по курсу СОА

Климчук Антонина Игоревна, БПМИ2110

Выбранная система: Социальная сеть

Для запуска сервиса из корня репозитория:
docker-compose -f tools/database-dev/docker-compose.yml up

В папке social-media/migrations находятся миграции в базу данных, в src лежат Dockerfile для запуска сервиса и
сам код сервиса в main.py

В папке tools/database-dev лежит docker-compose.yml для запуска сервиса, создания базы данных и накатки миграций