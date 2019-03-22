


x=6

if x<0:
	x=0 
	print('Negative changed to zero')

elif x==0:
	print('Zero')

elif x==1:
	print('single')

else:
	print('More')



## using for loop

words =['raks', 'pranav', 'sharv']

for w in words:
	print( w, len(w))


# using range function

print (range(5))

print(range(5,10)) # specify start num , print all numbers from 5 to 10

print ( range(0, 10 , 3)) # we are using 3 as increment 


# break  and continue statement

for n in range(2, 10):
     for x in range(2, n):
         if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n, 'is a prime number')


### continnue staement


for num in range(2, 10):
        if num % 2 == 0:
        	print("Found an even number", num)
                continue
print(" found number ", num)


# pass statement does nothing , usually its used if statement required syntactically but action need to taken 


while true: 
	pass








 
