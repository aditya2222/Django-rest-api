from django.urls import path
from rest_framework.routers import DefaultRouter
from snippets import views



# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)

# # Schema view for our api
# schema_view = get_schema_view(title='Pastebin API')



urlpatterns = [
    path('snippets/',views.snippet_list),
    path('snippets/<int:pk>/',views.snippet_detail),
    
]