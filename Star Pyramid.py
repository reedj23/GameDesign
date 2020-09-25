Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Jack Reed

rows = 14
rows2 = 7

for j in range(1, rows2+1):
    print("*" * j)
print("*"* rows, end end="n")
i = (rows//2) -1
j = 2
while i !=0:
    while j <= (rows-2):
        print("*" *i, end =" ")
        print("*" *j, end =" ")
        print("*" *i, end ="\n ")
        i = i-1
        j = j + 2

rows = 7
k = 2* rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end = "  ")
    k = k - 2
    for j in range(0, i + 1):
        print(" *", end = " ")
    print("")
