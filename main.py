

def input_str(msg:str=None):
    user_in = input(msg)
    if user_in == "\exit":
        return False
    else: 
        return user_in

def main():
    print("welcome too the darkside of coding")
    print("Enter \exit to exit the program")
    app_loop(user_in)
    user_in = input_str("man: ")
    while user_in or user_in== "":
        print("user_in")
        user_in = input_str("man: ")

def app_loop(user_in):
    while user_in or user_in =="":
        print(user_in)
        user_in = input_str("man:  and ")    

if __name__ == "__main__":
    main()
