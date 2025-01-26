#arithmetic operations
num1=5
num2=3
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
print(num1 // num2)
#complex numbers
num1=2+3j
num2=4+5j
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
#strings
str='hello'
print(len(str))
print(str)
str='hello everyone'
print(str)
#indexing and slicing
str='hello everyone'
print(str[2])
print(str[2:])
print(str[:9])
print(str[-2])
print(str[-3:])
print(str[2:5])
#boolean
num= 2 < 3
print(num)
a= 30/2 == 16
print(a)
#sequence
#list
list=[1,2,3,4,['hello','True','False'],5,6]
print(len(list))
list[4][1]='good morning' #mutable
print(list)
list[5]='five'
print(list)
#tuple
tuple=(1,2,3,4,['hii','welcome'],'five','six')
print(tuple)

#dictionary
dict1={1:'allu arjun',2:'mahesh',3:'prabhas',4:'ram charan'}
print(dict1)
dict1[2]='rana'
print(dict1)
#set
set1={1,2,3,3,4,4,5,5,6,2,2,1,2,'string','string2'}
print(set1)