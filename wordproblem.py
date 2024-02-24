word1 = input("Enter a word less than 5 characters: ")
word2 = input("Enter a word less than 5 characters: ")
word3 = input("Enter a word less than 5 characters: ")

modified_word1 = ''
for i in word1:
    if 'aeiou'.__contains__(i.lower()):
        modified_word1 += '%'
    else:
        modified_word1 += i

modified_word2 = ''
for i in word2:
    if not 'aeiou'.__contains__(i.lower()):
        modified_word2 += '#'
    else:
        modified_word2 += i

modified_word3 = word3.upper()

result = modified_word1 + modified_word2 + modified_word3
print(result)
