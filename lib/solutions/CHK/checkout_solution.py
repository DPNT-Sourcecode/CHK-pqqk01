items = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0} # Intitialized the dictionary of the stocks
#Calculates the total value from the basket taking into account the special offers

def specialOffers(i,val,discount):
	if i == 'A':
		if val >= 5:
			count = 0
			while val >= 5:
				val = val - 5
				count = count + 1
			discount = discount - (count * 50)
		if val >= 3:
			discount = discount - 20
	elif i == 'B':
		if items['E']>=2 and val != 0:
			aux = items['E']
			while aux >= 2:
				aux = aux - 2
				val = val - 1
				discount = discount - 30
		if val >= 2:
			while val >= 2:
				val = val - 2
				discount = discount - 15
	return int(discount)

# Computes the total without applying the discount
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
		

	# 	total = 0
	# if i == 'A':
	# 	if(val>=5):
	# 		count = 0
	# 		while (val >= 5):
	# 			val = val -5
	# 			count = count + 1
	# 		total = total + ( count * 200)
	# 	if(val>=3):
	# 		count = 0	
	# 		while (val >= 3):
	# 			val = val - 3
	# 			count = count + 1
	# 		total = total + ( count * 130 + 50 * val)
	# 	else:
	# 		total = total + 50 * val
	# elif i == 'B':
	# 	if(val>=2):
	# 		count = 0	
	# 		while (val >= 2):
	# 			val = val - 2
	# 			count = count + 1
	# 		total = total + ( count * 45 + 30 * val)
	# 	else:
	# 		total = total + 30 * val
	# elif i == 'C':
	# 	total = total + 20 * val
	# elif i == 'D':
	# 	total = total + 15 * val
	# elif i == 'E':
	# 	if(val>=4): # 45 pounds discount is applied (2 items of B)
	# 		count45 = 0
	# 		while val >= 4:
	# 			val = val - 4
	# 			count45 = count45 + 1
	# 		total = total + (count45 * 160 - count45 * 45)
	# 	if val >= 2: # 30 pounds discount is applied (1 item of B)
	# 		val = val - 2
	# 		total = total + 80 - 30
	# 	if val == 1:
	# 		total = total + 40
	# return int(total) #returning the total of a specific product		
def checkout(skus):
	needToPay =0 # Initializing the final amout needed to be paid

	#Count how many products are in the basket
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
		needToPay = specialOffers(i,items[i],needToPay)
	print(needToPay)
	return (needToPay)

checkout("CCADDEEBBA")

