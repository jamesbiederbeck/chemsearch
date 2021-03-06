#chemsearch.py
#A script by James Biederbeck to automate searching chemical sites
#Just run, type in your search, and watch the magic happen.
from selenium import webdriver
import time
import atexit

driver = webdriver.Chrome()
atexit.register(driver.quit)
class vendor():
    def __init__(self,name,domain,endpoint,urlsuffix,spacechar,favorite,**kwargs):
        self.name = name
        self.domain = domain
        self.endpoint = endpoint
        self.urlsuffix = urlsuffix
        self.spacechar = spacechar
        self.favorite = favorite
        self.pages = {}
        if "pages" in kwargs:
            self.pages = kwargs["pages"]
        self.replacementdictionary = {}
        if "replacementdictionary" in kwargs:
            self.replacementdictionary = kwargs["replacementdictionary"]
        vendors.append(self)
        
    def search(self,string):
        if len(self.pages.keys()):
            for page in self.pages.keys():
                if string in page:
                    driver.get(self.pages[page])
                    return
        #this url will get opened in the default browser at the end of this
        #function.
        url = ""
        url += self.domain
        url += self.endpoint
        searchstring = string.replace(" ", self.spacechar)
        url += searchstring #no self because this is a function variable
        url += self.urlsuffix
        driver.get(url)
        
vendors = [] #a list of all our vendors        
        
medisca = vendor(
        name = "Medisca",
        domain ="https://www.medisca.com",
        endpoint = "/Pages/ProductSearch.aspx?Search=",
        urlsuffix = "",
        spacechar = "%20",
        favorite = True,
        pages = {"order history":"https://www.medisca.com/my-orders",
                 "awp":"file:///C:/Users/technician/Downloads/AWP%20(2).pdf"
                }
        )

amazon = vendor(
        name = "Amazon",
        domain ="https://www.amazon.com",
        endpoint = "/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=",
        urlsuffix = "",
        spacechar = "+",
        favorite = False,
        pages = {"order history":"https://www.amazon.com/gp/css/order-history/ref=nav_youraccount_bnav_ya_ad_orders"
            }
        )


healthcarelogistics = vendor(
        name = "Health Care Logistics",
        domain ="https://search.gohcl.com",
        endpoint = "/results/",
        urlsuffix = "",
        spacechar = "%20",
        favorite = False
        )

sks = vendor(
        name = "SKS",
        domain ="https://www.sks-bottle.com",
        endpoint = "/search_result.php?keywords=",
        urlsuffix = "",
        spacechar = "+",
        favorite = False
        )

mckesson = vendor(
        name = "McKesson",
        domain = "https://connect.mckesson.com",
        endpoint = "/portal/site/smo/menuitem.87a0666be7398a3ece3ee6105740d0a0/?query=",
        urlsuffix = "",
        spacechar = "+",
        favorite = False,
        pages = {
            "order history":"https://orderzone2.mckesson.com/SMOnline/odr_lst_opn.jsp"
            }
        )        

letco = vendor(
        name = "Letco",
        domain ="https://www.letcomedical.com",
        endpoint = "/shop/item/get-list/type/search?term=",
        urlsuffix = "",
        spacechar = "+",
        favorite = True,
        pages = {
            "cofa":"https://www.letcomedical.com/shop/certificate-of-analysis",
            "awp":"https://www.letcomedical.com/shop/file/get-awp",
            "order history":"https://www.letcomedical.com/shop/order/get-list"

            }
        )

fagron = vendor(
        name = "Fagron",
        domain ="https://shop.fagron.us",
        endpoint = "/en-us/search.aspx?q=",
        urlsuffix = "&s_c=products",
        spacechar = "+",
        favorite = True,
        pages = {"order history":"https://shop.fagron.us/en-us/profile/orderhistory.aspx?bind=1",
                 "awp":"file:///C:/Users/technician/Downloads/AWP%20List%20PDF%2011-11-16.pdf"
                 }
        )

totalPharmacySupply = vendor(
        name = "Total Pharmacy Supply",
        domain = "http://www.totalpharmacysupply.com",
        endpoint = "/catalogsearch/result/?q=",
        urlsuffix = "",
        spacechar = "+",
        favorite = False
        )

pcca = vendor(
        name = "PCCA",
        domain = "https://members.pccarx.com",
        endpoint = "/Products/ProductCatalog.aspx?search=",
        urlsuffix = "",
        spacechar = "+",
        favorite = False,
        pages = {
            "order history":"https://members.pccarx.com/Account/OrderHistory.aspx"
        }
        )

spectrum = vendor(
        name = "Spectrum",
        domain = "https://www.spectrumrx.com",
        endpoint = "/search/go?w=",
        urlsuffix = "",
        spacechar = "+",
        favorite = True,
        pages = {
            "order history":"https://www.spectrumrx.com/OA_HTML/xxsc_ibeCZzpGetTemplateFile.jsp?tmp=STORE_PSI_ORDER_SUMMARY_P",
            "awp":"https://www.spectrumrx.com/OA_HTML/LAB_DOCS/master_ndc_awp.pdf"
        }
        )

emerson = vendor(
        name = "Emerson",
        domain = "https://www.emersonecologics.com",
        endpoint = "/shop/search?fft=term&term=",
        urlsuffix = "",
        spacechar = "%20",
        favorite = False
        )
        
biolmerieux = vendor(
        name = "Biomerieux",
        domain = "https://biomerieuxdirect.com",
        endpoint = "/industry/search?text=",
        urlsuffix = "",
        spacechar = "+",
        favorite = False
        )

msdonline = vendor(
    name = "msd",
    domain = "https://www.msdonline.com",
    endpoint = "/Search?categoryId=All+Products&criteria=",
    urlsuffix = "",
    spacechar = "+",
    favorite = False
    )





def main(vendors, query = ""):
    print("Welcome to Jamesbot5000!")
    print("This is a program by James to search for chemicals")
    print("Here are the current vendors supported:")
    for each in vendors:
        print(each.name)
        if len(each.pages):
            print("    Supports: ",list(each.pages.keys()), sep = '\n')
    print()
    print("If you want to seach a particular vendor, just type your search,")
    print("and then @vendorname. Eg to search PCCA for thyroid, you would type")
    print("thyroid@pcca")
    print()
    
    while not query:
        query = input("What chemical are you looking for?\n>")
        query=query.lower()#Because case doesn't matter, and the @ notation
                           #makes it easy to hold down shift.
    print(query)
    if "!" in query:
        mckesson.search(query.replace("!",""))
    elif "@" in query:
        if "all" in query.split("@")[1]:
            for each in vendors:
                each.search(query.split("@")[0])
        else:
            for each in vendors:
                if each.name.lower().startswith(query.split("@")[1]):
                    each.search(query.split("@")[0])
    elif query.lower() == "history":
        print("Loading order history")
        for each in vendors:
            if len(each.pages.keys()):
                each.search(query)
    else:
        for each in vendors:
            if each.favorite:
                each.search(query)

if __name__ == "__main__":
    main(vendors)


