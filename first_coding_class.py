# this is a comment

"""Multili
line comment
"""

x =10
# print on console 
print(x)

#input from command line
y = input("write  a number here: ")
print(y)

# mathematical operator
# +,-,*,/,pow,modulo


# character variables
a = 'x'
print(a)
# list of character called string

tomato = 'a quick brown fox jumps over the lazy dog' # all letter of english a to z
onion = "buffalo buffalo buffalo buffalo buffalo" # can make sentence in any numbers of buffalo
# spcial meaning

# operator oveloading
print(tomato+onion)
print(onion*5)

#print(tomato*onion) # this will give error

# indexing
tomato = 'a quick brown fox jumps over the lazy dog'
potato = "buffalo buffalo buffalo buffalo buffalo"

print(tomato[5]) # 6th character indexing start from 0
print(tomato[5:10])
print(tomato[5:])
print(tomato[:5])
print(tomato[-5])

# list

pumpkin = [ 'tomato','potato', tomato, potato, 10, 20.4]
print(pumpkin[2])
print(pumpkin[2:4])

# lenth of the list or string
print (len(pumpkin))

# comparision operator
print(100>30)
print(100>500)
print(30>=0)
print(30<=0)
print(30==30)
print(30!=30)

# python is case sensitive

# single =(asignments) versus double == (comparison)
rose = 100
print(rose==10)
print(rose==100)
rose+=10
print(rose==110)

# Boolean operator
tomato = 10
onion = 5
print(tomato>onion or tomato< onion)
print(tomato>onion and tomato< onion)
print(not tomato>onion)