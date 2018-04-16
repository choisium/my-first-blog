from django.conf.urls import url # django 메소드
from . import views # 우리가 만들 view들

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
