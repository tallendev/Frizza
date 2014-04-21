#!/usr/bin/python
#import Frizza.settings
#settings.configure()
from Frizza.models import Sauce
Sauce('Tomato', 100).save()
Sauce('Alfredo', 200).save()
Sauce('Olive Oil', 40).save()
from Frizza.models import Crust
Crust('Thick', 150).save()
Crust('Thin', 75).save()
Crust('Classic', 115).save()
from Frizza.models import Topping
Topping('Cheese', 200).save()
Topping('Pepperoni', 200).save()
Topping('Sausage', 200).save()
Topping('Ham', 200).save()
Topping('Bacon', 250).save()
Topping('Pineapple', 100).save()
Topping('Mushrooms', 80).save()
Topping('Spinach', 75).save()
Topping('Green Peppers', 50).save()
Topping('Onions', 50).save()
Topping('Black Olives', 60).save()
from Frizza.models import Pizza
Pizza(1, 'Cheese', 1, 'Tomato', 'Classic').save()
Pizza(2, 'Pepperoni', 2, 'Tomato', 'Classic').save()
Pizza(3, 'Sausage', 3, 'Tomato', 'Classic').save()
Pizza(4, 'Hawaiian', 4, 'Tomato', 'Classic').save()
Pizza(5, 'Vegetarian', 5, 'Tomato', 'Classic').save()
#from Frizza.models import Allergy
#Allergy('Gluten', 'Thick')
#Allergy('Gluten', 'Thin')
#Allergy('Gluten', 'Classic')
from Frizza.models import HasTopping
from Frizza.models import User
User(user_name='admin', password='admin')
from Frizza.models import Orders
Orders(1, 'admin', 1).save()
Orders(2, 'admin', 2).save()
Orders(3, 'admin', 3).save()
Orders(4, 'admin', 4).save()
Orders(5, 'admin', 4).save()
