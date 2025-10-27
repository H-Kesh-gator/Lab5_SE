import json
# remove unusable import logging
from datetime import datetime


# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Adds a specified quantity of an item to the stock.

    Args:
        item (str): The name of the item to add.
        qty (int): The quantity to add.
        logs (list, optional): A list to record logs of actions.
            Defaults to None.
    """
    if logs is None:
        logs = []
    if not item:
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Removes a specified quantity of an item from the stock.

    Args:
        item (str): The name of the item to remove.
        qty (int): The quantity to remove.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock_data.")


def get_qty(item):
    """
    Returns the quantity available for a specified item.

    Args:
        item (str): The name of the item to check.

    Returns:
        int: The quantity of the item in stock.
    """
    return stock_data[item]


def load_data(file="inventory.json"):
    """
    Loads stock data from a JSON file.

    Args:
        file (str): The filename to load data from.
            Defaults to 'inventory.json'.
    """
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.load(f)


def save_data(file="inventory.json"):
    """
    Saves current stock data to a JSON file.

    Args:
        file (str): The filename to save data to.
            Defaults to 'inventory.json'.
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """
    Prints a report of all items and their quantities.
    """
    print("Items Report")
    for i, qty in stock_data.items():
        print(f"{i} -> {qty}")


def check_low_items(threshold=5):
    """
    Returns a list of items with quantities below a given threshold.

    Args:
        threshold (int): The minimum quantity to consider sufficient.
            Defaults to 5.

    Returns:
        list: A list of items with quantities below the threshold.
    """
    result = []
    for i, qty in stock_data.items():
        if qty < threshold:
            result.append(i)
    return result


def main():
    """
    Demonstrates the use of inventory functions by adding, removing,
    checking, and saving stock data.
    """
    add_item("apple", 10)
    add_item("banana", -2)
    # add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()

