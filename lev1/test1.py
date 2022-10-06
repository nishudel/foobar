from math import *
 


 

def solution(s):
    # Your code here
    input_string=s
    n=len(input_string)
    set_factors=set( )
    i=1
    while(i*i<n):
        if (n%i==0):
            set_factors.add(i)
        i+=1
    
    for i in range(int(n/2),0,-1):
        if n%i==0:
            set_factors.add(i)
       
    all_divisors=list(set_factors)
    all_divisors.sort()
    #print(all_divisors)
    
    list_cuts=[]
    flag_divide=True
    num_cuts=0
    for elem in list(all_divisors):
        reference=input_string[0:elem]
        for i in range(0,int(len(input_string)/elem)-1):
            temp=input_string[(i+1)*elem:(i+2)*elem]
            if reference==temp:
                flag_divide=True
            else:
                flag_divide=False
                break
        if flag_divide==True:
            list_cuts.append(elem)
            num_cuts=int(len(input_string)/list_cuts[0])
            break   
            
        #if len(list_cuts)==2:
        #    num_cuts=int(len(input_string)/list_cuts[0])
        #    break
    
    if flag_divide==False:
        num_cuts=1
    #if len(list_cuts)!=0 and num_cuts==0:
    #    num_cuts=int(len(input_string)/list_cuts[0])


    #if num_cuts==0:
    #    return 1
    #else:
    return num_cuts




    


a=input()

print(solution(a))
