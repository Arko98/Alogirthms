def solve(input1, input2, input3):
    memo = [0]*(10**5)
    sum_val = 0
    for i in range(input1):
        memo[i] += sum_val + input2[i]
        sum_val += input2[i] 

    def choose(array, start, end):
        if (start >= end):
            return 0
        else:
            ans = 10**8
            for j in range(start,end):
                sum1 = memo[j] - memo[start] + array[start]
                sum2 = memo[end] - memo[j+1] + array[j+1]
                temp_val = choose(array, start, j) + choose(array, j+1, end) + (sum1 + sum2)*input3
                ans = min(temp_val, ans)
            return ans
    return choose(input2, 0, input1-1)