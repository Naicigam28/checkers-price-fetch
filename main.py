from helpers.ProductHelpers import getAllItemLinks, getProductData





URL="https://www.checkers.co.za/c-2256/All-Departments?q=%3Aname-asc%3AbrowseAllStoresFacetOff%3AbrowseAllStoresFacetOff%3AbrowseAllStoresFacet%3AbrowseAllStoresFacet"
#links=getAllItemLinks(URL)
testLinks=["https://www.checkers.co.za/All-Departments/Household/Kitchen/Plasticware/7-In-1-Rainbow-Container-Set/p/10370810EA","https://www.checkers.co.za/All-Departments/Gifts/Flowers-and-Plants/Cut-Flowers-and-Bouquets/Pin-Cushion-Bouquet-Flowers-Bunch/p/10637851EA","https://www.checkers.co.za/All-Departments/Food/Bakery/Bread-and-Rolls/Bread-Rolls/White-Hamburger-Roll/p/10151456EA"]
productData=getProductData(testLinks)
