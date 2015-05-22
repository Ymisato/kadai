import math

#練習問題6.1
def compare(x,y):
	if x > y:
		return 1
	elif x < y:
		return -1
	else:
		return 0
        
print compare(2,1)
print compare(1,2)
print compare(1,1)

#練習問題6.2    
def hypotenuse(x,y):
    square = x**2 + y**2
    z = math.sqrt(square)
    return z
    
print hypotenuse(3,4)
    
#練習問題6.3
def is_between(x, y, z):
    if x <= y <=z:
		return True
    else:
        return False

print is_between(2,4,6)
