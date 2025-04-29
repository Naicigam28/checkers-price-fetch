from helpers.ProductHelpers import getAllItemLinks, getProductData
from base64 import decodebytes
from helpers.ElementHelpers import getAllLinks
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from DataBaseHandler import DatabaseHandler



# URL="https://www.checkers.co.za/c-2256/All-Departments?q=%3Aname-asc%3AbrowseAllStoresFacetOff%3AbrowseAllStoresFacetOff%3AbrowseAllStoresFacet%3AbrowseAllStoresFacet"
# links=getAllItemLinks(URL)
testLinks=["https://www.checkers.co.za/All-Departments/Household/Kitchen/Kitchen-Disposables/Checkers-Housebrand-Single-Ply-Serviettes-100-Pack/p/10159231EA"]
product_list=getProductData(testLinks)

db_handler = DatabaseHandler()

for product_data in product_list:
    db_handler.add_product(product_data)

all_products = db_handler.get_all_products()

# Print the retrieved products
for product in all_products:
    print(f"Product: {product.name}, Price: {product.price}, URL: {product.url}")