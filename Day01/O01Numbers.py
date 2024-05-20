
"""
1. int
2. float
3. complex
"""

a = 10
b = -10

print(f"a :{a}")    # f string or format string - interpolation
print(type(a))      # RTTI - runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.5
d = -10.5

print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3
f = -2e3

print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 5 + 2j
h = 5 - 2j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))
print("-" * 60)
print("max :", max(34, 56, 23, 67, 12, 7, 39))
print("min :", min(34, 56, 23, 67, 12, 7, 39))

print("-" * 60)
x = 2 + 3.5
print(type(x))

x = 1
y = 2.5
z = x + y

print("x =", type(x))
print("y =", type(y))
print("z =", type(z))

print("Conversions".center(60, "-"))
a = -100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number Systems".center(60, "-"))
print(11)       # decimal
print(0b11)     # binary
print(0b101)    # binary
print(0o11)     # octal
print(0o101)    # octal
print(0o111)    # octal
print(0xe)      # hexa
print(0xa)      # hexa

print("Number System Conversion".center(60, "-"))
a = 100
print("100 :", oct(a))
print("100 :", hex(a))
print("100 :", bin(a))
