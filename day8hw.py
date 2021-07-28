
apples = int(input("how many apples do you have:"))
print(apples)
money = int(input("how much is one apple:"))
print(money)
print("-----------")
s = 0
p = 0
mylist = []
while True:
    a = int(input("choose one\nbuy:1\nsell:2\nselling data:3\nthe number of apple you have left:4\nstop:5\nyour number:"))
    print(a)
    
    if a==1:
        b = int(input("buy how many apples:"))
       
        apples = apples + b
    elif a==2:
        
        c = int(input("sell how many apples:"))
        
        if c >apples:
            print("apples not enough")
        if c <= apples:
            apples = apples - c
            s = money*c + s
            print("still have" ,apples , "apples")
            print("you made", s)
            mylist.append(c)
            p = p+1
    elif a==3:
        print("sell" , mylist ,"many apples every time")
        print("sell" , p , "times")
        print("total money you made" , s)
    elif a==4:
        print("you have" ,apples , "apples left") 
    elif a==5:
        break
    
    
        