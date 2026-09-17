""" The Decorator Pattern is a structural design pattern that allows you to add new functionality
 to an object dynamically without modifying its existing code."""
 
from abc import ABC, abstractmethod


# ==========================
# Base Pizza
# ==========================

class clsBasePizza(ABC):

    def __init__(self):
        self.nBasePrice = 0.0

    def get_price(self):
        return self.nBasePrice


# ==========================
# Concrete Pizzas
# ==========================

class clsGourmet(clsBasePizza):

    def __init__(self):
        super().__init__()
        self.nBasePrice = 7.99


class clsMargherita(clsBasePizza):

    def __init__(self):
        super().__init__()
        self.nBasePrice = 6.99


# ==========================
# Topping Decorator
# ==========================

class clsTopping(clsBasePizza):

    def __init__(self, oPizzaToDecorate):
        super().__init__()
        self.oPizza = oPizzaToDecorate

    def get_price(self):
        return self.oPizza.get_price() + self.nBasePrice


# ==========================
# Concrete Toppings
# ==========================

class clsExtraCheese(clsTopping):

    def __init__(self, oPizzaToDecorate):
        super().__init__(oPizzaToDecorate)
        self.nBasePrice = 0.99


class clsMushroom(clsTopping):

    def __init__(self, oPizzaToDecorate):
        super().__init__(oPizzaToDecorate)
        self.nBasePrice = 0.79


class clsJalapeno(clsTopping):

    def __init__(self, oPizzaToDecorate):
        super().__init__(oPizzaToDecorate)
        self.nBasePrice = 0.49


class clsExtraMeat(clsTopping):

    def __init__(self, oPizzaToDecorate):
        super().__init__(oPizzaToDecorate)
        self.nBasePrice = 1.99


class clsExtraShrimp(clsTopping):

    def __init__(self, oPizzaToDecorate):
        super().__init__(oPizzaToDecorate)
        self.nBasePrice = 2.99


# ==========================
# Main
# ==========================

def main():

    # Margherita Pizza
    oMPizza = clsMargherita()
    print(f"Plain Margherita Pizza: {oMPizza.get_price():.2f}")

    oMPizzaWithEC1 = clsExtraCheese(oMPizza)
    print(f"Margherita Pizza with Extra Cheese: {oMPizzaWithEC1.get_price():.2f}")

    oMPizzaWithEC2 = clsExtraCheese(oMPizzaWithEC1)
    print(f"Margherita Pizza with Double Extra Cheese: {oMPizzaWithEC2.get_price():.2f}")

    oMPizzaWithEC2M = clsMushroom(oMPizzaWithEC2)
    print(
        f"Margherita Pizza with Double Extra Cheese and Mushroom: "
        f"{oMPizzaWithEC2M.get_price():.2f}"
    )

    oMPizzaWithEC2MJ = clsJalapeno(oMPizzaWithEC2M)
    print(
        f"Margherita Pizza with Double Extra Cheese, Mushroom and Jalapeno: "
        f"{oMPizzaWithEC2MJ.get_price():.2f}"
    )

    oMPizzaWithEC2MJEM = clsExtraMeat(oMPizzaWithEC2MJ)
    print(
        f"Margherita Pizza with Double Extra Cheese, Mushroom, Jalapeno "
        f"and Extra Meat: {oMPizzaWithEC2MJEM.get_price():.2f}"
    )

    oMPizzaWithEC2MJEMES = clsExtraShrimp(oMPizzaWithEC2MJEM)
    print(
        f"Margherita Pizza with Double Extra Cheese, Mushroom, Jalapeno, "
        f"Extra Meat and Extra Shrimp: "
        f"{oMPizzaWithEC2MJEMES.get_price():.2f}"
    )

    print()

    # Gourmet Pizza
    oGPizza = clsGourmet()
    print(f"Plain Gourmet Pizza: {oGPizza.get_price():.2f}")

    oGPizzaWithEC1 = clsExtraCheese(oGPizza)
    print(f"Gourmet Pizza with Extra Cheese: {oGPizzaWithEC1.get_price():.2f}")

    oGPizzaWithEC2 = clsExtraCheese(oGPizzaWithEC1)
    print(f"Gourmet Pizza with Double Extra Cheese: {oGPizzaWithEC2.get_price():.2f}")

    oGPizzaWithEC2M = clsMushroom(oGPizzaWithEC2)
    print(
        f"Gourmet Pizza with Double Extra Cheese and Mushroom: "
        f"{oGPizzaWithEC2M.get_price():.2f}"
    )

    oGPizzaWithEC2MJ = clsJalapeno(oGPizzaWithEC2M)
    print(
        f"Gourmet Pizza with Double Extra Cheese, Mushroom and Jalapeno: "
        f"{oGPizzaWithEC2MJ.get_price():.2f}"
    )

    oGPizzaWithEC2MJEM = clsExtraMeat(oGPizzaWithEC2MJ)
    print(
        f"Gourmet Pizza with Double Extra Cheese, Mushroom, Jalapeno "
        f"and Extra Meat: {oGPizzaWithEC2MJEM.get_price():.2f}"
    )

    oGPizzaWithEC2MJEMES = clsExtraShrimp(oGPizzaWithEC2MJEM)
    print(
        f"Gourmet Pizza with Double Extra Cheese, Mushroom, Jalapeno, "
        f"Extra Meat and Extra Shrimp: "
        f"{oGPizzaWithEC2MJEMES.get_price():.2f}"
    )


if __name__ == "__main__":
    main()