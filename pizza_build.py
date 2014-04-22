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
cheese = Topping('Cheese', 200)
cheese.save()
pepperoni = Topping('Pepperoni', 200)
pepperoni.save()
sausage = Topping('Sausage', 200)
sausage.save()
ham = Topping('Ham', 200)
ham.save()
bacon = Topping('Bacon', 250)
bacon.save()
pineapple = Topping('Pineapple', 100)
pineapple.save()
mushrooms = Topping('Mushrooms', 80)
mushrooms.save()
spinach = Topping('Spinach', 75)
spinach.save()
green_peppers = Topping('Green Peppers', 50)
green_peppers.save()
onions = Topping('Onions', 50)
onions.save()
black_olives = Topping('Black Olives', 60)
black_olives.save()

from Frizza.models import Pizza
cheese_p = Pizza(1, 'Cheese', 1, 'Tomato', 'Classic')
cheese_p.save()
pepperoni_p = Pizza(2, 'Pepperoni', 2, 'Tomato', 'Classic')
pepperoni_p.save()
sausage_p = Pizza(3, 'Sausage', 3, 'Tomato', 'Classic')
sausage_p.save()
meat_lovers = Pizza(4, 'Meat Lovers', 4, 'Tomato', 'Classic')
meat_lovers.save()
hawaiian = Pizza(5, 'Hawaiian', 5, 'Tomato', 'Classic')
hawaiian.save()
vegetarian = Pizza(6, 'Vegetarian', 6, 'Tomato', 'Classic')
vegetarian.save()

from Frizza.models import HasTopping
##### 1 #####
HasTopping(pizza_id=cheese_p, topping_name=cheese).save()
##### 2 #####
HasTopping(pizza_id=pepperoni_p, topping_name=cheese).save()
HasTopping(pizza_id=pepperoni_p, topping_name=pepperoni).save()
##### 3 #####
HasTopping(pizza_id=sausage_p, topping_name=cheese).save()
HasTopping(pizza_id=sausage_p, topping_name=sausage).save()
##### 4 #####
HasTopping(pizza_id=hawaiian, topping_name=cheese).save()
HasTopping(pizza_id=hawaiian, topping_name=pineapple).save()
HasTopping(pizza_id=hawaiian, topping_name=bacon).save()
##### 5 #####
HasTopping(pizza_id=meat_lovers, topping_name=cheese).save()
HasTopping(pizza_id=meat_lovers, topping_name=pepperoni).save()
HasTopping(pizza_id=meat_lovers, topping_name=sausage).save()
HasTopping(pizza_id=meat_lovers, topping_name=bacon).save()
HasTopping(pizza_id=meat_lovers, topping_name=ham).save()
##### 6 #####
HasTopping(pizza_id=vegetarian, topping_name=cheese).save()
HasTopping(pizza_id=vegetarian, topping_name=mushrooms).save()
HasTopping(pizza_id=vegetarian, topping_name=spinach).save()
HasTopping(pizza_id=vegetarian, topping_name=green_peppers).save()
HasTopping(pizza_id=vegetarian, topping_name=onions).save()
HasTopping(pizza_id=vegetarian, topping_name=black_olives).save()

from Frizza.models import Allergy
Allergy(1, 'Gluten', 'Thick').save()
Allergy(2, 'Dairy', 'Thick').save()
Allergy(3, 'Gluten', 'Thin').save()
Allergy(4, 'Gluten', 'Classic').save()
Allergy(5, 'Dairy', 'Classic').save()
Allergy(6, 'Dairy', 'Alfredo').save()
Allergy(7, 'Dairy', 'Cheese').save()
Allergy(8, 'Soybean', 'Bacon').save()

from Frizza.models import User
User(user_name='admin', password='admin').save()

from Frizza.models import Orders
Orders(1, 'admin', 1).save()
Orders(2, 'admin', 2).save()
Orders(3, 'admin', 3).save()
Orders(4, 'admin', 4).save()
Orders(5, 'admin', 5).save()
Orders(6, 'admin', 6).save()
