def LCS_LENGTH(m, n):
    x = len(m)
    y = len(n)

    dp = [[0 for j in range(y + 1)] for i in range(x + 1)]

    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if m[i - 1] == n[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[x][y], dp


def BUILD_LCS(m, n, dp):
    i = len(m)
    j = len(n)

    result = []

    while i > 0 and j > 0:
        if m[i - 1] == n[j - 1]:
            result.insert(0, m[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1

        else:
            j -= 1

    return ''.join(result)


# Name and surname
m = "ANUSHKA"
n = "PATIL"

length, dp = LCS_LENGTH(m, n)
lcs = BUILD_LCS(m, n, dp)

print("Name:", m)
print("Surname:", n)
print("Length of LCS:", length)
print("LCS:", lcs)
