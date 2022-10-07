def solutions(h,q):
    '''
    q_str=str(q)
    print("q_str",q_str)
    q_sub_str=q_str[1:len(q_str)-1].replace(" ","")
    print("q_sub_str",q_sub_str)
    list_string=q_sub_str.split(",")
    print("list_string",list_string)
    q_new=[]
    for elem in list_string:
        q_new.append(int(elem))
    print("q_new",q_new)
    '''
    p=[]
    #Exception
    #for elem in q:
    #    print(elem)
    #    if elem>=((2^h)-1) or elem<=0:
    #        p.append(-1)
        
    # Track a map left(-1) or right(0)
    #maps=[]
    for elem in q:
        map=[]
        #print(map)
        status=False    
        for level in range(h,0,-1):
            if status==False:
                track_val=(2**h)-1
                if len(map)!=0:
                    #print(map)
                    #print("level",level)
                    temp_level=h
                    for dir in map:
                        temp_level+=-1                    
                        if dir=='r':
                            #print('trackval_bef',track_val)
                            track_val+=-1
                            #print('trackval_aft',track_val)
                        if dir=='l':
                            #print('trackval_bef',track_val,-(2**(temp_level))) 
                            track_val+=-(2**(temp_level))     
                            #print('trackval_aft',track_val)  
                
                if elem<=track_val-1 and elem>track_val-(2**(level-1)):
                    map.append('r')
                    #print("action: right")
                else:
                    map.append('l')

                if elem == track_val:
                    #print(map[-2])
                    if map[-2]=='r':
                        p.append(track_val+1)
                        #print("found match in right",track_val+1)
                        #print(track_val)
                    elif map[-1]=='l':
                        p.append(track_val+(2**(level)))
                        #print("found match in left",(2**(level)))
                        #print(track_val)
                    status=True
                    break            

        if status==False:
            p.append(-1)


    #if elem==track_val or elem==track_val-(2^level)+1:
    #    status==True
    #    p.append(track_val+1)
    #for a,b in zip(p,q):
    #    print(a,b)
    return p


#
#a=[1,2]
h=30
b=[19,14,21]
print(b)
print(solutions(h,b))

def solution(h, q):
# Your code here
    q=list(q)
    p=[]
    for elem in q:
        if elem>=(2**h)-1:
            p.append(-1)
            continue
        map=[]
        status=False    
        for level in range(h,0,-1):
            if status==False:
                track_val=(2**h)-1
                if len(map)!=0:
                    temp_level=h
                    for dir in map:
                        temp_level+=-1                    
                        if dir=='r':
                            track_val+=-1
                        if dir=='l':
                            track_val+=-(2**(temp_level))  

                if elem<=track_val-1 and elem>track_val-(2**(level-1)):
                    map.append('r')
                else:
                    map.append('l')
                if elem == track_val:
                    #print(map)
                    if map[-2]=='r':
                        p.append(track_val+1)
                        
                    elif map[-2]=='l':
                        p.append(track_val+(2**(level)))
                    status=True
                    break            

        if status==False:
            p.append(-1)
    return p

h=5
b=[31,31,15,30]#,200,30,100000,10.75]
print(solution(h,b))