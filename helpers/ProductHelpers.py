from base64 import decodebytes
from helpers.ElementHelpers import getAllLinks
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getProductData(links):
    products=list()
    for link in links:
        driver = webdriver.Chrome()
        try:
            driver.get(link)
            available=len(driver.find_elements_by_class_name("product-not-available"))==0
            name=driver.find_element_by_class_name("pdp__name").text
            desc=driver.find_element_by_class_name("pdp__description").text
            barcode=driver.find_element_by_xpath("/html/body/main/div[4]/div[3]/div/div/div/div[4]/div/table/tbody/tr[3]/td[2]").text
            price=None
            if(available):
                price=driver.find_element_by_class_name("special-price").text
            print({"name":name,"desc":desc,"barcode":barcode,"price":price})
       
        finally:
            driver.close()


def getAllItemLinks(startURL):
    productLinks=set()
    driver = webdriver.Chrome()
    try:
        
        URL=startURL
        driver.get(URL)
        total=int(driver.find_element_by_class_name("total-number-of-results").text.replace(",","").replace("items","").strip())
        itemsPerPage=len(driver.find_elements_by_class_name("item-product__details"))
        numberOfPages=int(total/itemsPerPage)
        print(f"{total} items")
        print(f"{numberOfPages} pages")
        for i in range(1,2+1):
            currentURL=(f"{URL}&page={i}")
            driver.get(currentURL)
            productElements=driver.find_elements_by_class_name("item-product__details")
            productLinks.update(getAllLinks(productElements))
            print(f"Page {i} scraped")
        print(f"{len(productLinks)} links found!")
    except:
        print("Error")
    finally:
        
        driver.close()
        return productLinks
    
