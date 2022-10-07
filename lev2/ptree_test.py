# Your code here
    q=list(q)
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
    return p