from django.shortcuts import render
from django.views.generic import TemplateView
import settings
from django.contrib import auth
from Frizza.models import User, Sauce, Crust, Pizza, Topping, HasTopping, \
                          Orders, Allergy
from django.db.models import F


# This function provides an appropriate response to a request for the pizza
# page.
def pizza(request):
    admin_list = Orders.objects.filter(user_name="admin")
    #user_list = Orders.objects.filter(user_name=USER)
    context = {'admin_list': admin_list}
    #context = {'user_list': user_list}
    return render(request, settings.TEMPLATE_DIRS +
                  '/public_html/Pizza/pizza.html', context)


# This function provides an appropriate response to a request for the toppings
# page.
def toppings(request):
    topping_list = Topping.objects.all()
    context = {'topping_list': topping_list}
    return render(request, settings.TEMPLATE_DIRS +
                  '/public_html/Toppings/toppings.html', context)


# This function provides an appropriate response to a request for the crust
# page.
def crust(request):
    crust_list = Crust.objects.all()
    context = {'crust_list': crust_list}
    return render(request, settings.TEMPLATE_DIRS +
                  '/public_html/Crust/crust.html', context)


# This function provides the appropriate response to a request for the sauce
# page.
def sauce(request):
    sauce_list = Sauce.objects.all()
    context = {'sauce_list': sauce_list}
    return render(request, settings.TEMPLATE_DIRS +
                  '/public_html/Sauce/sauce.html', context)


#This function does not work, but we would like to revisit it in the future.
def allergy(request):
    allergy_list = Allergy.objects.all()
    context = {'allergy_list': allergy_list}
    return render(request, settings.TEMPLATE_DIRS +
                  '/public_html/Allergy/allergy.html', context)

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
    pizza = Pizza.objects.get(pizza_name="Sausage") 
    crust = Crust.objects.get(crust_name=pizza.crust_name)
    crust_calorie = crust.calorie
    
    sauce = Sauce.objects.get(sauce_name=pizza.sauce_name)
    sauce_calorie = sauce.calorie

    hasToppings = HasTopping.objects.filter(pizza_name=pizza.pizza_name)
    
    top_cal_sum = 0
    for ht in hasToppings:
        topping = Topping.objects.get(topping_name = ht.topping_name)
        top_cal_sum = top_cal_sum + topping.calorie;
    
    cal_total = top_cal_sum + sauce_calorie + crust_calorie
    
    context = {'cal_total': cal_total}
    return render(request, settings.TEMPLATE_DIRS +
                  '/public_html/Confirmation/confirmation.html', context)


# This function provides an appropriate response to a request for the 
# returns/waste page.
def waste(request):
    wasted_toppings = HasTopping.objects.filter(pizza_name="Pepperoni").select_related('orders__pizza_name')

    wasted_sauce = Pizza.objects.filter(pizza_name="Pepperoni").select_related('orders__pizza_name')

    wasted_crust = Pizza.objects.filter(pizza_name="Pepperoni").select_related('orders__pizza_name')
     
    context = {'wasted_toppings': wasted_toppings,
               'wasted_sauce': wasted_sauce,
               'wasted_crust': wasted_crust}
    return render(request, settings.TEMPLATE_DIRS +
                  '/public_html/Return/return.html', context)


def disclaimer(request):
    if request.user.is_authenticated():
        return render(request, settings.TEMPLATE_DIRS +
                      '/public_html/Disclaimer/disclaimer.html')
    else:
        return login(request)


# This function provides the appropriate response to a request for the
# registration page.
def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print(username)
        #User.
    else:
        registration_list = User.objects.all() #Registration?
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
    auth.logout(request)
    # Redirect to a success page.
    return render(request, settings.TEMPLATE_DIRS + "/public_html/login/")