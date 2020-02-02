
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/currency', views.CurrencyList.as_view(), name='currency'),
    path(r'api/currency/<str:name>', views.CurrencyDetails.as_view(), name='currency-details'),
    path(r'api/convert/(<int:amount>/(<str:from_currency>/<str:to_currency>)',
        views.CurrencyConvert.as_view(), name='convert'),

]

