from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
import views
import settings
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # View for login page.
    (r'^accounts/login/$',  login, '/public_html/login'),
    (r'^accounts/logout/$', logout, '/public_html/Goodbye/goodbye'),
    #url(r'^login/', 'Frizza.views.login'), #views.LoginView.as_view()),
    # Login is the default page.
    url(r'^$', 'Frizza.views.login', name='login'),
    # View for the disclaimer page.
    url(r'^disclaimer/', 'Frizza.views.disclaimer', name='disclaimer'),
    # View for toppings page.
    url(r'^toppings/', 'Frizza.views.toppings', name='toppings'),
    # View for registration page.
    url(r'^registration/', 'Frizza.views.registration', name='registration'),
    # View for allergies page.
    url(r'^allergies/', 'Frizza.views.allergies', name='allergies'),
    # View for Pizza display page.
    url(r'^pizza/', 'Frizza.views.pizza', name='pizza'),
    # View for crust page.
    url(r'^crust/', 'Frizza.views.crust', name='crust'),
    # View for sauce page.
    url(r'^sauce/', 'Frizza.views.sauce', name='sauce'),
    # View for confirmation page. Currently being displayed by calorie.
    url(r'^confirmation/', 'Frizza.views.calorie', name='confirmation'),
    # View for goodbye page.
    url(r'^goodbye/', 'Frizza.views.goodbye', name='goodbye'),
    # View for login page.
    url(r'^return/', 'Frizza.views.waste', name='return'),
    # This sets up the static section properly so that static content
    # is distributed properly in production.
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
