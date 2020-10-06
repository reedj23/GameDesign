from copy import deepcopy
#create a tuple
tuplex=("Hello", 5, [], True)
print(tuplex)

tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)
print(tuplex_colon)
print(tuplex)
x = ("apple","banana, "cherry")
y=list(x)
y[1]="kiwi"
print(type(y))
x=tuple(y)
print(type(x))
aList= [(1,2),(4,5),(8,9)]
print(list(zip)(*aList)))
