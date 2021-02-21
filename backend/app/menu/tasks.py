# import datetime
import os
from datetime import datetime, timezone, timedelta

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Q
from celery import shared_task

from menu.models import Dish


class MenuTask:

    @staticmethod
    @shared_task
    def send_notification_with_updated_data():
        from_datetime = datetime.now(timezone.utc) - timedelta(days=1)

        all_users_emails = User.objects.all().values_list('email', flat=True)
        updated_or_added_dish = Dish.objects.filter(
            Q(create_date__gt=from_datetime) | Q(last_update_date__gt=from_datetime)).values('uuid', 'name', 'create_date')

        if updated_or_added_dish and all_users_emails:
            send_mail(
                'Updated Menus',
                'Dishes was updated or created: \n' + \
                '\n'.join(
                    [f"Dish {dish['name']} ({dish['uuid']}) was updated or created" for dish in updated_or_added_dish]),
                os.environ.get('EMAIL_ADDRESS', 'your_favorite_restaurant@example.com'),
                all_users_emails,
                fail_silently=False,
            )

            return f'E-mail was send to {all_users_emails} \n updated dishes:' \
                   f'{[dish["uuid"] for dish in updated_or_added_dish]}'
        return 'Nothing has been changed'
