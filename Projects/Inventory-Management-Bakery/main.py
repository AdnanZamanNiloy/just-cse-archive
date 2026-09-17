import os
import argparse
from bakery import Inventory, BakerySimulator
from data import INITIAL_INVENTORY, PRODUCTS


def run_demo(days: int, outdir: str = "output"):
    os.makedirs(outdir, exist_ok=True)
    inv = Inventory(INITIAL_INVENTORY)
    sim = BakerySimulator(inv, PRODUCTS, seed=123)

    print(f"\nRunning bakery simulation for {days} days...")
    sim.simulate(days=days, customers_min=8, customers_max=25)

    df = sim.history_to_dataframe()
    csv_path = os.path.join(outdir, f"days.{days}.bakery_simulation_history.csv")
    df.to_csv(csv_path, index=False)
    print(f"History saved to {csv_path}")

    img_path = os.path.join(outdir, f"days.{days}.inventory_trends.png")
    sim.plot_inventory(save_path=img_path)
    print(f"Inventory plot saved to {img_path}")

    # Print a summary
    total_revenue = df["revenue"].sum()
    total_sales_cols = [c for c in df.columns if c.startswith("sales_")]
    total_sales = df[total_sales_cols].sum().to_dict()

    print("\n--- Simulation Summary ---")
    print(f"Total revenue: {total_revenue}")
    for col, val in total_sales.items():
        print(f"{col.replace('sales_', '')}: {val}")
    print("--------------------------")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run bakery simulation")
    parser.add_argument("-d", "--days", type=int, default=None,
                        help="Number of days to simulate (positive integer). If omitted you'll be prompted.")
    args = parser.parse_args()

    default_days = 14
    days = args.days

    # If days not provided on command line, prompt interactively until valid input
    if days is None:
        while True:
            try:
                user = input(f"Enter number of days to simulate [default {default_days}]: ")
                if user.strip() == "":
                    days = default_days
                    break
                days = int(user)
                if days <= 0:
                    print("Please enter a positive integer for days.")
                    continue
                break
            except ValueError:
                print("Invalid input — please enter a positive integer (or press Enter to use the default).")

    # Final safety check
    if not isinstance(days, int) or days <= 0:
        print("Aborting: days must be a positive integer.")
    else:
        run_demo(days=days)
