l1 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
l2 = ['a','e','i','o','u','A','E','I','O','U']

ch = str(input())
if (ch in l1):
    print ("Consonant")
elif (ch in l2):
    print ("Vowel")
else:
    print("invalid")
