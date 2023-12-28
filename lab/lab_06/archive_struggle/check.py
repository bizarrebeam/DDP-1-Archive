data = {(1,2,3):"a", (4,5,6):"b"}
iS = 1
js = 2
ks = 3
x = 1
task1 = None

for key, value in data.items():
    i,j,k = key
    if k == ks:
        if x == iS or x == js:
            task1 = value

print(task1)


