palindromes = [palindrome for palindrome in input().split() if palindrome == palindrome[::-1]]
palindrome = input()

print(palindromes)
print(f"Found palindrome {palindromes.count(palindrome)} times")
