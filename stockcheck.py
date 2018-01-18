import main
from time import sleep
with open("watchlist.txt") as f:
    for each in f.readlines():
        sleep(1)#avoid rate limiting
        query = each
        if each[0] == "#":
            continue #Skip commented lines
        main.main(main.vendors,query)