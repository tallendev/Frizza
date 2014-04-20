from django.shortcuts import render
from django.views.generic import TemplateView
import settings
from django.contrib import auth
from Frizza.models import User, Sauce, Crust, Pizza, Topping, HasTopping, \
                           Allergy, Orders
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
import logging

logger = logging.getLogger('registration')


# This function provides an appropriate response to a request for the pizza
# page.
def pizza(request):
    if request.user.is_authenticated():
        admin_list = Orders.objects.filter(user_name="admin")#.select_related('pizza_id')
        context = {'admin_list': admin_list}
        print ("Context: " + str(context) + "\n")
        return render(request, settings.TEMPLATE_DIRS +
                               '/public_html/Pizza/pizza.html', context)
    else:
        return HttpResponseRedirect('/login')


# This function provides an appropriate response to a request for the toppings
# page.
def toppings(request):
    if request.user.is_authenticated():
        topping_list = Topping.objects.all()
        context = {'topping_list': topping_list}
        return render(request, settings.TEMPLATE_DIRS +
                               '/public_html/Toppings/toppings.html', context)
    else:
        return HttpResponseRedirect('/login')


# This function provides an appropriate response to a request for the crust
# page.
def crust(request):
    if request.user.is_authenticated():
        crust_list = Crust.objects.all()
        context = {'crust_list': crust_list}
        return render(request, settings.TEMPLATE_DIRS +
                               '/public_html/Crust/crust.html', context)
    else:
        return HttpResponseRedirect('/login')


# This function provides the appropriate response to a request for the sauce
# page.
def sauce(request):
    if request.user.is_authenticated():
        sauce_list = Sauce.objects.all()
        context = {'sauce_list': sauce_list}
        return render(request, settings.TEMPLATE_DIRS +
                               '/public_html/Sauce/sauce.html', context)
    else:
        return HttpResponseRedirect('/login')


#This function does not work, but we would like to revisit it in the future.
def allergies(request):
    if request.user.is_authenticated():
        allergies_list = Allergy.objects.all()
        context = {'allergy_list': allergies_list}
        return render(request, settings.TEMPLATE_DIRS +
                               '/public_html/Allergy/allergy.html', context)
    else:
        return HttpResponseRedirect('/login')
    # topping_allergies = HasTopping.objects.filter(pizza_name="Sausage") \
    #                         .select_related('allergy__ingredient_name')
     
# topping_allergies = HasTopping.objects.raw('''SELECT topping_name, FROM frizza_hastopping as h, \
#                            frizza_allergy as a, \
#                            WHERE a.ingredient_name=h.topping_name \
#                            and h.pizza_name=Sausage''')    

    #sauce_allergies = Pizza.objects.filter(pizza_name="Sausage") \
    #                        .select_related('allergy__ingredient_name')

    #crust_allergies = Pizza.objects.filter(pizza_name="Sausage") \
    #                         .select_related('allergy__ingredient_name')

#    template = loader.get_template(settings.TEMPLATE_DIRS + \
 #                                   '/public_html/Allergies/allergies.html')
  #  context = RequestContext(request, {
   #     'topping_allergies': topping_allergies,
    #    'sauce_allergies': sauce_allergies,
    #    'crust_allergies': crust_allergies,
   # })
   # print(str(topping_allergies))
    #print(str(sauce_allergies))
    #print(str(crust_allergies))
   # return HttpResponse(template.render(context))

# This function provides an appropriate response to a request for the calorie
# page.


def calorie(request):
    if request.user.is_authenticated():
        pizza = Pizza.objects.get(pizza_name="Sausage")
        crust = Crust.objects.get(crust_name=pizza.crust_name)
        crust_calorie = crust.calorie
    
        sauce = Sauce.objects.get(sauce_name=pizza.sauce_name)
        sauce_calorie = sauce.calorie

        hasToppings = HasTopping.objects.filter(pizza_name=pizza.pizza_name)
    
        top_cal_sum = 0
        for ht in hasToppings:
            topping = Topping.objects.get(topping_name = ht.topping_name)
            top_cal_sum = top_cal_sum + topping.calorie
    
        cal_total = top_cal_sum + sauce_calorie + crust_calorie
    
        context = {'cal_total': cal_total}
        return render(request, settings.TEMPLATE_DIRS +
                      '/public_html/Confirmation/confirmation.html', context)
    else:
        return HttpResponseRedirect('/login')


# This function provides an appropriate response to a request for the
# returns/waste page.
def waste(request):
    if request.user.is_authenticated():
        wasted_toppings = HasTopping.objects.filter(pizza_name="Pepperoni").\
                                     select_related('orders__pizza_name')

        wasted_sauce = Pizza.objects.filter(pizza_name="Pepperoni").\
                             select_related('orders__pizza_name')

        wasted_crust = Pizza.objects.filter(pizza_name="Pepperoni").\
                             select_related('orders__pizza_name')

        context = {'wasted_toppings': wasted_toppings,
                   'wasted_sauce': wasted_sauce,
                   'wasted_crust': wasted_crust}

        return render(request, settings.TEMPLATE_DIRS +
                               '/public_html/Return/return.html', context)
    else:
        return HttpResponseRedirect('/login')


def disclaimer(request):
    if request.user.is_authenticated():
        return render(request, settings.TEMPLATE_DIRS +
                      '/public_html/Disclaimer/disclaimer.html')
    else:
        return HttpResponseRedirect('/login')


# This function provides the appropriate response to a request for the
# registration page.
def registration(request):
    logger.debug('In registration')
    if request.method == 'POST':
        logger.debug('Successful post from registration')
        post = request.POST
        form = UserCreationForm(post, request)

        print('Post: ' + str(request.POST))
        #print('Errors: ' + str(form.error_messages))
        print('Is Valid: ' + str(form.is_valid()))
        print('More Errors: ' + str(form.errors) + "\n\n")
        if form.is_valid():
            username = post.get('username', '')
            #email = post.get('Email', '')
            password = post.get('password1', '')
            logger.debug('Is_Valid from registration')
            u = User(user_name=username, password=password)
            u.save()
            new_user = form.save()
            registration_list = User.objects.all()  # Registration?
            context = {'registration_list': registration_list}
            return HttpResponseRedirect('/disclaimer')
            #return HttpResponseRedirect("/disclaimer")

        #User.
    registration_list = User.objects.all()  # Registration?
    context = {'registration_list': registration_list}
    return render(request, settings.TEMPLATE_DIRS +
                '/public_html/Registration/registration.html', context)


def login(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}

    #username = request.POST.get('username', '')
    #password = request.POST.get('password', '')
    #user = auth.authenticate(username=username, password=password)
    #if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
     #   auth.login(request, user)
        # Redirect to a success page.
      #  return HttpResponseRedirect(settings.TEMPLATE_DIRS + "/public_html/Disclaimer/disclaimer.html")
    #else:
        # Show an error page
    return render(request, settings.TEMPLATE_DIRS +
                  '/public_html/login.html', context)


def goodbye(request):
    # Redirect to a success page.
    return render(request, settings.TEMPLATE_DIRS +
                  "/public_html/Goodbye/goodbye/")


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return render(request, settings.TEMPLATE_DIRS + "/public_html/logout/")
