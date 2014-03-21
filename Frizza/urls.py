from django.conf.urls import patterns, include, url
import views
import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Frizza.views.home', name='home'),
    # url(r'^Frizza/', include('Frizza.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^disclaimer/', views.DisclaimerView.as_view(), name='disclaimer'),
    #url(r'^admin/', include('admin.urls')),
    url(r'^toppings/', 'Frizza.views.toppings', name='toppings'),
    url(r'^allergies/', 'Frizza.views.allergy', name='allergies'),
    url(r'^pizza/', 'Frizza.views.pizza', name='pizza'),
    url(r'^crust/', 'Frizza.views.crust', name='crust'),
    url(r'^sauce/', 'Frizza.views.sauce', name='sauce'),
    url(r'^confirmation/', 'Frizza.views.calorie', name='confirmation'),
    url(r'^goodbye/', views.GoodbyeView.as_view(), name='goodbye'),
    url(r'^return/', 'Frizza.views.waste', name='return'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
