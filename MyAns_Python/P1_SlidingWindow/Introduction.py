'''
'''
# Brute-Force Algorithms
def find_averages_of_subarrays_bf(K, arr):
    result = []
    for i in range(len(arr)-K+1):
        sum = 0.0
        for j in range(i, i+K):
            sum += arr[j]
        result.append(sum/K)
    return result

def main_bf():
    result = find_averages_of_subarrays_bf(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

main_bf()


# 
def find_averages_of_subarrays_sw(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K+1:
            result.append(windowSum/K)
            windowSum -= arr(windowStart)
            windowStart += 1
    
    return result

def main_sw():
    result = find_averages_of_subarrays_sw(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

main_sw()