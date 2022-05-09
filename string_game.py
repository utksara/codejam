
def do (S):
    word_stack  = []
    temp_stack = []
    single_stack = []
    retrunval = ""
    for i in range(1, len(S)):
        if (S[i-1]< S[i]):
            word_stack.append(S[i-1])
            word_stack.append(S[i-1])
            if(i == len(S)-1):
                word_stack.append(S[i])
            word_stack = temp_stack + word_stack
            temp_stack = []
        if (S[i-1] == S[i]):
            temp_stack.append(S[i])
        else:
            temp_stack = []
            word_stack.append(S[i-1])
            if(i == len(S)-1):
                word_stack.append(S[i])
    
    return retrunval.join(word_stack + single_stack)

print(do("ABCD"))