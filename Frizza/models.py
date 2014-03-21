from django.db import models

class Sauce(models.Model):
    sauce_name = models.CharField(max_length=20, primary_key=True)
    calorie = models.IntegerField()

    def __unicode__(self):
        return self.sauce_name

class Crust(models.Model):
    crust_name = models.CharField(max_length=20, primary_key=True)
    calorie = models.IntegerField()

    def __unicode__(self):
         return self.crust_name

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=20, primary_key=True)
    order_count = models.IntegerField()
    sauce_name = models.ForeignKey(Sauce)
    crust_name = models.ForeignKey(Crust)

    def __unicode__(self):
        return self.pizza_name

class Topping(models.Model):
    topping_name = models.CharField(max_length=20, primary_key=True)
    calorie = models.IntegerField()

    def __unicode__(self):
        return self.topping_name

class User(models.Model):
    user_name = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user_name

class HasTopping(models.Model):
    pizza_name = models.ForeignKey(Pizza)
    topping_name = models.ForeignKey(Topping)

    def __unicode__(self):
        return str(self.id)

class Orders(models.Model):
    user_name = models.ForeignKey(User)
    pizza_name = models.ForeignKey(Pizza)

    def __unicode__(self):
        return str(self.id)

class Allergy(models.Model):
    allergy_name = models.CharField(max_length=20)
    ingredient_name = models.CharField(max_length=20)

    def __unicode__(self):
        return str(self.id)
