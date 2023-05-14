katz_deli=[]

def line(katz_deli):
    if len(katz_deli) == 0:
        print ("The line is currently empty.")
    else:
        queue=[f"{i+1}. {name}" for i, name in enumerate (katz_deli)]
        print ("The line is currently: " + " ".join(queue))


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    i=len(katz_deli)
    print(f"Welcome, {name}. You are number {i} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving = katz_deli[0]
        print(f"Currently serving {serving}.")
        katz_deli.remove(serving)


