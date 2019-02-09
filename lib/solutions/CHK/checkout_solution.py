

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	items = [0] * 4
	total = 0
	for i in skus:
		if(i not in "ABCD"):
			print("wrong")
		if i == 'A':
			items[0] = items[0] + 1
		elif i == 'B':
			items[1] = items[1] + 1
		elif i == 'C':
			items[2] = items[2] + 1
		elif i == 'D':
			items[3] = items[3] + 1
	

    # raise NotImplementedError()


checkout("EAABACDBBAD")
