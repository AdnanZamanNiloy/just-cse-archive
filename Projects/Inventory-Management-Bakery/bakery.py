# bakery.py
import random
import copy
from typing import Dict, List
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from data import PRODUCTS, INITIAL_INVENTORY

class Inventory:
    def __init__(self, stocks: Dict[str, int]):
        self.stocks = copy.deepcopy(stocks)

    def can_make(self, product_name: str) -> bool:
        recipe = PRODUCTS[product_name]["ingredients"]
        for ing, amt in recipe.items():
            if self.stocks.get(ing, 0) < amt:
                return False
        return True

    def consume(self, product_name: str):
        recipe = PRODUCTS[product_name]["ingredients"]
        for ing, amt in recipe.items():
            self.stocks[ing] -= amt
            if self.stocks[ing] < 0:
                self.stocks[ing] = 0  # Safety check


    #Restock ingredients if below threshold
    def restock_if_needed(self, threshold: int = 500, restock_amount: int = 2000) -> List[str]:
        restocked = []
        for ing, qty in self.stocks.items():
            if qty < threshold:
                self.stocks[ing] += restock_amount
                restocked.append(ing)
        return restocked

    def snapshot(self) -> Dict[str, int]:
        return copy.deepcopy(self.stocks)

class BakerySimulator:
    def __init__(
        self,
        inventory: Inventory,
        products: Dict[str, Dict],
        seed: int | None = 42
    ):
        self.inventory = inventory
        self.products = products
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
        # History for plotting and CSV export
        self.history = []  # list of dicts each day

    def simulate_day(self, day: int, customers_min: int = 5, customers_max: int = 20):
        day_record = {
            "day": day,
            "sales": {p: 0 for p in self.products},
            "revenue": 0.0,
            "restocked": [],
            "inventory": {}
        }

        customers = random.randint(customers_min, customers_max)
        for _ in range(customers):
            item = random.choice(list(self.products.keys()))
            if self.inventory.can_make(item):
                self.inventory.consume(item)
                day_record["sales"][item] += 1
                day_record["revenue"] += self.products[item]["price"]
            else:
                # Could log shortages here if desired
                pass

        # Restock step at end of day
        restocked = self.inventory.restock_if_needed()
        day_record["restocked"] = restocked
        day_record["inventory"] = self.inventory.snapshot()
        self.history.append(day_record)
        return day_record

    def simulate(self, days: int = 7, customers_min: int = 5, customers_max: int = 20):
        for d in range(1, days + 1):
            rec = self.simulate_day(d, customers_min, customers_max)
        return self.history

    def history_to_dataframe(self) -> pd.DataFrame:
        """
        Convert history into a DataFrame suitable for CSV export and plotting.
        Inventory columns will be expanded so each ingredient has its own column.
        """
        rows = []
        for dayrec in self.history:
            base = {"day": dayrec["day"], "revenue": dayrec["revenue"]}
            # flatten sales
            for p, cnt in dayrec["sales"].items():
                base[f"sales_{p}"] = cnt
            # add inventory snapshot
            for ing, qty in dayrec["inventory"].items():
                base[f"inv_{ing}"] = qty
            # restocked as comma string
            base["restocked"] = ",".join(dayrec["restocked"]) if dayrec["restocked"] else ""
            rows.append(base)
        df = pd.DataFrame(rows)
        return df

    def plot_inventory(self, save_path: str = "inventory_trends.png"):
        df = self.history_to_dataframe()
        inv_cols = [c for c in df.columns if c.startswith("inv_")]
        if df.empty:
            print("No history to plot.")
            return
        plt.figure(figsize=(10, 6))
        for col in inv_cols:
            plt.plot(df["day"], df[col], label=col.replace("inv_", ""))
        plt.xlabel("Day")
        plt.ylabel("Quantity")
        plt.title("Inventory Levels Over Time")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        return save_path
