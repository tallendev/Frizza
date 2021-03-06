"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Tyler Allen, Trevor Griggs, Hayden Thomas
"""


from django.conf.urls import patterns, url
from django.conf.urls.static import static

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       # Login is the default page.
                       url(r'^$', 'django.contrib.auth.views.login', {
                       'template_name': settings.TEMPLATE_DIRS + '/public_html/login.html'},
                           name='login'),
                       # View for login page.
                       url(r'^login/', 'django.contrib.auth.views.login', {
                       'template_name': settings.TEMPLATE_DIRS + '/public_html/login.html'},
                           name='login'),
                       # View for registration page.
                       url(r'^registration/', 'Frizza.views.registration',
                           name='registration'),
                       # View for the disclaimer page.
                       url(r'^disclaimer/', 'Frizza.views.disclaimer',
                           name='disclaimer'),
                       # View for Pizza display page.
                       url(r'^pizza/', 'Frizza.views.pizza', name='pizza'),
                       # View for return page.
                       url(r'^return/', 'Frizza.views.return_pizza',
                           name='return'),
                       # View for waste page.
                       url(r'^waste/', 'Frizza.views.waste', name='waste'),
                       # View for crust page.
                       url(r'^crust/', 'Frizza.views.crust', name='crust'),
                       # View for sauce page.
                       url(r'^sauce/', 'Frizza.views.sauce', name='sauce'),
                       # View for toppings page.
                       url(r'^toppings/', 'Frizza.views.toppings',
                           name='toppings'),
                       # View for allergies page.
                       url(r'^allergies/', 'Frizza.views.allergies',
                           name='allergies'),
                       # View for confirmation page. Currently being displayed by calorie.
                       url(r'^confirmation/', 'Frizza.views.confirmation',
                           name='confirmation'),
                       # View for thank page.
                       url(r'^thank/', 'Frizza.views.thank', name='thank'),
                       # View for logout page.
                       url(r'^logout/', 'django.contrib.auth.views.logout', {
                       'template_name': settings.TEMPLATE_DIRS + '/public_html/logout.html'},
                           name='logout'),
                       # This sets up the static section properly so that static content
                       # is distributed properly in production.
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
