from django.urls import include, path
from django.conf.urls.static import static
from server import settings
from djangoTest import views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('allauth.urls')),
    path('add_work/', views.add_work, name='add_work'),
    path('work_update/<int:pk>', views.work_update, name='work_update'),
    path('work_delete/<int:pk>', views.work_delete, name='work_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)