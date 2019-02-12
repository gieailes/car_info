from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from cars import views

urlpatterns = [
    path('',('cars.urls')),
    path('cars/', views.car_list),
    path('cars/<int:pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
