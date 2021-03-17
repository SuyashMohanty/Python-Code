'''
Reversing an Integer
_________
|1|2|3|4|
--------
Step1: We are after the lat digit in every iteration
     ~We can get it using modulo(%) operation:
         the last digit is the remainder when divided by 10
         
Step2: We have to make sure to remove the digit from the original number
     ~so we just have to divide the original number by 10.
'''

def reverse_integer(n):
    
    reversed_integer = 0
    remainder = 0
    
    while n > 0:
        remainder = n % 10
        reversed_integer = reversed_integer*10 + remainder
        #print(remainder)
        #print(reversed_integer)
        n = n // 10 #//(integer division)gives output in the form of integer not floating point
        #print(n)
    
    return reversed_integer
    

if __name__ == '__main__':
    n = int(input("input value of integer: "))
    print("Reversed integer: ",reverse_integer(n))