
# global scope

glbx = 100

def fun(a):                # a is a local variable
    print("-" * 60)
    global glbx            # do not assign any value in this line
    print(f"a :{a}")
    #glbx = 250            # local variable with the same name of global
    glbx = 250
    print(f"glbx inside :{glbx}")
    print("-" * 60)

print(f"Before :{glbx}")

fun(25)

print(f"After :{glbx}")
