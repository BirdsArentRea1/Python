from calendar import timegm


time = 0
#def distance(mile,kilo):

print("(m)iles or (k)ilometers")
option = input()
print ("How many miles do you want to ride your skooter")
dist = float(input())


#converts miles to km
if option == 'm' or option == 'M':
    print("converted to kilometers is", dist *1.6)

#convert km miles
if option == 'k' or option == 'K':
    print("converted to miles is", dist *0.6) 

#this figures out what the time is when it's in miles
if option == 'm' or option == 'M':
    time = dist/15
    print(time*60)


#this figures out what the time is when it's in kms
if option == 'k' or option == 'K':
    time = dist/24
    print(time*60)

print("Distance is", dist)

A= 1+.15*time
if time<=5:
    B= 2.5*time
else:
     B= 2.5+.12*time
C= 5+.06*time
print(A, B, C)

if A<B and A<C:
    print("use company A")
elif B<A and B<C:
    print("Use company B")
else:
    print("Use Company C")
