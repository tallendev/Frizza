from django.db import models


# This is a table representation for Sauces types, containing two fields:
# a name for the sauce and
# a calorie count
class Sauce(models.Model):
    sauce_name = models.CharField(max_length=20, primary_key=True)
    calorie = models.IntegerField()

    def __unicode__(self):
        return self.sauce_name


# This is a table representation for Crust types, containing two fields:
# a name for the crust and
# a calorie count
class Crust(models.Model):
    crust_name = models.CharField(max_length=20, primary_key=True)
    calorie = models.IntegerField()

    def __unicode__(self):
        return self.crust_name


# This is a table representation for Pizza types, containing four fields:
# a name for the pizza, which will be specified per user
# the user count
# the name of the sauce on the pizza
# the name of the crust on the pizza
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=20)
    order_count = models.IntegerField()
    sauce_name = models.ForeignKey(Sauce)
    crust_name = models.ForeignKey(Crust)

    # to string returns pizza name
    def __unicode__(self):
        return self.pizza_name


# This is a table representation for topping types, containing two fields:
# a name for the topping
# a calorie count
class Topping(models.Model):
    topping_name = models.CharField(max_length=20, primary_key=True)
    calorie = models.IntegerField()
   
     # to string returning topping name
    def __unicode__(self):
        return self.topping_name


# Table for a user, containing: 
# their user name
# the password
class User(models.Model):
    user_name = models.CharField(max_length=20, primary_key=True)
    #email = models.EmailField(max_length=100)
    password = models.CharField(max_length=30)

    # returns the user name as a to string
    def __unicode__(self):
        return self.user_name


# Relationship for toppings on pizzas, containing two fields:
# the pizza name
# a topping on the pizza. 
#
# Weird behavior due to no composite primary keys.
class HasTopping(models.Model):
    pizza_name = models.ForeignKey(Pizza)
    topping_name = models.ForeignKey(Topping)
    
    # returns ids
    def __unicode__(self):
        return str(self.id)


# A table for orders, containing:
# the user name of the person with the order
# name of the pizza that they ordered
class Orders(models.Model):
    user_name = models.ForeignKey(User)
    pizza_id = models.ForeignKey(Pizza)

    def __unicode__(self):
        return str(self.id)


# A table of allergies, containing:
# the name of the allergy
# the name of the ingredient
class Allergy(models.Model):
    allergy_name = models.CharField(max_length=20)
    ingredient_name = models.CharField(max_length=20)

    def __unicode__(self):
        return str(self.id)