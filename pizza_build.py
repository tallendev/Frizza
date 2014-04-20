#import Frizza.settings
#settings.configure()
from Frizza.models import Sauce
Sauce('Tomato', 100).save()
Sauce('Alfredo', 100).save()
Sauce('Olive Oil', 100).save()
from Frizza.models import Crust
Crust('Thick', 100).save()
Crust('Thin', 100).save()
Crust('Classic', 100).save()
from Frizza.models import Topping
Topping('Pepperoni', 100).save()
Topping('Olives', 100).save()
from Frizza.models import Pizza
Pizza(1, 'Pepperoni', 1, 'Alfredo', 'Thin').save()
Pizza(2, 'Cheese', 1, 'Alfredo', 'Thin').save()
from Frizza.models import HasTopping

