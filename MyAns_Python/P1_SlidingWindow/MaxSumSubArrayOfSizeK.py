# Jimmy的答案
def max_sub_array_of_size_k_jimmy(k, arr):
    max = 0
    #result = []
    for i in range(len(arr)-k+1):
        sum = 0
        #temp = []
        for j in range(i, i+k):
            sum += arr[j]
            #temp.apped(j)
            if sum > max:
                max = sum
                #result = temp
    return max

def main_jimmy():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k_jimmy(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k_jimmy(2, [2, 3, 4, 1, 5])))

main_jimmy()



#Brute Force 的标准答案
def max_sub_array_of_size_k_bf(k, arr):
    max_sum = 0
    window_sum = 0
    for i in range(len(arr)-k+1):
        for j in range(i, i+k):
            window_sum += arr[j]
        max_sum = max(window_sum, max_sum)
    return max_sum



#Sliding Window 的标准答案
def max_sub_array_of_size_k_sw(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum

def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k_sw(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k_sw(2, [2, 3, 4, 1, 5])))


main()


