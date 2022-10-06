

def get_all_divisors(input_string):
    num=len(input_string)
    n=len(input_string)
    set_factors=set( )
    # To make n cuts ussing n m&ms
    set_factors.add(1)
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
       set_factors.add(int(num/n))
    return set_factors

input_string=input()

# all factors
all_divisors=list(get_all_divisors(input_string))

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
    if len(list_cuts)==2:
        num_cuts=int(len(input_string)/list_cuts[0])
        break

if flag_divide==False:
    num_cuts=0
if len(list_cuts)!=0 and num_cuts==0:
    num_cuts=int(len(input_string)/list_cuts[0])

print(num_cuts)

