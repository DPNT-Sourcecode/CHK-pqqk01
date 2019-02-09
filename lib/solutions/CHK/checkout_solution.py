#Calculates the total value from the basket taking into account the special offers
def repeat(i,val):
	total = 0
	if i == 'A':
		if(val>=3):
			count = 0	
			while (val >= 3):
				val = val - 3
				count = count + 1
			total = total + ( count * 130 + 50 * val)
		else:
			total = total + 50 * val
	elif i == 'B':
		if(val>=2):
			count = 0	
			while (val >= 2):
				val = val - 2
				count = count + 1
			total = total + ( count * 45 + 30 * val)
		else:
			total = total + 30 * val
	elif i == 'C':
		total = total + 20 * val
	elif i == 'D':
		total = total + 15 * val
	return int(total) #returning the total of a specific product
				
def checkout(skus):
	needToPay =0 # Initializing the final amout needed to be paid
	items = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0} # Intitialized the dictionary of the stocks
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
	print(items)
	for i in items.keys():
		needToPay = needToPay + repeat(i,items[i])
	# return (needToPay)
	print(needToPay)

checkout("ABCDEEE")
