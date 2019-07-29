from django.urls import path
from polls import views
#from polls.views import IndexView

app_name = 'polls'

urlpatterns = [

    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    #path('<int:question_id>/', views.detail, name='detail'),

    #path('<int:question_id>/results/', views.results, name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
    #
    #path('question_form/',views.QuestionFormView.as_view(),name='quesform'),
    path('success/',views.success,name='success'),
    path('question_form/',views.Questionform,name='fun_quesform'),
    #display list of model
    path('data/',views.qdata),
    #display details of model
    path('details/<int:id>/',views.detailqus),
    # delete model data
    path('details/delete/<int:id>/',views.detaildel)
]
