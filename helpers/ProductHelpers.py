from base64 import decodebytes
from helpers.ElementHelpers import getAllLinks
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def find_element_by_class_name(className, current_driver):
    try:
        element = current_driver.find_element(By.CLASS_NAME, className)

        return element
    except:
        return None


def find_element_by_xpath(xpath, current_driver):
    try:
        element = current_driver.find_element(By.XPATH, xpath)

        return element
    except Exception as e:
        print(e)
        return None


def find_elements_by_class_name(className, current_driver):
    try:
        return current_driver.find_elements(By.CLASS_NAME, className)
    except:
        return None


def getProductData(links):
    products = list()
    for link in links:
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        try:
            driver.get(link)
            time.sleep(15)
            available = (
                len(find_elements_by_class_name("product-not-available", driver)) == 0
            )
            name = find_element_by_class_name("pdp__name", driver).text
            desc = find_element_by_class_name("pdp__description", driver).text

            table_element = driver.find_element(
                By.CLASS_NAME, "pdp__product-information"
            )

            rows = table_element.find_elements(By.TAG_NAME, "tr")

            extracted_data = {}
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                key = cells[0].get_attribute("innerHTML")
                value = cells[1].get_attribute("innerHTML")
                extracted_data[key] = value

            price = None
            if available:
                price = find_element_by_class_name("special-price", driver).text
            product = {
                "name": name,
                "desc": desc,
                "barcode": extracted_data.get("Main Barcode"),
                "brand": extracted_data.get("Product Brand"),
                "price": price,
                "url": link,
            }
            products.append(product)

        finally:
            driver.close()
    return products


def getAllItemLinks(startURL):
    productLinks = set()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    try:
        URL = startURL
        driver.get(URL)
        time.sleep(15)
        total = int(
            find_element_by_class_name("total-number-of-results", driver)
            .text.replace(",", "")
            .replace("items", "")
            .strip()
        )
        itemsPerPage = len(find_elements_by_class_name("item-product__details", driver))
        numberOfPages = int(total / itemsPerPage)
        print(f"{total} items")
        print(f"{numberOfPages} pages")
        for i in range(1, 1 + 1):
            currentURL = f"{URL}&page={i}"
            driver.get(currentURL)
            productElements = find_elements_by_class_name(
                "item-product__details", driver
            )
            productLinks.update(getAllLinks(productElements))
            print(f"Page {i} scraped")
        print(f"{len(productLinks)} links found!")
    except Exception as e:
        print(e)
        print("Error")
    finally:
        driver.close()
    return productLinks
