from django.conf.urls import url,patterns

urlpatterns=patterns('core.views',
    url(r'^$','index',name='index'),
    url(r'^produto/$','product',name='product'),
    url(r'^produtos/$','products',name='products'),
    url(r'^contato/$','contact',name='contact'),
)
