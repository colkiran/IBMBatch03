
# local variable - lexical variable - loses the scope out of a block

def fun(x):
    print(f"x :{x}")
    y = "local variable"
    print(f"y :{y}")

fun(20)

# local variables
# print(f"x :{x}")
# print(f"y :{y}")
