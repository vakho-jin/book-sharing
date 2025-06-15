from django.core.management.base import BaseCommand
from apps.books.models import BookCondition

class Command(BaseCommand):
    help = 'წიგნების საწყისი მდგომარეობის შექმნა'

    def handle(self, *args, **options):
        conditions = [
            ('excellent', 'საუკეთესო'),
            ('good', 'კარგი'),
            ('fair', 'დამაკმაყოფილებელი'),
            ('poor', 'დაზიანებული'),
        ]

        for condition_code, condition_display in conditions:
            condition, created = BookCondition.objects.get_or_create(
                name=condition_code,
                defaults={'description': f'წიგნის მდგომარეობაა {condition_display.lower()}'}
            )
            if created:
                self.stdout.write(f'შეიქმნა მდგომარეობა: {condition_display}')

        self.stdout.write(self.style.SUCCESS('წიგნების მდგომარეობები წარმატებით შეიქმნა'))