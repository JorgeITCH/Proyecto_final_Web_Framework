from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('<int:department_id>/questions/',views.QuestionsView.as_view(),name='questions'),
    path('<int:department_id>/questions/newquestion/',views.CreateQuestionView.as_view(),name='newquestion'),
    path('<int:department_id>/questions/newquestion/createquestion/',views.createquestion, name='createquestion'),
    path('<int:department_id>/questions/deletequestion/<int:question_id>/',views.deletequestion, name='deletequestion'),
    path('<int:department_id>/questions/<int:question_id>/', views.DetailView.as_view(), name='detail'),
    path('<int:department_id>/questions/<int:question_id>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:department_id>/questions/<int:question_id>/vote/', views.vote, name='vote'),
    
]