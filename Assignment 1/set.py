set = {1,2,3,4,5,6,7}
print(set)
set.add(40)
print(set)
set.update([50,60])
print(set)
set.remove(4)
print(set)
set.discard(100)
print(set)
set.discard(3)
print(set)
x = set.pop()
print(x)
print(set)

st = set.copy()
print(st)
st.clear()
print(st)

a = {1,2,3}
b = {3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))

print(a.issubset({1,2,3,4,5}))
print(a.issuperset({1,2}))