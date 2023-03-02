
#!/bin/bash

# マイグレーションを実行
docker compose -f docker-compose.prod.yml exec app python manage.py makemigrations --noinput
docker compose -f docker-compose.prod.yml exec app python manage.py migrate --noinput
docker compose -f docker-compose.prod.yml exec app python manage.py makemigrations pairleary_app --noinput
docker compose -f docker-compose.prod.yml exec app python manage.py migrate pairleary_app --noinput
# スーパーユーザー作成
# docker compose -f docker-compose.yml exec app python manage.py createsuperuser
