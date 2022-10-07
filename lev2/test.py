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