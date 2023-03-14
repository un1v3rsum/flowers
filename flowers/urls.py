from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from flowers import views

#url paths to admin page, flowers main-page and to a single flower page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flowers/', views.flower_list),
    path('flowers/<int:id>', views.flower_detail)

]

urlpatterns = format_suffix_patterns(urlpatterns)
