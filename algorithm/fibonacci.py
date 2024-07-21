'''
斐波那契数：
F(n) = 1 (n = 0, 1)
F(n) = F(n - 1) + F(n - 2) (n > 2)
'''

# 递归解法
def recursion(n):
    if n < 2:
        return 1
    else:
        return recursion(n - 1) + recursion(n - 2)
    

# 动态规划
# 使用一个数组存放子问题的答案，以空间换时间
def dp(n):
    res_list = [1, 1]
    for i in range(2, n):
        res = res_list[i -1] + res_list[i - 2]
        res_list.append(res)
    return res_list[n - 1]

print(dp(5))