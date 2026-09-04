txt = "       apple        "
print(txt)
x = txt.lstrip()
print(x+".")
x = x.rstrip()
print(x+".")

mytable = x.maketrans("p", "b")
print(x.translate(mytable))

student = {
    "name" : "hyerim",
    "age" : "28",
    "studentid" : "왹져박사"
}
y = student.keys()
print(y)
student["color"] = "green"
print(y)

v = student.values()
print(v)

print(student.items())