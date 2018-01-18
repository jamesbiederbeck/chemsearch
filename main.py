#chemsearch.py
#A script by James Biederbeck to automate searching chemical sites
#Just run, type in your search, and watch the magic happen.
import webbrowser

class vendor():
    def __init__(self,name,domain,endpoint,urlsuffix,spacechar,favorite):
        self.name = name
        self.domain = domain
        self.endpoint = endpoint
        self.urlsuffix = urlsuffix
        self.spacechar = spacechar
        self.favorite = favorite
        vendors.append(self)
        
    def search(self,string):
        #this url will get opened in the default browser at the end of this
        #function.
        url = ""
        url += self.domain
        url += self.endpoint
        searchstring = string.replace(" ", self.spacechar)
        url += searchstring #no self because this is a function variable
        url += self.urlsuffix
        #new = 2 opens the search results in a new tab, and autoraise gives the 
        #browser focus. 
        webbrowser.open(url, new = 2, autoraise = True)

vendors = [] #a list of all our vendors        
        
medisca = vendor(
        name = "Medisca",
        domain ="https://www.medisca.com",
        endpoint = "/Pages/ProductSearch.aspx?Search=",
        urlsuffix = "",
        spacechar = "%20",
        favorite = True
        )

mckesson = vendor(
        name = "McKesson",
        domain = "https://connect.mckesson.com",
        endpoint = "/portal/site/smo/menuitem.87a0666be7398a3ece3ee6105740d0a0/?query=",
        urlsuffix = "",
        spacechar = "+",
        favorite = False
        )        

letco = vendor(
        name = "Letco",
        domain ="https://www.letcomedical.com",
        endpoint = "/shop/item/get-list/type/search?term=",
        urlsuffix = "",
        spacechar = "+",
        favorite = True
        )

fagron = vendor(
        name = "Fagron",
        domain ="https://shop.fagron.us",
        endpoint = "/en-us/search.aspx?q=",
        urlsuffix = "&s_c=products",
        spacechar = "+",
        favorite = True
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
        favorite = False
        )

spectrum = vendor(
        name = "Spectrum",
        domain = "https://www.spectrumrx.com",
        endpoint = "/search/go?w=",
        urlsuffix = "",
        spacechar = "+",
        favorite = True
        )

emerson = vendor(
        name = "Emerson",
        domain = "https://www.emersonecologics.com",
        endpoint = "/shop/",
        urlsuffix = "",
        spacechar = "%20",
        favorite = False
        )
        

def main(vendors, query = ""):
    print("Welcome to Jamesbot5000!")
    print("This is a program by James to search for chemicals")
    print("Here are the current vendors supported:")
    for each in vendors:
        print(each.name)
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
    else:
        for each in vendors:
            if each.favorite:
                each.search(query)

if __name__ == "__main__":
    main(vendors)


