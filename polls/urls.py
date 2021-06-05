from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ejemplo: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ejemplo: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ejemplo: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ejemplo: /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]