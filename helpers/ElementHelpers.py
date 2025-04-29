from selenium.webdriver.common.by import By

def getAllLinks(elements):
    links=set()
    for element in elements:
        aTags=element.find_elements(By.TAG_NAME, "a")
        
        for tag in aTags:
            link=tag.get_attribute("href")
            links.add(link)
    #print(f"{len(links)} links found!")
    return links
