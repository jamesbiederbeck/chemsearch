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
        endpoint = "/Pages/GeneratePdf.aspx?Name=Cofa&Lot=",
        urlsuffix = "",
        spacechar = "%20",
        favorite = True
        )

pcca = vendor(
        name = "PCCA",
        domain ="https://members.pccarx.com",
        endpoint = "/Documents/1000CofA_pdf/",
        urlsuffix = ".pdf",
        spacechar = "",
        favorite = True
        )
        

def main(vendors, query = ""):
    print("Welcome to C of A Search-5000!")
    print("This is a program by James to search for C of A's")
    print("Here are the current vendors supported:")
    for each in vendors:
        print(each.name)
    print()
    print("If you want to seach a particular vendor, just type your search,")
    print("and then @vendorname. Eg to search PCCA for thyroid, you would type")
    print("thyroid@pcca")
    print()
    
    while not query:
        query = input("What chemcial are you looking for?\n>")
        query=query.lower()#Because case doesn't matter, and the @ notation
                           #makes it easy to hold down shift.
    print(query)
    if "!" in query:
        mckesson.search(query.replace("!",""))
    if "/" in query:
        medisca.search(query)
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


