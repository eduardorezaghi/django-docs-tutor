from unicodedata import name
from django.urls import path
from . import views

# Namespacing urls.py file so templates 
# can reference the correct path 
# (ex.: {% url %}) template notation
app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]