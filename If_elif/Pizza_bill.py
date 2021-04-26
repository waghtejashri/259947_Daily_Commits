def generate_pizza_bill(slices):
	if slices%2 == 0:
	    print(str(slices*120)+"/-")
	else:
	    print(str(123*slices)+"/-") 
	    
print("Enter the number of slices required: ")
slice = int(input())
generate_pizza_bill(slice)
