def swap(x, pos1, pos2):
    x[pos1]  = x[pos1] + x[pos2]
    x[pos2]  = x[pos1] - x[pos2]
    x[pos1]  = x[pos1] - x[pos2]


def swapped_prod(x, y):   
    if len(x) == 0 or len(y) == 0:
        return 0 
    min_x = min(x)
    min_x_pos = [l for l in range(0, len(x)) if x[l] == min_x][0]
    max_x = max(x)
    max_x_pos = [l for l in range(0, len(x)) if x[l] == max_x][0]

    min_y = min(y)
    min_y_pos = [l for l in range(0, len(y)) if y[l] == min_y][0]
    max_y = max(y)
    max_y_pos = [l for l in range(0, len(y)) if y[l] == max_y][0]

    if (min_x_pos == max_y_pos and max_x_pos == min_y_pos ):
        prod_ = x[min_x_pos]* y[max_y_pos] +  x[max_x_pos]* y[min_y_pos]
        i_i = 0
        while i_i < len(x):
                if x[i_i] == min_x or x[i_i] == min_y or x[i_i] == max_x or x[i_i] == max_y:
                    del x[i_i]
                    del y[i_i]
                    i_i -= 1
                i_i +=1
        return prod_ + swapped_prod(x, y)

    elif (min_x_pos == max_y_pos):
        prod_ = x[min_x_pos]* y[max_y_pos] 
        i_i = 0
        while i_i < len(x):
                if x[i_i] == min_x or x[i_i] == max_y:
                    del x[i_i]
                    del y[i_i]
                    i_i -= 1
                i_i +=1
        return prod_ + swapped_prod(x, y)

    elif ( max_x_pos == min_y_pos):
        prod =  x[max_x_pos]* y[min_y_pos]
        i_i = 0
        while i_i < len(x):
                if x[i_i] == x[i_i] == min_y or x[i_i] == max_x:
                    del x[i_i]
                    del y[i_i]
                    i_i -= 1
                i_i +=1
        return prod_ + swapped_prod(x, y)

    else:
        prod = 0
        if( max_x_pos == max_y_pos and min_y_pos ==  min_x_pos):
            prod = x[min_x_pos]* y[max_y_pos] +  x[max_x_pos]* y[min_y_pos]

            i_i = 0
            while i_i < len(x):
                if x[i_i] == min_x or x[i_i] == min_y or x[i_i] == max_x or x[i_i] == max_y:
                    del x[i_i]
                    del y[i_i]
                    i_i -= 1
                i_i +=1
            
            print(x, y)

            min_x = min(x)
            min_x_pos = [l for l in range(0, len(x)) if x[l] == min_x][0]
            max_x = max(x)
            max_x_pos = [l for l in range(0, len(x)) if x[l] == max_x][0]

            min_y = min(y)
            min_y_pos = [l for l in range(0, len(y)) if y[l] == min_y][0]
            max_y = max(y)
            max_y_pos = [l for l in range(0, len(y)) if y[l] == max_y][0]

            sum1 = x[max_x_pos] * y[min_y_pos] + y[max_x_pos] * x[min_y_pos] - (x[max_x_pos] * y[max_x_pos] + y[min_y_pos] * x[min_y_pos])
            sum2 = x[min_x_pos] * y[max_y_pos] + y[min_x_pos] * x[max_y_pos] - (x[min_x_pos] * y[min_x_pos] + x[max_y_pos] * y[max_y_pos])

            if (sum1 < sum2):
                swap(x, max_x_pos, min_y_pos)
            else: 
                swap(x, max_y_pos, min_x_pos)
            for i in range(0, len(x)):
                prod += x[i] * y[i]
            return prod

        swap(x, max_x_pos, min_y_pos)
        swap(x, max_y_pos, min_x_pos)
        for i in range(0, len(x)):
            prod += x[i] * y[i]
        return prod


T = int (input())

for i in range(0, T):
    v1 = []
    v2 = []    
    N = int(input())
    
    raw_input_v1 = input().split()
    raw_input_v2 = input().split()
    
    for j in range(0, N):
        v1.append(int(raw_input_v1[j]))
    
    for j in range(0, N):
        v2.append(int(raw_input_v2[j]))

    print("Case #" + str(i) + ":", swapped_prod(v1, v2))



