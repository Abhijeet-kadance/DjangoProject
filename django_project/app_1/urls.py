from django.urls import include,path


urlpatterns = [
    path('app_1/', include('app1.urls')),
]