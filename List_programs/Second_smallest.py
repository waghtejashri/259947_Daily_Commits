def secondSmallest():
	my_list = []
	  
	# number of elemetns as input
	n = int(input("Enter number of elements : "))
	  
	# iterating till the range
	for i in range(0, n):
	    ele = int(input())
	    my_list.append(ele)

	print(my_list)
	firstmin = min(my_list[0],my_list[1])
	secondmin = max(my_list[0],my_list[1])
	n = len(my_list)
	
	for i in range(2,n):
	    if my_list[i] < firstmin:
	        secondmin = firstmin
	        firstmin = my_list[i]
	    elif my_list[i]<secondmin and firstmin != my_list[i]:
	        secondmin = my_list[i]
	 
	print("Second smallest number is : ", secondmin)

secondSmallest()