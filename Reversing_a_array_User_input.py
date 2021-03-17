#Reversing an Array or List

def reverse(nums):
    
    #pointing to the first item    
    start_index = 0
    # index pointing to the last item
    end_index = len(nums)-1 #since array starts from zero
    
    while end_index > start_index:
        #keep swapping the items
        nums[start_index], nums[end_index]= nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index -1
        
        
if __name__ == '__main__':
    #creating an empyt array/list
    arr = []
    #input number of elements
    n = int(input("Enter number of elements : "))
    
    #iterating till the range
    for i in range(0, n):
        ele = int(input())
        
        arr.append(ele) #adding the elements in the list
    print("Input Array: ", arr)
    reverse(arr)
    print("Reverse Array: ", arr)