# typecasting is  conversion of one data type to another data type


a ='1' #a is string
b = '2' #b is also string
print(a + b) # asboth are string it comes as combined 12
# typecasting converting string in integer
print(int(a)+int(b))

a1 = 4
b1 = 2 
print (a1+b1)

# eplicit typecasting is manually coneverting data type 
# example of ecplicit typecasting
string = "15"
number = 7
string_number = int(string) #throws error if string is not valid integer
# adding string_number and number
sum = number + string_number
# printing the sum 
print("The sum of number and string_number is :", sum)

# implicit typecasting is automatically python converts data type for the opertation
# example of implicit typecasting
c = 5.2
print(type(c))
d = 7
print(type(d))
# e is sum
e = c+d
print(e)
print(type(e))
