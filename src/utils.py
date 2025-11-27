import json
import os
from src.products import Product
from src.category import Category


def read_json(path: str) -> list[dict]:
    file_json = os.path.abspath(path)
    with open(file_json, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def object_json(data):
    names = []
    for name in data:
        products = []
        for product in name["products"]:
            products.append(Product(**product))
        name["products"] = products
        names.append(Category(**name))
    return names


# if __name__ == '__main__':
#     result = read_json("../data/products.json")
#     prod = object_json(result)
#     print(prod)
#
#     print(prod[1].name)
#     print(prod[1].description)
#     print(prod[1].products)
    # print(prod[1].quantity)
    # read_object_json = object_json(result)
    # print(read_object_json)
