
values  = [1, 2, "Ardak", 4, 5]

print(values[0])
print(values[1])
print(values[2])
print(values[3])
print(values[-1])
values.insert(3, "Akishev")
values.append("Bye")
values[2] = "ARDAK"
del values[0]
print(values)
# tuple, same as LIST data type but immutable
val = (1, 2, "Arsen", 4.5)
print(val[1])
# Dictionary
dic = {"a": 2, 4: "Arsen", "c": "Hello World"}
print(dic)
print(dic["c"])

dict = {}
dict["FirstName"] = "Ardak"
dict["LastName"] = "Akishev"
dict["Gender"] = "Male"
print(dict)
print(dict["LastName"])