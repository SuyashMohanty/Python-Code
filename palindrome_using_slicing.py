#Palindrome using string slicing

def palindrome_pythom(s):
    if s == s[::-1]:
        return True
    return False

if __name__ == '__main__':
    nam = input("Insert Element: ")
    print(palindrome_pythom(nam))