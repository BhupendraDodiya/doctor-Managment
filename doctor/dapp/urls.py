from django.urls import path
from dapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('signup/',views.signup),
    path('login/',views.login),
    path('lreg/',views.lreg),
    path('table/',views.table),
    path('delete/<int:uid>/',views.delete),
    path('update/<int:uid>/',views.update),
    path('ureg/',views.ureg)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
