def mergeDict():
	first_Dict = {1: 'apple', 2: 'Banana' , 3: 'Orange'}
	second_Dict = { 4: 'Kiwi', 5: 'Mango'}
	print("First Dictionary: ", first_Dict)
	print("Second Dictionary: ", second_Dict)
	
	# Concatenate Two Dictionaries in Python
	first_Dict.update(second_Dict)
    
	print("\nAfter Concatenating two Dictionaries : ")
	print(first_Dict)

mergeDict()