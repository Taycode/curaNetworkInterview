from django.urls import path
from api.views import Index, GetPropertyView

urlpatterns = [
    path('', Index.as_view()),
    path('properties/', GetPropertyView.as_view())
]
