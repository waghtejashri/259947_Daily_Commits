def show_full_form(str):
    if str == "s1":
        print("Laughing Out Loud")
    elif str == "s2":
        print("Rolling on the floor laughing")
    elif str == "s3":
        print("Let Me know")
    elif str == "s4":
    	print("shaking my head")
    else:
        print("Not available") 

print("s1 = lol \ns2 = rofl\ns3 = lmk \ns4 = smh")
str = input("Enter your choice : ").strip()
show_full_form(str)