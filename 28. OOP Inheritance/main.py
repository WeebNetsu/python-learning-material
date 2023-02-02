from Chef import Chef
from McDonaldsChef import McDonaldsChef

myChef = Chef(24, 9876)
myChef.make_chicken()

print("\n\tWe got a chef from McDonalds\n")

betterChef = McDonaldsChef(20, 6900, True)
betterChef.make_special_dish()
betterChef.make_burger()