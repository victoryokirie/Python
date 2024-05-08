def new_fun():
    print("This is a new function")

def fxn_with_param(name):
    print(f"Hello {name}")

#fxn with multiple param
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"what is like in {location}?")

#note the difference between positional and keyword arguments
greet_with(location="London", name="Victory")
greet_with("Angela", "Malaysia")