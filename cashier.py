
cart = []


user_item = input("enter done when finished : ")
while user_item != "done":
	user_price = float(input("price"))
	quantity = int(input("quantity "))
	item={"name": user_item, "price": user_price, "quantity": quantity}
	user_item = input("enter done when finished: ")
	
	cart.append(item)

print(cart)

print("-------")
print("receipt")
print("-------")

total=0.0
for item in cart:
	print("%d %s %f" %(item['quantity'], item['name'], item['price']))
	total +=  (item['price']* item['quantity'])

print("-------")	
print("Total Price: %f" % total)






	