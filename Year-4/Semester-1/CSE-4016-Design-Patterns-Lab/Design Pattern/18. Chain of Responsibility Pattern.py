"""The Chain of Responsibility Pattern is a behavioral design pattern where a request is passed through a 
chain of objects until one of them handles it.Instead of one object knowing exactly who should process the 
request, the request travels through a chain."""

from abc import ABC, abstractmethod


# ==========================
# Purchase
# ==========================

class clsPurchase:

    def __init__(self, number, amount, purpose):
        self.number = number
        self.amount = amount
        self.purpose = purpose


# ==========================
# Approver Base Class
# ==========================

class clsApprover(ABC):

    def __init__(self):
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor

    @abstractmethod
    def process_request(self, purchase):
        pass


# ==========================
# Chairman
# ==========================

class clsChairman(clsApprover):

    def process_request(self, purchase):

        if purchase.amount <= 25000.0:

            print(f"Chairman approves Purchase "f"{purchase.number}")

        elif self.successor is not None:

            self.successor.process_request(purchase)


# ==========================
# Treasurer
# ==========================

class clsTreasurer(clsApprover):

    def process_request(self, purchase):

        if purchase.amount <= 500000.0:

            print(f"Treasurer approves Purchase "f"{purchase.number}")

        elif self.successor is not None:

            self.successor.process_request(purchase)


# ==========================
# Vice Chancellor
# ==========================

class clsViceChancellor(clsApprover):

    def process_request(self, purchase):

        if purchase.amount <= 1000000.0:

            print(f"Vice Chancellor approves "f"Purchase {purchase.number}")

        else:

            print(f"Purchase {purchase.number} "f"requires Regent Board Meeting.")


# ==========================
# Main
# ==========================

def main():

    # Setup Chain of Responsibility

    chairman = clsChairman()

    treasurer = clsTreasurer()

    vice_chancellor = clsViceChancellor()

    chairman.set_successor(treasurer)

    treasurer.set_successor(vice_chancellor)

    # Process Purchases

    purchase = clsPurchase(
        777,
        350000.00,
        "Research"
    )

    chairman.process_request(purchase)

    purchase = clsPurchase(
        888,
        800000.00,
        "Construction"
    )

    chairman.process_request(purchase)

    purchase = clsPurchase(
        999,
        3060000000.00,
        "ADB Project"
    )

    chairman.process_request(purchase)


if __name__ == "__main__":
    main()