from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
import settings
from django.conf.urls.static import static
from django.template import loader
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Login is the default page.
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': settings.TEMPLATE_DIRS + '/public_html/login.html'}, name='login'),
    # View for login page.
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': settings.TEMPLATE_DIRS + '/public_html/login.html'}, name='login'),
    # View for registration page.
    url(r'^registration/', 'Frizza.views.registration', name='registration'),
    # View for the disclaimer page.
    url(r'^disclaimer/', 'Frizza.views.disclaimer', name='disclaimer'),
    # View for Pizza display page.
    url(r'^pizza/', 'Frizza.views.pizza', name='pizza'),
    # View for return page.
    url(r'^return/', 'Frizza.views.return_pizza', name='return'),
    # View for waste page.
    url(r'^waste/', 'Frizza.views.waste', name='waste'),
    # View for crust page.
    url(r'^crust/', 'Frizza.views.crust', name='crust'),
    # View for sauce page.
    url(r'^sauce/', 'Frizza.views.sauce', name='sauce'),
    # View for toppings page.
    url(r'^toppings/', 'Frizza.views.toppings', name='toppings'),
    # View for allergies page.
    url(r'^allergies/', 'Frizza.views.allergies', name='allergies'),
    # View for confirmation page. Currently being displayed by calorie.
    url(r'^confirmation/', 'Frizza.views.calorie', name='confirmation'),
    # View for thank page.
    url(r'^thank/', 'Frizza.views.thank', name='thank'),
    # View for logout page.
    url(r'^logout/', 'django.contrib.auth.views.logout', {'template_name': settings.TEMPLATE_DIRS + '/public_html/logout.html'}, name='logout'),
    # This sets up the static section properly so that static content
    # is distributed properly in production.
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
