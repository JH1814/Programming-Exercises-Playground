def input_int(msg:str) -> int:
    is_valid = False
    while not is_valid:
        try: 
            number = int(input(msg))
            is_valid = True
        except:
            print("Invalid input. Please enter a valid integer.")
    return number


def input_int_fancy(msg:str) -> int:
    while True:
        try: 
            return int(input(msg))
        except ValueError as e:
            print(f"Invalid input. Please enter a valid integer. Error details: {e}")
        except ConnectionError as e:
            print(f"Connection error occurred. Please try again later. Error details: {e}")

input_int("Please enter a number: ")
input_int_fancy("Please enter a number: ")