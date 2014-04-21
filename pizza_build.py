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
cheese_p = Pizza(1, 'Cheese', 1, 'Tomato', 'Classic')
cheese_p.save()
Pizza(2, 'Pepperoni', 2, 'Tomato', 'Classic').save()
Pizza(3, 'Sausage', 3, 'Tomato', 'Classic').save()
Pizza(4, 'Meat Lovers', 4, 'Tomato', 'Classic').save()
Pizza(5, 'Hawaiian', 5, 'Tomato', 'Classic').save()
Pizza(6, 'Vegetarian', 6, 'Tomato', 'Classic').save()

from Frizza.models import Allergy
Allergy(1, 'Gluten', 'Thick').save()
Allergy(2, 'Dairy', 'Thick').save()
Allergy(3, 'Gluten', 'Thin').save()
Allergy(4, 'Gluten', 'Classic').save()
Allergy(5, 'Dairy', 'Classic').save()
Allergy(6, 'Dairy', 'Alfredo').save()
Allergy(7, 'Dairy', 'Cheese').save()
Allergy(8, 'Soybean', 'Bacon').save()

from Frizza.models import HasTopping
##### 1 #####
HasTopping(pizza_id=cheese_p, topping_name='Cheese').save()
##### 2 #####
HasTopping(2, "Cheese").save()
HasTopping(2, "Pepperoni").save()
##### 3 #####
HasTopping(3, "Cheese").save()
HasTopping(3, "Sausage").save()
##### 4 #####
HasTopping(4, "Cheese").save()
HasTopping(4, "Pineapple").save()
HasTopping(4, "Bacon").save()
##### 5 #####
HasTopping(5, "Cheese").save()
HasTopping(5, "Pepperoni").save()
HasTopping(5, "Sausage").save()
HasTopping(5, "Bacon").save()
HasTopping(5, "Ham").save()
##### 6 #####
HasTopping(6, "Cheese").save()
HasTopping(6, "Mushrooms").save()
HasTopping(6, "Spinach").save()
HasTopping(6, "Green Peppers").save()
HasTopping(6, "Onions").save()
HasTopping(6, "Black Olives").save()

from Frizza.models import User
User(user_name='admin', password='admin').save()

from Frizza.models import Orders
Orders(1, 'admin', 1).save()
Orders(2, 'admin', 2).save()
Orders(3, 'admin', 3).save()
Orders(4, 'admin', 4).save()
Orders(5, 'admin', 5).save()
Orders(6, 'admin', 6).save()
