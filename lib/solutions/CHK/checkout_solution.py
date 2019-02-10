items = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0} # Intitialized the dictionary of the stocks

#Applying the discounts
def specialOffers(i,val,discount):
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
	return int(discount)

#Computes the total without applying any discounts
def add(i,val):
	total = 0
	if i == 'A':
		total = total + 50 * val
	elif i == 'B':
		total = total + 30 * val
	elif i == 'C':
		total = total + 20 * val
	elif i == 'D':
		total = total + 15 * val
	elif i == 'E':
		total = total + 40 * val
	return int(total) #returning the total of a specific product

def checkout(skus):
	needToPay =0 # Initializing the final amout needed to be paid
	
	for i in skus:
		if(i not in "ABCDE"):
			return -1
		else:
			if i == 'A':
				items['A'] = items['A'] + 1
			elif i == 'B':
				items['B'] = items['B'] + 1
			elif i == 'C':
				items['C'] = items['C'] + 1
			elif i == 'D':
				items['D'] = items['D'] + 1
			elif i == 'E':
				items['E'] = items['E'] + 1
	for i in items.keys():
		needToPay = needToPay + add(i,items[i])

	for i in items.keys():
		needToPay=specialOffers(i,items[i],needToPay)
	return (needToPay)

