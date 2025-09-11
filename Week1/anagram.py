a1=input('Enter phrase1')
a2=input('Enter phrase2')
a1=a1.lower()
a2=a2.lower()
for x in a1:
    if x.isalpha():
        if a1.count(x) == a2.count(x):
            print('Yes Anagram')
        else: print('Not an Anagram')
        break
