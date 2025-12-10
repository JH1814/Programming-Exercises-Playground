def function(msg="Hello"):
    print(msg)

function("Hello World")


def print_all(messages: list[str] = None): #empty list as default value = dangerous!!!
    if messages is None: # always use None for values which have to be instantiated
        return
    for msg in messages:
        print(msg)

print_all("Hello World")

print_all(["Hello World",])

def printMessage(user, messages= None): #empty list as default value = dangerous!!!
    if messages is None: # always use None for values which have to be instantiated
        messages=""
    
    print(f"{user}: {messages}")

printMessage("joni", "Hello, I teach you Python today!")

msg = (
    "Hello my name is Joni \n"
    "I'm at FHNW and teaching a great class!"
)

print(msg)

