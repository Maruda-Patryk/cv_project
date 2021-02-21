#!/bin/sh

case $1 in

"migrate_and_run_backend_develop")
  export DJANGO_SETTINGS_MODULE=cv_project.settings.dev
  python manage.py migrate --noinput
  python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); \\
     User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')"
  python manage.py shell -c "from django.core.management import call_command; from menu.models import MenuCard; \\
    bool(MenuCard.objects.all().count()) or call_command('loaddata', 'fixtures/menu.json')"
  python manage.py runserver 0.0.0.0:8000
  ;;

"run_worker")
  /wait-for.sh django:8000
  celery worker --app=cv_project --pidfile= --loglevel=info
  ;;

"run_scheduler")
  /wait-for.sh django:8000
  celery --app=cv_project beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile= --loglevel=info
  ;;

esac
