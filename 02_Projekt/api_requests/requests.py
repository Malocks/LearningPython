"""
This Code makes RESTful calls,
it get an JSON data back.
"""
import json
from pip._vendor import requests
from main import get_user_input

BASE_URL = "https://dummyjson.com/products/"
PRODUCT_ID = get_user_input()


def get_all_products():
    """
    This module makes an GET call for all Products,
    it gives back a JSON-list of ohjects.
    """

    response = requests.get(BASE_URL)

    if response.status_code == 200:
        data = response.json()
        return data

    print("Error: ", response.status_code)
    return None


results_all_products = get_all_products()

if results_all_products is not None:
    all_products = json.dumps(results_all_products, indent=4)
    #print("ALL PRODUCTS:   " + all_products)


def get_single_product():
    """
    This module makes and GET call for a single product,
    it gives back a JSON-Object of a single product.
    """
    response = requests.get(BASE_URL + PRODUCT_ID)

    if response.status_code == 200:
        data = response.json()
        return data

    print("Error: ", response.status_code)
    return None


results_single_product = get_single_product()

if results_single_product is not None:
    single_product = json.dumps(results_single_product, indent=4)
    print("Single PRODUCT:   " + single_product)
