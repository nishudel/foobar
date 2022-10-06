def solution(s):
    # Your code here
    input_string=s
    num=64#len(input_string)
    n=64#len(input_string)
    set_factors=set( )
    # To make n cuts ussing n m&ms
    set_factors.add(1)
    #set_factors.add(num)
    while n%2==0:
        n=n/2
        set_factors.add(2)
        set_factors.add(int(num/2))
    for i in range(3,int(n/2)+1,2):
        while n%i==0:
            n=n/i
            set_factors.add(int(i))
            set_factors.add(int(num/i))
    if n>2:
       set_factors.add(int(n))
       #set_factors.add(int(num/n))
       
    all_divisors=list(set_factors)
    all_divisors.sort()
    print(all_divisors)
    
    '''
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
    #return num_cut
    '''
    return 0



    


a=input()

print(solution(a))