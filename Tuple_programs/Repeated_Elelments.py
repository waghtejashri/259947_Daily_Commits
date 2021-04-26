def repeatedElements(tuple1):
	for i in tuple1:
		if tuple1.count(i) > 1:
			print("Repeated")
			print(i)
			break;



tuple1 = (3, 7, 9, 2, 2, 1, 5, 6, 8)
repeatedElements(tuple1)