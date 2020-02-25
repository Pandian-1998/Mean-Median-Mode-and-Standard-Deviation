#Mean:
def Mean(a):
    sum=0
    for elements in a:
        sum=sum+elements
        answer=sum/len(a)
    print(answer)
a=[5,5,5,5,5]
print(Mean(a))


#Median
def Median(a):
        if len(a) % 2 == 0:
            answer1 = a[len(a)//2]
            answer2 = a[len(a)//2-1]
            answer = (answer1 + answer2)/2
            print(answer)
        else:
            ans=len(a)//2
            print(a[ans])
a=[11,12,13,14,15,16,17,18]
print(Median(a))  
     

#Mode
def Mode(d):
    for i in range(0,len(d)):
        repeat=d[i]
        for j in range(i+1,len(d)):
            if d[j] == repeat:
                print(d[j])                
d=[10,3,4,7,10,2,10,5,9,7,2]
print(Mode(d))

# #StandardDeviation
def StandardDeviation(s):
    sum = 0
    for i in s:
        sum = sum + i
    print(sum)
    n=len(s)
    xbar = sum / len(s)
        x_xbar = 0
        answer=0
        for j in range(0,len(s)):
            x_xbar=s[j]-xbar * s[j]-xbar
            answer=answer + x_xbar
        sd=answer/n
        print(sd)  
    # print(sum)
    # print(xbar)
    # print(n)
s=[1,2,3,4,15]
print(StandardDeviation(s))



def mode(a): 
    counter = 0
    num = a[0] 
    for i in a: 
        repeat = a.count(i) 
        if(repeat > counter): 
            counter = repeat 
            num = i
            print(str(num) + " is present " + str(counter) + " times.") 

a=[10,7,4,7,4,10,10,7,10,7,7,10,9,10]
mode(a)
