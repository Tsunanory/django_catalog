from django.core.mail import send_mail
from django.core.management import BaseCommand
from config.settings import DEFAULT_FROM_EMAIL


class Command(BaseCommand):
    def handle(self, *args, **options):
        send_mail(
            subject="Восстановление пароля",
            message=f"Ваш пароль от сайта Shop изменен:\n"
                    f"Email:"
                    f"Пароль:",
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=['ivan.sklyaruk47@bk.ru']
        )
        print('mail sent')