from abc import ABC


# ==========================
# Base Pizza
# ==========================

class clsBasePizza(ABC):

    def __init__(self):
        self.base_price_pizza = 0.0

    def get_price(self):
        return self.base_price_pizza


class clsMargherita(clsBasePizza):

    def __init__(self):
        super().__init__()
        self.base_price_pizza = 6.99


class clsGourmet(clsBasePizza):

    def __init__(self):
        super().__init__()
        self.base_price_pizza = 7.99


# ==========================
# Toppings (Decorator Pattern)
# ==========================

class clsTopping(clsBasePizza):

    def __init__(self, pizza_to_decorate):
        super().__init__()

        self.pizza = pizza_to_decorate
        self.base_price_topping = 0.0

    def get_price(self):
        return (
            self.pizza.get_price()
            + self.base_price_topping
        )


class clsExtraCheese(clsTopping):

    def __init__(self, pizza_to_decorate):
        super().__init__(pizza_to_decorate)

        self.base_price_topping = 0.99


class clsMushroom(clsTopping):

    def __init__(self, pizza_to_decorate):
        super().__init__(pizza_to_decorate)

        self.base_price_topping = 0.79


class clsJalapeno(clsTopping):

    def __init__(self, pizza_to_decorate):
        super().__init__(pizza_to_decorate)

        self.base_price_topping = 0.49


class clsExtraMeat(clsTopping):

    def __init__(self, pizza_to_decorate):
        super().__init__(pizza_to_decorate)

        self.base_price_topping = 1.99


class clsExtraShrimp(clsTopping):

    def __init__(self, pizza_to_decorate):
        super().__init__(pizza_to_decorate)

        self.base_price_topping = 2.99


# ==========================
# Main
# ==========================

def main():

    # --------------------------
    # Margherita Pizza
    # --------------------------

    m_pizza = clsMargherita()

    print(
        f"Plain Margherita Pizza: "
        f"{m_pizza.get_price():.2f}"
    )

    m_pizza_ec1 = clsExtraCheese(m_pizza)

    print(
        f"Margherita Pizza with Extra Cheese: "
        f"{m_pizza_ec1.get_price():.2f}"
    )

    m_pizza_ec2 = clsExtraCheese(m_pizza_ec1)

    print(
        f"Margherita Pizza with Double Extra Cheese: "
        f"{m_pizza_ec2.get_price():.2f}"
    )

    m_pizza_ec2m = clsMushroom(m_pizza_ec2)

    print(
        f"Margherita Pizza with Double Extra Cheese "
        f"and Mushroom: "
        f"{m_pizza_ec2m.get_price():.2f}"
    )

    m_pizza_ec2mj = clsJalapeno(m_pizza_ec2m)

    print(
        f"Margherita Pizza with Double Extra Cheese, "
        f"Mushroom and Jalapeno: "
        f"{m_pizza_ec2mj.get_price():.2f}"
    )

    m_pizza_ec2mjem = clsExtraMeat(m_pizza_ec2mj)

    print(
        f"Margherita Pizza with Double Extra Cheese, "
        f"Mushroom, Jalapeno and Extra Meat: "
        f"{m_pizza_ec2mjem.get_price():.2f}"
    )

    m_pizza_ec2mjemes = clsExtraShrimp(
        m_pizza_ec2mjem
    )

    print(
        f"Margherita Pizza with Double Extra Cheese, "
        f"Mushroom, Jalapeno, Extra Meat and "
        f"Extra Shrimp: "
        f"{m_pizza_ec2mjemes.get_price():.2f}"
    )

    print("\n" + "=" * 60 + "\n")

    # --------------------------
    # Gourmet Pizza
    # --------------------------

    g_pizza = clsGourmet()

    print(
        f"Plain Gourmet Pizza: "
        f"{g_pizza.get_price():.2f}"
    )

    g_pizza_ec1 = clsExtraCheese(g_pizza)

    print(
        f"Gourmet Pizza with Extra Cheese: "
        f"{g_pizza_ec1.get_price():.2f}"
    )

    g_pizza_ec2 = clsExtraCheese(g_pizza_ec1)

    print(
        f"Gourmet Pizza with Double Extra Cheese: "
        f"{g_pizza_ec2.get_price():.2f}"
    )

    g_pizza_ec2m = clsMushroom(g_pizza_ec2)

    print(
        f"Gourmet Pizza with Double Extra Cheese "
        f"and Mushroom: "
        f"{g_pizza_ec2m.get_price():.2f}"
    )

    g_pizza_ec2mj = clsJalapeno(g_pizza_ec2m)

    print(
        f"Gourmet Pizza with Double Extra Cheese, "
        f"Mushroom and Jalapeno: "
        f"{g_pizza_ec2mj.get_price():.2f}"
    )

    g_pizza_ec2mjem = clsExtraMeat(g_pizza_ec2mj)

    print(
        f"Gourmet Pizza with Double Extra Cheese, "
        f"Mushroom, Jalapeno and Extra Meat: "
        f"{g_pizza_ec2mjem.get_price():.2f}"
    )

    g_pizza_ec2mjemes = clsExtraShrimp(
        g_pizza_ec2mjem
    )

    print(
        f"Gourmet Pizza with Double Extra Cheese, "
        f"Mushroom, Jalapeno, Extra Meat and "
        f"Extra Shrimp: "
        f"{g_pizza_ec2mjemes.get_price():.2f}"
    )


if __name__ == "__main__":
    main()