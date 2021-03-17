"""
Angram problem:An angram is a word or phase formed by rearranging 
the letters of different word or phase,typically using all 
the original letters exactly once
        or
thot check if all the alphabets or letters in both 
the strings are same or not
ex:- restful and fluster
"""

def is_anagram(str1, str2):
    
    #if the length of the string differ - they are not angrams
    if len(str1) != len(str2):
        print("Length of string is different")
        return False
    
    #we have to sort the letters of the strings and then we have to
    #compare the letters with the same indexes
    #this is the bottlenect/fastest because it has o(NlogN)
    str1 = sorted(str1)
    str2 = sorted(str2)
    
    #print(str1)
    #print(str2)
    
    #after that we have to check the letters with the same indexes
    for i in range(len(str1)):#since length of str1 & str2 is same already checked
        if str1[i] != str2[i]:
            return False
    return True

if __name__ == '__main__':
    
    s1 = list(input("input string-1: "))
    s2 = list(input("input string-2: "))
    
    print(is_anagram(s1, s2))
    