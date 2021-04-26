def dict(peeps):
	print(peeps)
	print(peeps[1]['name'])
	print(peeps[1]['age'])
	print(peeps[1]['sex'])

	for p_id, p_info in peeps.items():
		print("\nPerson ID:", p_id)
		
		for key in p_info:
			print(key + ':', p_info[key])


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

dict(people)