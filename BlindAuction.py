from art import logo
print(logo)
ch="yes"
bid={}
while ch!="no":
    name=input("Enter the name : ").upper()
    price=int(input("Enter the bid amount : "))
    bid[name]=price
    ch=input("Want to add more name ?\nType 'yes' to continue, Type 'no' to stop :\n").lower()
    print("\n"*100)
highes_bid=0
winner=None
for i in bid:
    if bid[i]>highes_bid:
        highes_bid=bid[i]
        winner=i
print(f"The winner is {winner} with the bid amount of {highes_bid}")
