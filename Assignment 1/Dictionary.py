Dict = {"name":"uday","Surname":"Raut","age":19}
x = Dict.copy()
print(x)

print(x.get("name"))
print(x.keys())
print(x.values())
print(x.items())
Dict.update({"name":"udai"})
Dict["city"] = "Silvassa"
print(Dict)
print(x.pop("name"))
print(x.popitem())
x.clear()
print(x)
x = dict.fromkeys(["a","b"],0)
print(x)

