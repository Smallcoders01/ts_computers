# ts_computers/urls.py

from django.contrib import admin
from django.urls import path
from myapp.views import home, sub_service_form, about_us, contact_form, contact_us_success  # Update the import statement
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', about_us, name='about_us'),
    path('contact-us/', contact_form, name='contact_us'),  # Update the view name to contact_form
    path('contact-us-success/', contact_us_success, name='contact_us_success'),  # Update the view name
    path('', home, name='home'),
    path('sub-service/<int:service_id>/', sub_service_form, name='sub_service_form'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
