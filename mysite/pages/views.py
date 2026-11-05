from django.http import HttpResponse, Http404,HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import date

#Наконец-то
MESSAGES = []  # временное хранилище, пока нет базы данных

PRODUCTS = [
    {"id": 1, "name": "Ноутбук", "price": 450000, "category": "Компьютеры",
     "in_stock": True, "rating": 4.7, "description": "Лёгкий ноутбук для учёбы и работы."},
    {"id": 2, "name": "Смартфон", "price": 220000, "category": "Телефоны",
     "in_stock": True, "rating": 4.5, "description": "Экран 6,5 дюйма, камера 50 Мп."},
    {"id": 3, "name": "Наушники", "price": 35000, "category": "Аксессуары",
     "in_stock": False, "rating": 4.1, "description": None},
    {"id": 4, "name": "Клавиатура", "price": 18000, "category": "Аксессуары",
     "in_stock": True, "rating": 3.9, "description": ""},
    {"id": 5, "name": "Монитор", "price": 120000, "category": "Компьютеры",
     "in_stock": False, "rating": 4.6, "description": "Диагональ 27 дюймов, IPS."},
]


COURSES2 = [
    {"id": 1, "name": "Python для начинающих", "hours": 36},
    {"id": 2, "name": "Веб-разработка на Django", "hours": 48},
    {"id": 3, "name": "Алгоритмы и структуры данных", "hours": 24},
    {"id": 4, "name": "Базы данных и SQL", "hours": 30},
]

COURSES = [
    {"id": 1, "title": "Python для начинающих", "teacher": "Алексей Иванов", "hours": 36, "price": 15000, "is_open": True, "about": "Базовый курс по программированию на Python с нуля."},
    {"id": 2, "title": "Веб-разработка на Django", "teacher": "Айдана Султанова", "hours": 48, "price": 25000, "is_open": True, "about": ""},
    {"id": 3, "title": "Алгоритмы и структуры данных", "teacher": "Иван Петров", "hours": 24, "price": 10000, "is_open": False, "about": "Углубленное изучение алгоритмов и структур."},
    {"id": 4, "title": "Базы данных и SQL", "teacher": "Ольга Смирнова", "hours": 30, "price": 12000, "is_open": True, "about": "Реляционные БД, PostgreSQL, написание запросов."},
    {"id": 5, "title": "Machine Learning Intro", "teacher": "Тимур Бек", "hours": 60, "price": 45000, "is_open": False, "about": None},
]


ENROLLED_STUDENTS = []  # Временное хранилище заявок на курсы


def home(request):
    context = {
        "title": "Главная",
        "user_name": "Байстан",
        "today": date.today(),
        "total": len(PRODUCTS),
    }
    return render(request, "pages/home.html", context)


def about(request):
    return render(request, "pages/about.html")


def contacts(request):
    return render(request, "pages/contacts.html")


def services(request):
    return render(request, "pages/services.html")


def portfolio(request):
    return render(request, "pages/portfolio.html")


def greet(request):
    context = {
        "name": request.GET.get("name", "Гость")
    }
    return render(request, "pages/greet.html", context)


# Старый product_list из практики 5
# def product_list(request):
#     lines = ["<h1>Каталог</h1>", "<ul>"]
#     for item in PRODUCTS:
#         lines.append(
#             f'<li><a href="/products/{item["id"]}/">{item["name"]}</a></li>'
#         )
#     lines.append("</ul>")
#     return HttpResponse("".join(lines))

def product_list(request):
    return render(request, "pages/product_list.html",
                  {"title": "Каталог", "products": PRODUCTS})


# Старый product_detail
# def product_detail(request, product_id):
#     for item in PRODUCTS:
#         if item["id"] == product_id:
#             return HttpResponse(
#                 f"<h1>{item['name']}</h1>"
#                 f"<p>Цена: {item['price']} сом</p>"
#                 '<a href="/products/">Назад к каталогу</a>'
#             )
#     raise Http404("Товар не найден")

def product_detail(request, product_id):
    for item in PRODUCTS:
        if item["id"] == product_id:
            return render(request, "pages/product_detail.html",
                          {"title": item["name"], "product": item})
    raise Http404("Товар не найден")


def search(request):
    q = request.GET.get("q", "").strip().lower()
    found = [i for i in PRODUCTS if q in i["name"].lower()]
    if not q:
        return HttpResponse("Введите запрос: /search/?q=ноут")
    if not found:
        return HttpResponse(f"По запросу «{q}» ничего не найдено")
    names = ", ".join(i["name"] for i in found)
    return HttpResponse(f"Найдено: {names}")


def feedback(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        message = request.POST.get("message", "").strip()
        if name and message:
            MESSAGES.append({"name": name, "message": message})
            return redirect("pages:feedback_done")
    return render(request, "pages/feedback.html")


def feedback_done(request):
    context = {
        "total": len(MESSAGES),
    }
    return render(request, "pages/feedback_done.html", context)


def api_products(request):
    return JsonResponse({"count": len(PRODUCTS), "items": PRODUCTS})


def api_product(request, product_id):
    for item in PRODUCTS:
        if item["id"] == product_id:
            return JsonResponse(item)
    return JsonResponse({"error": "not found"}, status=404)


def subscribe(request):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])
    email = request.POST.get("email", "")
    return HttpResponse(f"Подписка оформлена: {email}")


def request_info(request):
    html = (
        f"<p>Метод: {request.method}</p>"
        f"<p>Путь: {request.path}</p>"
        f"<p>Параметры GET: {dict(request.GET)}</p>"
        f"<p>Браузер: {request.META.get('HTTP_USER_AGENT', '-')}</p>"
    )
    return HttpResponse(html)


def calculate_square(request, n):
    result = n ** 2
    return HttpResponse(f"Квадрат числа {n} равен {result}")


def course_list_by_hour(request):
    context = {
        "title": "Список курсов",
        "courses": COURSES2,
        "total": len(COURSES2),
    }

    return render(request, "pages/course_list_by_hour.html", context)


def course_list(request):
    return render(request, "pages/course_list.html", {
        "title": "Список курсов",
        "courses": COURSES
    })

def course_by_hour_detail(request, course_id):
    for course in COURSES2:
        if course["id"] == course_id:
            context = {
                "title": "Детали курса",
                "course": course,
            }
            return render(request, "pages/course_by_hour_detail.html", context)

    raise Http404("Курс не найден")



def course_detail(request, course_id):
    for item in COURSES:
        if item["id"] == course_id:
            return render(request, "pages/course_detail.html", {
                "title": item["title"],
                "course": item
            })
    raise Http404("Курс не найден")


def course_enroll(request, course_id):
    for course in COURSES:
        if course["id"] == course_id:
            if request.method == "POST":
                name = request.POST.get("name")
                email = request.POST.get("email")

                if name and email:
                    return redirect("pages:enroll_success")

            context = {
                "title": "Запись на курс",
                "course": course,
            }

            return render(request, "pages/course_enroll.html", context)

    raise Http404("Курс не найден")



def course_enroll_done(request):
    return HttpResponse(
        f"<h1>Успешно!</h1><p>Всего заявок на курсы: {len(ENROLLED_STUDENTS)}</p>"
        '<a href="/courses/">Вернуться к каталогу курсов</a>'
    )


def hello(request):
    name = request.GET.get("name", "")
    return render(request, "pages/hello.html",
                  {"title": "Приветствие", "name": name})
