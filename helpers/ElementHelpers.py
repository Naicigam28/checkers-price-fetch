def getAllLinks(elements):
    links=set()
    for element in elements:
        aTags=element.find_elements_by_tag_name("a")
        
        for tag in aTags:
            link=tag.get_attribute("href")
            links.add(link)
    #print(f"{len(links)} links found!")
    return links
