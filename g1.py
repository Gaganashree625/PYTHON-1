swapping two numbers
#there are five ways

a,b=10,20
print(f"a: {a}, b: {b}")
a,b=b,a
print(f"a: {a}, b: {b}")

#using third variable
a,b=10,20
print(f"a: {a}, b: {b}")
c=a
a=b
b=c
print(f"a: {a}, b: {b}")

#using arithmetic operator 
a,b=10,20
print(f"a: {a}, b: {b}")
a=a+b
b=a-b
a=a-b
print(f"a: {a}, b: {b}")

# using xor operation
a,b=10,20
print(f"a: {a}, b: {b}")
a=a^b
b=a^b
a=a^b
print(f"a: {a}, b: {b}")

#using temp variable
a,b=10,20
print(f"a: {a}, b: {b}")
temp=a
a=b
b=temp
print(f"a: {a}, b: {b}")


# reversing numbers from descending to ascending
#there are three approaches
l=[23,56,87,56,90,23]
l.sort(reverse=True)
print(l)

l=[23,56,87,56,90,23]
l.sort()
l.reverse()
print(l)

l=[23,56,87,56,90,23]
l.sort()
print(l[::-1])



#Adding sum of n numbers
#there are two approaches
total=0
for i in range(1,11):
    total=total+i
print(total)

#using formula  n(n+1/2)
print(int(10*11/2))