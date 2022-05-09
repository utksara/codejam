def first_n_digit(x, n):
    p = 0
    while (x >= 1):
        x = x/10
    x = x*10
    
    digits = []

    for i in range(0, n):
        digits.append(int(x%10))
        x =x*10
    
    return digits

def number_of_digits(x):
    p = 0
    zeros = 0
    while (x >= 1):
        x = x/10
        zeros += 1
    return zeros

def append_sort(arr):
    total_digits = 0
    for i in range(0, len(arr)):
        if i > 0:
            if arr[i-1] >= arr[i]:
                diff = number_of_digits(arr[i-1]) - number_of_digits(arr[i])
                if diff == 0:
                    arr[i] *= 10
                    total_digits +=1
                else:
                    comparision_done = False
                    digits_i = first_n_digit(arr[i], number_of_digits(arr[i]))
                    digits_i_1 = first_n_digit(arr[i-1], number_of_digits(arr[i]))
                    for i_i in range(0, number_of_digits(arr[i])):
                        if digits_i_1[i_i] > digits_i[i_i]:
                            total_digits += diff + 1
                            arr[i] *= pow(10, diff+1)
                            comparision_done =True
                            
                            break
                        elif digits_i_1[i_i] < digits_i[i_i]:
                            total_digits += diff
                            arr[i] *= pow(10, diff)
                            comparision_done =True
                            
                            break

                    if comparision_done == False:
                        num_diff = arr[i-1] - arr[i]*pow(10, diff)
                        

                        if number_of_digits(num_diff+1) > diff:
                            total_digits += diff + 1
                            arr[i] *= pow(10, diff+1)
                        else:
                            total_digits += diff
                            arr[i] *= pow(10, diff)
                            arr[i] += num_diff + 1
        
    return total_digits

string_data = ''
N = int(input())

for i in range(1, N+1):
    m = int(input())
    arr = input().split(' ')
    for j in range(0,m):
        arr[j] = int(arr[j])
    data = append_sort(arr)
    print("Case #" + str(i) + ":", data)
    
#     string_data += "Case #"+ str(i) + ": " + str(data) + '\n'

# with open('doubleoutput.txt', 'a') as f:
#     f.write(string_data)