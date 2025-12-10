name = ""

def validate(name):
    return name.strip() if name else None
    
while not name:
    name = validate(input("Enter your name: "))
    if not name:
        print("Name cannot be empty. Please try again.")
        name = validate(input("Enter your name: "))


        
