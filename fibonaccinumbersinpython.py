a = int(input("Enter the number of terms"))
f = 0
s = 1
if a<=0 :
    print("The required series is:", f)
else:
    print(f, s, end = " ")
    for n in range(2, a):
        next = f+s
        print(next, end = " ")
        f = s
        s = next
    
