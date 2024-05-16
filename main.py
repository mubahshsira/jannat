q1=('''Subtruction symbol=?
a)*
b)%
c)-
d)/ ''')
q2=('''Floor division symbol=?
a)*
b)%
c)/
d)// ''')
q3=('''Multipliction symbol=?
a)*
b)%
c)-
d)/ ''')

Q={q1:"c",q2:"d",q3:"a"}
n=input("Enter your name:")
print("WELCOME TO QUIZE",n)
point=0
for i in Q:
    print(i)
    j=input("do u want to skip :")
    if j=="yes":
        continue
    ans=input("Enter the ans:")

    if ans==Q[i]:
        print("Correct ans.You got 1 point ")
        point+=1
        print("Your current point in",point)
    else:
        print("Wrong ans.You got no point")
        point=point
print("Fainally you got",point,"point")

