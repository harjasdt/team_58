from django.urls import path
from . import views
from django.views.generic import TemplateView






urlpatterns = [
    path('',views.home,name='home'),
    path('getting/',views.getting,name='getting'),
    path('models/',views.pest,name='pest'),
    path('clear/',views.clear,name='clear'),
    path('history/',views.history,name='history'),
    path('predhistory/',views.predhistory,name='predhistory'),


    # path('goodhome/',views.goodhome,name='goodhome'),
    

    path('test/',views.test,name='test'),
    # path('multiemail_static/',views.static,name='home'),
    # path('multiemail_dynamic/',views.dynamic,name='d'),
    # path('', TemplateView.as_view(
    #     template_name='docs.html',
    #     extra_context={'schema_url':'api_schema'}
    #     ), name='swagger-ui'),

    path('security/',views.securehome,name='securehome'),
    path('doorstatus/',views.doorstatus,name='doorstatus'),
    path('updatestatus/',views.updatestatus,name='safesafe'),
    path('newstatus/',views.newstatus,name='newstaut'),
    path('reqactive/',views.reqactive,name='activestate'),
    path('changeactive/',views.changeactive,name='change'),
    path('failhistory/',views.failhistory,name='failhistory'),
    path('sendtemp/',views.sendtemp,name='temp'),

    
    ]