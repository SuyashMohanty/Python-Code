"""
Duplicates in an array problem
-------------------------------

Here we want to find duplicates in one-dimensional array of integers in O(N)
running time where the integer values are smaller than the length of the array

For example: if we have a list [1,2,3,1,5] then the algorithm can detect
             that there are duplicates with value 1.
             
To check no of repetations in 1-dimentional array in linear time complexity
reference: https://www.udemy.com/course/algorithms-and-data-structures-in-python/learn/lecture/11408418#questions
"""
def find_duplicates(nums):
    
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print('Repetition found: %s' %str(abs(num)))
            
if __name__ == '__main__':
    
    #This Method cannot handle values < 0 !!!
    #The maximum item is smaller than the size of the list
    n = [2, 6, 5, 1, 4, 3, 2]
    find_duplicates(n)