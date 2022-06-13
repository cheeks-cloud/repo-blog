from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('add/',views.new_project,name = 'new-project'),
    path('views/',views.new_review,name = 'new-review'),
    path('allviews/',views.reviews,name = 'reviews'),
    path("user", views.userpage, name = "userpage"),
    path('search/',views.search,name = 'search'),
    path('projects/', views.ProjectsList.as_view(),name = 'project'),
    path('projects/<int:pk>/', views.ProjectsDetail.as_view()),
    path('profiles',views.ProfileList.as_view(),name = 'profile_list'),
    path('api/', views.api_root),
]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)