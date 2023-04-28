def number():
    x=range(10)
    for i in x:
      if i%2==0:
            print(i)

#  odd number      
def odd_number():
     c=range(20) 
     for i in c:
         if i%2 !=0:
             print(i)    

def divisible_by_five():
    v =range(100)
    for i in v:
        if i%5==0:
            print(f"{i} is divisible by 5")
        else:
            print(f"{i} is not disvisible by 5")


def multiplycomparison():
    x =range(30)
    for i in x:
        if i%2==0:
            print(f"{i} is divible by 2")
        elif i%3==0:
            print(f"{i} is divible by 3")
        elif i%5==0:
             print(f"{i} is divible by 3")
        else:
             print(f"{i} is not divible by 2,3,5")


def divisible_by_two_and_three():
    x =range(30)
    for i in x:
        if i%2==0 and i%3==0:
            print(f"{i} is divible by both 2 and 3")
        elif i%2==0 or i%3==0:
            print(f"{i} is divible by either 2 or 3")
        else:
             print(f"{i} is not divible by 2 or 3")

def while_loop():
    x=1
    while x<10:
        print("Hello while")
        x+=1  
        
def break_statement():
    x=1
    while x<10:
        print("Hello while")
        x+=1  
        if x==5:
            break            
def continues_statement():
    x =0
    while x<20:
        x+=1
        if x%2==0:
            continue
        print(x)      
      