
# fibonaci series for arbitrary boundary

def fib1(n):
	result= []
	x, y=0, 1
	
	while x < n:
		result.append(x)
		x, y= y, x+y
	return result

### FUNCTION CALL

f1=fib1(10)

print(f1)
