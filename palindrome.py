#palindrome check
def palindrome(n):
    n_str = str(n)
    revn_str = n_str[::-1]
    if n_str==revn_str:
        return("Palindrome")
    return("Not Palindrome")
num=(input("Enter a number :"))
print(palindrome(num))
