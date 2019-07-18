from django.urls import path
from polls import views
# urlpatterns = [
#     path("",views.index,name = "index"),
#     path('detail/<int:question_id>/',views.detail,name = "detail"),
#     path('results/<int:question_id>/',views.results,name = "results"),
#     path('vote/<int:question_id>/',views.vote,name = "vote"),
# ]

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
