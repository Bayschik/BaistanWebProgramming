# pages/urls.py
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('greet/', views.greet, name='greet'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/done/', views.feedback_done, name='feedback_done'),
    path('api/products/', views.api_products, name='api_products'),
    path('api/products/<int:product_id>/', views.api_product, name='api_product'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('info/', views.request_info, name='request_info'),
    path('square/<int:n>/', views.calculate_square, name='calculate_square'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/enroll/', views.course_enroll, name='course_enroll'),
    path('courses/enroll/done/', views.course_enroll_done, name='course_enroll_done'),
    path('hello/', views.hello, name='hello'),
    path('course_list_by_hour/', views.course_list_by_hour, name='course_list_by_hour'),
]
