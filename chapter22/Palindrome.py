def palindrome(word):
    word = word.lower()
    # メモ：スライス[l:m:n] l番目からm番目の要素までnごとに切りだし
    return word[::-1] == word

print(palindrome("Mother"))
print(palindrome("Mom"))
