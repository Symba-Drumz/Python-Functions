# PYTHON FUNCTIONS
# function = a block of reusable code that performs a specific task
# place a pir of brackets after the function name to invoke it

def day_of_week(purpose, time_of_day): # a parameter is a temporary variable that is used to pass information into a function
    print(f"Saturday is for {purpose}!")
    print(f"Preferably in the", time_of_day)
    print("I love Saturdays!")

day_of_week("swimming", "morning.")
day_of_week("reading", "evening.")
day_of_week("hunting", "afternoon.")

def short_bio(name, age, location):
    print(f"My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {location}.")

short_bio("Alfa", 26, "Ngong")  

# Using the return statement: this is used to end a function and send a result back to the caller
def schedule(activity, time):
    return f"I will {activity} in the {time}."
print(schedule("practice the drums", "afternoon"))
print(schedule("go to the gym", "evening")) # I can use the return statement with multiple values.

def my_parents(dad, mum):
    dad = dad.capitalize()
    mum = mum.capitalize()
    return f"My dad is {dad} and my mum is {mum}."
print(my_parents("Chris", "Judy"))

def dog_info(name, breed):
    name = name.capitalize()
    breed = breed.capitalize()
    return f"{name} is a {breed} dog."
dog_id = dog_info("Rex", "German shepherd")
print(dog_id)