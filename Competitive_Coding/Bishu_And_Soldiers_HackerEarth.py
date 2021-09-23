# Problem: https://www.hackerearth.com/problem/algorithm/bishu-and-soldiers-227/

def fight(soldier_arr,max_bishu_power):
    soldier_hash = {i:0 for i in soldier_arr}
    for i in soldier_arr:
        soldier_hash[i] += 1
    sorted_soldier_hash = {k:v for k,v in sorted(soldier_hash.items(), key = lambda item:item[0])}
    soldier_keys = list(sorted_soldier_hash.keys())
    
    # Memo Table for Results
    memo_table = {i:[0,0] for i in range(1,max_bishu_power+1)}

    defeated_soldiers_count = 0
    defeated_soldiers_power = 0
    # Initiaization
    for i in range(1,max_bishu_power+1):
        if i==1:
            for j in soldier_keys:
                if j <= 1:
                    defeated_soldiers_count += sorted_soldier_hash[j]
                    defeated_soldiers_power += (j*sorted_soldier_hash[j])
                    memo_table[i] = [defeated_soldiers_count,defeated_soldiers_power]
        else:
            if i <= max(soldier_keys):
                for j in soldier_keys:
                    if j <= i:
                        count = memo_table[i-1][0] + sorted_soldier_hash[j]
                        power = memo_table[i-1][1] + j*sorted_soldier_hash[j]
                        memo_table[i] = [count,power]
            else:
                memo_table[i] = [memo_table[i-1][0],memo_table[i-1][1]]
    return memo_table

# Inputs
N = int(input())
soldier_arr = []
for i in range(N):
    soldier_arr.append(int(input()))
Q = int(input())
bishu_power_arr = []
for i in range(Q):
    bishu_power_arr.append(int(input()))

# Execution
result = fight(soldier_arr,max(bishu_power_arr))

# Result
for i in bishu_power_arr:
    print(result[i][0],result[i][1])
