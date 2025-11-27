
'''sumop=lambda a,b:a+b



#main program
a,b=float(input("Enter number: ")), float(input("Enter number: "))
res=sumop(a,b)
print(res)'''


"""p=lambda value:"palindrome" if value==value[::-1] else "not palinorme"

#main program
value=input("Enter words:")
res=p(value)
print(res)"""



vowelornot=lambda word:"vowel" if 'a' in word.lower() or  'e' in word.lower() or 'i' in word.lower() or 'o' in word.lower() or 'u' in word.lower() else 'vowel not'

#main program
value=input("Enter word:")
res=vowelornot(value)
print(value,res)


def isprime(n):
    res=True
    for i in range(2,n):
        if n%i==0:
            res=False
            break
    return res


#anonymous function
prime=lambda n:"{} is invalid input".format(n) if n<=1  else "{} is prime".format(n) if isprime(n) else "{} is not prime".format(n)
#main program
n=int(input("Enter number:"))
res=prime(n)
print(res)