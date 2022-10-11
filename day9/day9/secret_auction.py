print("Secret Auction Program")

list_of_auctions = []


def get_bid():
    bids = {}
    name = input("What is your name? : ")
    price = float(input("What is your bid? : $"))
    bids[name] = price
    list_of_auctions.append(bids)


def get_max(bids):
    highest_bid = 0
    name = None
    for x in range(0, len(bids)):
        for y in bids[x]:
            if bids[x][y] > highest_bid:
                highest_bid = bids[x][y]
                name = y
    print(f"{name} has the highest price : {highest_bid}")

'''
def show_list_of_auctions():
    for x in range(0, len(list_of_auctions)):
        for y in list_of_auctions[x]:
            print(f"{y} : {list_of_auctions[x][y]}")
'''

#get_bid()
#get_bid()

#show_list_of_auctions()
# get_max(list_of_auctions)


more = True

while more:
    get_bid()
    cont = input("Other bidder? Type 'yes' if yes, 'no' if no : ")
    if cont == "yes":
        more = True
    else:
        get_max(list_of_auctions)
        more = False

