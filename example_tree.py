def solutions(h,q):
    p=[]
    #Exception
    for elem in q:
        if elem>=((2^h)-1) or elem<=0:
            p.append(-1)
        
    # Track a map left(-1) or right(0)
    #maps=[]
    #for elem in q:
    map=[]
    status=False    
    elem=q[0]
    for level in range(h,0,-1):
        if status==False:
            track_val=(2**h)-1
       
            
            print("track_val,level",track_val,level)            

            if elem<=track_val-1 and elem>track_val-(2**(level-1)):
                map.append('r')
                #print("action: right")
            else:
                map.append('l')

            if len(map)!=0:
                print(map)
                for dir in map:
                    if dir=='r':
                        track_val+=-1
                    if dir=='l':
                        track_val+=-(2**(level-1))

            if elem == track_val:
                if map[-1]=='r':
                    p.append(track_val+1)
                    print("found match in right")
                    print(track_val)
                elif map[-1]=='l':
                    p.append(track_val+(2**(level-1)))
                    print("found match in left")
                    print(track_val)
                status=True
                break            

                #print("action: left")
    #print(map)


    #if elem==track_val or elem==track_val-(2^level)+1:
    #    status==True
    #    p.append(track_val+1)



    return p


#
#a=[1,2]
#h=5
#print(solutions(h,a))
solutions(5,[15])


## Check the input type
#a=input()
#levels=5
#a=[eval(i) for i in a]

#print(solutions(levels,int(a)))