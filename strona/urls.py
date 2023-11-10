from django.urls import path
from . import views

# URL Conf module
urlpatterns = [
    path('szyfr/',views.kod)
]