from django.shortcuts import render
import settings
from django.contrib import auth
from Frizza.models import User, Sauce, Crust, Pizza, Topping, HasTopping, \
                           Allergy, Orders
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
import logging
from django.db.models import Max
from pizza import PizzaOrder

logger = logging.getLogger('registration')


# This function provides an appropriate response to a request for the pizza
# page.
def pizza(request):
    if request.user.is_authenticated():
        order_list = Orders.objects.filter(user_name="admin")
        admin_list = Pizza.objects.filter(pizza_id=order_list).select_related()
        #TODO add user stuff
        if request.method == 'POST':
            print(request.POST)
            request.session['pizza'] = ''
            post = request.POST
            pizza = request.POST['pizza']
            #FIXME are these conditions right?
            if pizza == 'Make Your Own!':
                return HttpResponseRedirect('/crust')

            # need else here to dynamically rebuild prebuilt pizzas
            context = {'admin_list': admin_list}
            print ("Context: " + str(admin_list) + "\n")
            return render(request, settings.TEMPLATE_DIRS +
                               '/public_html/Pizza/pizza.html', context)
        else:
            context = {'admin_list': admin_list}
            print ("Context: " + str(admin_list) + "\n")
            return render(request, settings.TEMPLATE_DIRS +
                                   '/public_html/Pizza/pizza.html', context)
    else:
        return HttpResponseRedirect('/login')


# This function provides an appropriate response to a request for the toppings
# page.
def toppings(request):
    if request.user.is_authenticated():
        if 'pizza' in request.session:
            if 'crust' in request.session:
                if 'sauce' in request.session:
                    topping_list = Topping.objects.all()
                    if request.method == 'POST':
                        for i in topping_list:
                            print(str(i))
                            if str(i) in request.POST:
                                print("Whee!")
                                request.session[str(i)] = str(i)
                        print(str(request.session))
                        return HttpResponseRedirect('/allergies')
                    else:
                        context = {'topping_list': topping_list}
                        return render(request, settings.TEMPLATE_DIRS +
                               '/public_html/Toppings/toppings.html', context)
                else:
                    return HttpResponseRedirect('/sauce')
            else:
                return HttpResponseRedirect('/crust')
        else:
            return HttpResponseRedirect('/pizza')
    else:
        return HttpResponseRedirect('/login')


# This function provides an appropriate response to a request for the crust
# page.
def crust(request):
    if request.user.is_authenticated():
        if 'pizza' in request.session:
            #TODO maybe change for redirect?
            if request.method == 'POST' and 'crust' in request.POST:
                request.session['crust'] = request.POST['crust']
                return HttpResponseRedirect('/sauce')
            else:
                crust_list = Crust.objects.all()
                context = {'crust_list': crust_list}
                return render(request, settings.TEMPLATE_DIRS +
                                   '/public_html/Crust/crust.html', context)
        else:
            return HttpResponseRedirect('/pizza')
    else:
        return HttpResponseRedirect('/login')


# This function provides the appropriate response to a request for the sauce
# page.
def sauce(request):
    if request.user.is_authenticated():
        if 'pizza' in request.session:
            if 'crust' in request.session:
                if request.method == 'POST' and 'sauce' in request.POST:
                    request.session['sauce'] = request.POST['sauce']
                    return HttpResponseRedirect('/toppings')
                else:
                    sauce_list = Sauce.objects.all()
                    context = {'sauce_list': sauce_list}
                # TODO Check for Post
                    return render(request, settings.TEMPLATE_DIRS +
                                   '/public_html/Sauce/sauce.html', context)
            else:
                return HttpResponseRedirect('/crust')
        else:
            return HttpResponseRedirect('/pizza')
    else:
        return HttpResponseRedirect('/login')


#This function does not work, but we would like to revisit it in the future.
def allergies(request):
#=======
    # Sausage is a placeholder for the actual, variable pizza name.
#    pizza = Pizza.objects.get(pizza_name="Sausage")
#    crust = Crust.objects.get(crust_name=pizza.crust_name);
#    sauce = Sauce.objects.get(sauce_name=pizza.sauce_name);

#    pizzaToppings = HasTopping.objects.filter(pizza_name=pizza.pizza_name)

#    topping_allergies = []    

#    for topping in pizzaToppings:
#        allergies = Allergy.objects.filter(ingredient_name=topping.topping_name)        
        
#        for allergy in allergies:
#            topping_allergies.append(allergy)

#    sauce_allergies = Allergy.objects.filter(ingredient_name=sauce.sauce_name)
#    crust_allergies = Allergy.objects.filter(ingredient_name=crust.crust_name)

#    context =  {
#        'topping_allergies': topping_allergies,
#        'sauce_allergies': sauce_allergies,
#        'crust_allergies': crust_allergies,
#    }
#    return render(request, settings.TEMPLATE_DIRS +
#                  '/public_html/Allergies/allergies.html', context)

#=======
    if request.user.is_authenticated():
        if (request.method == 'POST'):
            return HttpResponseRedirect('/confirmation')
        else:
            #FIXME lists all allergies
            allergies_list = Allergy.objects.all()
            context = {'allergy_list': allergies_list}
            return render(request, settings.TEMPLATE_DIRS +
                               '/public_html/Allergies/allergies.html', context)
    else:
        return HttpResponseRedirect('/login')
     
# This function provides an appropriate response to a request for the calorie
# page.

def calorie(request):
    if request.user.is_authenticated():
        #TODO: Validate appropriate fields are filled out
        if request.method == 'POST':
            current_id = Pizza.objects.all().\
                         aggregate(Max('pizza_id'))['pizza_id__max']
            pizza_id = 0
            if request.session['pizza'] == '':
                pizza_id = 1
                pizza = Pizza(current_id, str(request.POST['pizza_name']), pizza_id,
                      request.session['sauce'], request.session['crust'])
                pizza.save()
            #else
            topping_list = Topping.objects.all()
            for topping in topping_list:
                if str(topping) in request.session:
                    HasTopping(pizza_id=pizza, topping_name=topping).save()
            Orders(user_name=(User.objects.filter(user_name=str(request.user)))['User'], pizza_id=pizza).save()
            return HttpResponseRedirect('/goodbye')
        else:
            pizza = None
            crust = None
            sauce = None
            crust_calorie = 0
            sauce_calorie = 0
            top_cal_sum = 0
            toppings = []
            pizza_name = request.session['pizza']
            if pizza_name != '':
                pizza = Pizza.objects.get(pizza_name=request.session['pizza'])
                crust = Crust.objects.get(crust_name=pizza.crust_name)
                crust_calorie = crust.calorie
    
                sauce = Sauce.objects.get(sauce_name=pizza.sauce_name)
                sauce_calorie = sauce.calorie

                hasToppings = HasTopping.objects.filter(pizza_id=pizza.pizza_id)

                for ht in hasToppings:
                    topping = Topping.objects.get(topping_name=ht.topping_name)
                    toppings.append(topping)
                    top_cal_sum = top_cal_sum + topping.calorie
            else:
                crust = Crust.objects.get(crust_name=request.session['crust'])
                sauce = Sauce.objects.get(sauce_name=request.session['sauce'])
                crust_calorie = crust.calorie
                sauce_calorie = sauce.calorie
                topping_list = Topping.objects.all()
                topping_str = []
                for topping in topping_list:
                    if str(topping) in request.session:
                        topping_str.append(topping)
                for topping in topping_str:
                    topping = Topping.objects.get(topping_name=topping)
                    toppings.append(topping)
                    top_cal_sum += topping.calorie

            cal_total = top_cal_sum + sauce_calorie + crust_calorie
    
            context = {'crust': crust,
                        'sauce': sauce,
                        'toppings': toppings,
                        'cal_total': cal_total}
            return render(request, settings.TEMPLATE_DIRS +
                         '/public_html/Confirmation/confirmation.html', context)
    else:
         return HttpResponseRedirect('/login')


# This function provides an appropriate response to a request for the
# returns/waste page.
def waste(request):
    if request.user.is_authenticated():
        pizza = Pizza.objects.get(pizza_name="Pepperoni")
        wasted_toppings = HasTopping.objects.filter(pizza_id=pizza.pizza_id).\
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
                  "/public_html/Goodbye/goodbye.html")


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
#    return render(request, settings.TEMPLATE_DIRS + "/public_html/login/")
    return render(request, settings.TEMPLATE_DIRS + "/public_html/logout/")
