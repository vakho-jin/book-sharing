from django.core.management.base import BaseCommand
from apps.books.models import Genre, BookCondition
from apps.authors.models import Author

class Command(BaseCommand):
    help = 'საწყისი მონაცემების ჩატვირთვა'

    def handle(self, *args, **options):
        # ჟანრები
        genres = [
            'მხატვრული ლიტერატურა',
            'დეტექტივი',
            'თრილერი',
            'ფანტასტიკა',
            'ფენტეზი',
            'რომანი',
            'კლასიკური ლიტერატურა',
            'თანამედროვე პროზა',
            'პოეზია',
            'დრამატურგია',
            'ბიოგრაფია და მემუარები',
            'ისტორია',
            'ფილოსოფია',
            'ფსიქოლოგია',
            'ტექნოლოგია',
            'კომპიუტერი და ინტერნეტი',
            'ბიზნესი და ეკონომიკა',
            'თვითგანვითარება',
            'კულინარია',
            'მედიცინა და ჯანმრთელობა',
            'მოგზაურობა',
        ]

        for genre_name in genres:
            genre, created = Genre.objects.get_or_create(name=genre_name)
            if created:
                self.stdout.write(f'შეიქმნა ჟანრი: {genre_name}')

        # წიგნის მდგომარეობა
        conditions = [
            ('excellent', 'საუკეთსო'),
            ('good', 'კარგი'),
            ('fair', 'დამაკმაყოფილებელი'),
            ('poor', 'დაზიანებული'),
        ]

        for condition_code, condition_name in conditions:
            condition, created = BookCondition.objects.get_or_create(
                name=condition_code,
                defaults={'description': f'წიგნის მდგომარეობა არის {condition_name.lower()}'}
            )
            if created:
                self.stdout.write(f'შეიქმნა მდგომარეობა: {condition_name}')

        # ავტორები
        authors = [
    {'name': 'ვაჟა-ფშაველა', 'biography': 'ქართველი პოეტი და მწერალი, ქართული ლიტერატურის კლასიკოსი'},
    {'name': 'ილია ჭავჭავაძე', 'biography': 'ქართველი მწერალი, პუბლიცისტი და საზოგადო მოღვაწე, ქართული ნაციონალური მოძრაობის ლიდერი'},
    {'name': 'ალექსანდრე ყაზბეგი', 'biography': 'ქართველი მწერალი და პოეტი, ქართული რომანტიზმის წარმომადგენელი'},
    {'name': 'გალაკტიონ ტაბიძე', 'biography': 'ქართველი პოეტი, XX საუკუნის ქართული ლიტერატურის ერთ-ერთი უდიდესი წარმომადგენელი'},
    {'name': 'ნიკოლოზ ბარათაშვილი', 'biography': 'ქართველი რომანტიკოსი პოეტი, ქართული რომანტიზმის ფუძემდებელი'},
    {'name': 'შოთა რუსთაველი', 'biography': 'ქართველი პოეტი და სახელმწიფო მოღვაწე, მსოფლიო კლასიკის შედევრის „ვეფხისტყაოსნის“ ავტორი'}
    ]

        for author_data in authors:
            author, created = Author.objects.get_or_create(
                name=author_data['name'],
                defaults={'biography': author_data['biography']}
            )
            if created:
                self.stdout.write(f'შეიქმნა ავტორი: {author_data["name"]}')

        self.stdout.write(self.style.SUCCESS('საწყისი მონაცემები წარმატებით ჩაიტვირთა!'))