import numpy as np
import math


def get_all_p_factors(n):
    set_factors=set()
    while n%2==0:
        n=n/2
        set_factors.add(2)

    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i==0:
            n=n/i
            set_factors.add(int(i))

    if n>2:
       set_factors.add(int(n))

    return set_factors


input_string=input()
all_factors=get_all_p_factors(len(input_string))
flag=False
cut_len=100000
for elem in list(all_factors):
    reference=input_string[0:elem]
    for i in range(1,int(len(input_string)/elem)+1):
        if reference==input_string[0+i*elem:elem+i*elem]:
            flag=True
        else:
            flag=False
    if flag==True:
        if cut_len>=elem:
            cut_len=elem

print(int(len(input_string)/cut_len))
    