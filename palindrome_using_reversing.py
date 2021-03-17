#Palindrome using reverse string
# it has O(s) basically linear running time complexity as
# as far as the number of letters in the string is concerned
def is_palindrome(s):
    original_string = s
    #reversing a string in O(n) linear time complexity
    reversed_string = reverse(s)

    if original_string == reversed_string:#Palindrome check point
        return True
    return False

#O(N) linear running time complexity
#where N is the number of letters in string s N=len(s)
def reverse(data):
    
    #string into a list of character
    data = list(data)
    
    #pointing to the first item    
    start_index = 0
    # index pointing to the last item
    end_index = len(data)-1 #since array starts from zero
    
    while end_index > start_index:
        #keep swapping the items
        data[start_index], data[end_index]= data[end_index], data[start_index]
        start_index = start_index + 1
        end_index = end_index -1
        #print(data)
    
    #transform the list of letters into a string    
    return ''.join(data)



if __name__ == '__main__':
    nam = input("Insert Data: ")
    print(is_palindrome(nam))