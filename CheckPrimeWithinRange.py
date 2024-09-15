def prime(x,y):
    mylist=[]
    for i in range(x,y+1):
        if i==0 or i==1:
                continue
        for j in range(2,int(i/2)+1):
            
            if(i%j == 0):
                break
        else:
            mylist.append(i)
    
    return mylist
ll=prime(3,9)
print(ll)