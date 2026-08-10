#8. Write a Python program to find all the anagrams and group them
##together from a given list of strings.
#list of string
words=["eat","tea","ant","tan","ate","nat","bat","tab"]
d={}
for word in words:
    key=" ".join(sorted(word))

    if key in d:
        d[key].append(word)
    else:
        d[key]=[word]

print("anagram groups:")
for i in d. values():
   print(i)