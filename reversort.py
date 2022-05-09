from operator import index


T = int(input())

def push_min_stack(min_stack, x):
    if min_stack[-1] == -1:
        k = len(min_stack)-1
        while k >=0:  
            if min_stack[k] == -1 : 
                k = k-1
            else : break
        min_stack[k] = x
    else: 
        for k in range(0,len(min_stack)-1):
            min_stack[k] = min_stack[k+1]
        min_stack[-1] = x

    return min_stack

def do(a_L):

    min_stack = [-1, -1, -1]
    min_val = a_L[0]
    for  i_i in range(0, len(a_L)):
        if a_L[i_i] < min_val:
            min_val = a_L[i_i]
            min_stack = push_min_stack(min_stack, i_i)
        print(min_stack)


for i in range(0, T):
    L = []    
    N = int(input())
    
    raw_input = input().split()
    
    for j in range(0, N):
        L.append(int(raw_input[j]))
    
    do(L)
