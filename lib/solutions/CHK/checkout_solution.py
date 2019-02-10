# Applying the discounts
def specialOffers(i,val,discount,items):
	if i == 'A':
		if(val>=5):
			count = 0
			while (val >= 5):
				val = val -5
				count = count + 1
			discount = discount - ( count * 50)
		if(val>=3):
			discount = discount - 20
	elif i == 'B':
		if items['E']>=2 and val!=0:
			aux = items['E']
			while aux >= 2:
				aux = aux -2
				val = val -1
				discount = discount - 30 
		if(val>=2):
			while (val >= 2):
				val = val - 2
				discount = discount - 15
	elif i == 'F':
		if val>=3:
			while val >= 3:
				val = val - 3
				discount = discount - 10
	elif i == 'H':
		if(val>=10):
			count = 0
			while (val >= 10):
				val = val -10
				count = count + 1
			discount = discount - ( count * 20)
		if(val>=5):
			discount = discount - 5
	elif i == 'K':
		if(val>=2):
			while (val >= 2):
				val = val - 2
				discount = discount - 20
	elif i == 'N':
		if(val>=3 and items['M']!=0):
			while (val >= 3 and items['M']!=0 ):
				val = val - 3
				items['M'] = items['M'] - 1
				discount = discount - 15
	elif i == 'P':
		if(val>=5):
			count = 0
			while (val >= 5):
				val = val -5
				count = count + 1
			discount = discount - ( count * 50)
	elif i == 'Q':
		if items['R']>=3 and val!=0:
			aux = items['R']
			while aux >= 3:
				aux = aux - 3
				val = val - 1
				discount = discount - 30 
		if(val>=3):
			while (val >= 3):
				val = val - 3
				discount = discount - 10
	elif i == 'U':
		if val>=4:
			while val >= 4:
				val = val - 4
				discount = discount - 40
	elif i == 'V':
		if(val>=3):
			count = 0
			while (val >= 3):
				val = val -3
				count = count + 1
			discount = discount - ( count * 20)
		if(val>=2):
			discount = discount - 10
	return int(discount)

# Offer discounts when grouping STXYZ products 
def groupProducts(needToPay,items):
	STY = items['S'] + items['T'] + items['Y']
	X = items['X']
	Z = items['Z']
	while (STY + X + Z >= 3):
		if Z >= 3:
			while(Z >= 3):
				Z = Z - 3
				needToPay = needToPay - 18
		if Z == 2 and STY!=0:
			Z = Z - 2
			STY = STY -1 
			needToPay = needToPay - 17
		if Z == 1 and STY>1:
			Z = Z - 1
			STY = STY - 2
			needToPay = needToPay - 16
		if Z == 2 and X!=0:
			Z = Z - 2
			X = X - 1
			needToPay = needToPay - 14
		if Z == 1 and X>1:
			Z = Z - 1
			X = X - 2
			needToPay = needToPay - 10
		if STY >= 3: 
			while STY >=3:
				STY = STY -3
				needToPay = needToPay - 15	
		if STY == 2 and X!=0:
			STY = STY - 2
			X = X - 1
			needToPay = needToPay - 12
		if STY == 1 and X>1:
			STY = STY - 1
			X = X - 2
			needToPay = needToPay - 9
		if X >= 3:
			while(X >= 3):
				X = X - 3
				needToPay = needToPay - 6		
	return int(needToPay)

#Computes the total without applying any discounts
def add(i,val,price):
	total = 0
	total = total + price[i] * val
	return int(total) #returning the total of a specific product

def checkout(skus):
	needToPay = 0 # Initializing the final amout needed to be paid
	# Intitialized the dictionary of the stocks
	items = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}  
	# Intitialized the dictionary of the prices
	price = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10, 'G':20, 'H':10, 'I':35, 'J':60, 'K':70, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 'Q':30, 'R':50, 'S':20, 'T':20, 'U':40, 'V':50, 'W':20, 'X':17, 'Y':20, 'Z':21}  
	for i in skus:
		if(i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
			print(-1)
			return -1
		else:
			items[i]=items[i]+1
	for i in items.keys():
		needToPay = needToPay + add(i,items[i],price)
		needToPay = specialOffers(i,items[i],needToPay,items)
	needToPay = groupProducts(needToPay,items)
	return (needToPay)