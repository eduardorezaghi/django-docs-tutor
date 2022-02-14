from django.urls import path
from . import views

# Namespacing urls.py file so templates 
# can reference the correct path 
# (ex.: {% url %}) template notation
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]