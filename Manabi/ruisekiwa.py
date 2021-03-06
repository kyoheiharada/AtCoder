import numpy as np

N, K = map(int, input().split())
E = list(map(int, input().split()))
res = np.cumsum(E)

ans = res[K - 1]
for i in range(K, N):
    if ans < res[i] - res[i - K]:
        ans = res[i] - res[i - K]
print(ans)
