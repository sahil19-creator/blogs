from django.contrib import admin
from django.urls import path
from .import views
urlpatterns=[
     path("",views.dashboard,name="dashboard"),
     path("archieve",views.archieve,name="archieve"),
     path("tags",views.tags,name="tags"),
     path("view/<int:id>",views.blog_view,name="view"),
      path("tag_list/<int:id>",views.tag_list,name="tag_list"),
      path("month_list/<year>/<month>",views.month_list,name="month_list"),
      path("year_list/<year>",views.year_list,name="year_list"),
 ]