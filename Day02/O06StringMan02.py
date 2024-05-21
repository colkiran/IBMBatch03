
st1 = 'hello world'
st2 = "the quick brown fox jumps over the lazy dog"

print("find".center(60, "-"))
print(f"st1 :{st1}")
indx = st1.find("w")
print(f"Index :{indx}")

indx = st1.find("l")
print(f"Index :{indx}")
# hard coding
indx = st1.find("l", 6)
print(f"Index :{indx}")

# generic code
indx = st1.find("l", st1.find("l") + 1)
print(f"2nd Index of l :{indx}")

indx = st1.find("l", st1.find("l", st1.find("l") + 1) + 1)
print(f"3rd Index of l :{indx}")

print("-" * 60)
print(st2.find("the"))
print(st2.find("the", st2.find("the") + 1))

print("replace".center(60,  "-"))
print(f"st1 :{st1}")
res = st1.replace("w", "W")
print(f"res :{res}")

res = st1.replace("l", "L", 1)
print(f"res :{res}")

print("-" * 60)
print(f"st2 :{st2}")

res = st2.replace("the", "The", 1)
print(f"res :{res}")

print("-" * 60)
st = "*****hello*****"
print(f"st :{st}")

print(f"left side :{st.lstrip('*')}")
print(f"right side :{st.rstrip('*')}")
print(f"both side :{st.strip('*')}")

# maketrans, translate
print("maketrans".center(60, "-"))
# replace charaters
st = "hello world"
print(f"st :{st}")
a = "helowrd"
b = "HELOWRD"
# rule is length of a and b should be the same
resTbl = st.maketrans(a, b)
print(f"resTbl :{resTbl}")

print("Translate".center(60, "-"))
res = st1.translate(resTbl)
print(f"res :{res}")
