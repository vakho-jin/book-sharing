# წიგნების გაცემის სერვისის API

RESTful API წიგნების გაცემის სერვისისთვის, სადაც მომხმარებლებს შეეძლებათ უფასოდ გასცენ, ასევე სხვა მომხმარებლებისგან მოითხოვონ სასურველი წიგნები.

## ფუნქციები
- 📚 **წიგნების მართვა**: წიგნების დამატება, რედაქტირება, ნახვა და წაშლა (CRUD)
- 👥 **მომხმარებლების სისტემა**: რეგისტრაცია, ავტორიზაცია, პროფილები
- 🔍 **ძებნა და ფილტრაცია**: ძიება და ფილტრაცია ავტორის, ჟანრის, წლის, მდებარეობის მიხედვით
- 📋 **მოთხოვნების სისტემა**: წიგნების მოთხოვნები და მოთხოვნების მართვა
- ⭐ **რეიტინგის სისტემა**: მომხმარებლების შეფასება წიგნების გაცვლის შემდეგ
- 📱 **API დოკუმენტაცია**: Swagger ინტერფეისი

## გამოყენებული ტექნოლოგიები
- **Backend**: Python 3.11, Django 4.2, Django REST Framework
- **მონაცემთა ბაზა**: SQLite
- **კონტეინერიზაცია**: Docker, Docker Compose
- **დოკუმენტაცია**: Swagger (drf-yasg)
- **ავტორიზაცია**: Token-based authentication

## დაწყება

### მოთხოვნები
- Python 3.11+
- Docker и Docker Compose (სასურველია)

### დაყენება და გაშვება

#### Docker-ის საშუალებით
**რეპოზიტორიის დაკლონვა და ინსტალაცია**
```bash
# რეპოზიტორიის დაკლონვა
git clone https://github.com/vakho-jin/book-sharing.git
# დირექტორიაში შესვლა
cd book-sharing
# ვირტუალური გარემოს შექმნა
python -m venv venv
#ვირტუალური გარემოს აქტივაცია
source venv/bin/activate  # Linux/Mac
# ან
venv\Scripts\activate  # Windows
# დამოკიდებულებების ინსტალაცია
pip install -r requirements.txt
# მონაცემთა ბაზის მიგრაცია
python manage.py makemigrations
python manage.py migrate
# წინასწარი მონაცემების შექმნა
python manage.py create_conditions
python manage.py load_initial_data
# სუპერმომხმარებლის შექმნა
python manage.py createsuperuser
# სერვერის გაშვება
python manage.py runserver
```

## API Endpoints

### ავრტორიაზაცია
 - POST /api/auth/register/ - რეგისტრაცია
 - POST /api/auth/login/ - შესვლა
 - POST /api/auth/logout/ - გამოსვლა
 - GET/PUT /api/auth/profile/ - პროფილის ნახვა/რედაქტირება

### წიგნები
 - GET /api/books/ - ხელმისაწვდომი წიგნების სია
 - POST /api/books/ - ახალი წიგნის დამატება
 - GET /api/books/{id}/ - წიგნის შესახებ
 - PUT /api/books/{id}/ - წიგნის განახლება (მხოლოდ მფლობელისთვის)
 - DELETE /api/books/{id}/ - წიგნის წაშლა (მხოლოდ მფლობელისთვის)
 - GET /api/books/my-books/ - ჩემი წიგნები

### ავტორები და ჟანრები
 - GET /api/authors/ - ავტორების სია
 - POST /api/authors/ - ავტორის დამატება
 - GET /api/books/genres/ - ჟანრების სია
 - GET /api/books/conditions/ - წიგნების მდგომარეობის სია

### წიგნების მოთხოვნები
 - GET /api/requests/ - ჩემი მოთხოვნები
 - POST /api/requests/ - წიგნის მოთხოვნის შექმნა
 - GET /api/requests/incoming/ - ჩემს წიგნებზე შემოსული მოთხოვნები
 - PUT /api/requests/{id}/handle/ - მოთხოვნის მიღება/უარყოფა

## API დოკუმენტაცია
სერვერის გაშვების შემდეგ დოკუმენტაცია ხელმისაწვდომია მისამართზე:
 - Swagger UI: http://localhost:8000/swagger/

## პროექტის სტრუქტურა
 - book-sharing/
 -    apps/
 -    - authentication/    # მომხმარებლები და ავტორიზაცია
 -    - books/             # წიგნების მართვა
 -    - authors/           # ავტორების მართვა
 -    - requests/          # წიგნების მოთხოვნის სისტემა
 -    config/               # Django პარამეტრები
 -    static/               # სტატიკური ფაილები
 -    media/                # ატვირთული ფაილები
 -    docs/                 # დოკუმენტაცია
 -    tests/                # ტესტები

