cardinal_numbers = ("first", "second", "third")
print(cardinal_numbers[1])  


position1, position2, position3 = cardinal_numbers
print(position1)
print(position2)
print(position3)

my_name = tuple("Shuhrat")  
print("x" in my_name)  


new_tuple = my_name[1:]
print(new_tuple)

#HOMEWORK 2
food=["rice","beans"]
food
food.append("brocolli")
food.extend(['pizza','bread'])

print(food[:2])
print(food[-1])
breakfast = "eggs, fruit, orange juice".split(", ")
print(len(breakfast))
lengths = [len(item) for item in breakfast]  
print(lengths)


##1
num= ['1','2','3']
smallest=min(num)
print(smallest)
##2
colors=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colors.pop(5)
colors.pop(4)
colors.pop(0)
print(colors)
##5 
colors.append(num)
print(colors)

#1
length= '123456789'
print(len(length))
#2
string= '123456'
print(string[:2])
print(string[-2:])
#8
exp= 'hELLo WORld'
print(exp.swapcase())
#10
exp[:3]
#11
print(string[::-1])
#12
exp.startswith('he')
