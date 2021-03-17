#Reversing an Array or List without using extra memory

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
    
    n = [1,2,3,4]
    reverse(n)
    print(n)