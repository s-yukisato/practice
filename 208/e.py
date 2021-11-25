
def calc(N, K):
  dp = [[0] * N for _ in range(N)]
  eq = [0] * N
  eq[0] = 1
  for i in range(1, len(str(N)) + 1):
    # Nのi桁目をdigitとする
    digit = i
    # (1) less -> less
    # i-1桁目までがNのi-1桁目までと比べて小さい場合
    # i桁目の数dは0以上9以下がOK
    for p in range(0, i):
      for d in range(0, 10):
        dp[i + 1][p * d] += dp[i][p]
    # (2) equal -> less
    #  i-1桁目までがNと同じで、かつi桁目がNのi桁目より小さい場合
    # i桁目の数dは0以上digit未満がOK
    for d in range(0, digit):
      # i = 0 かつ d = 0 の時は全体が0になってしまうため除外
      if i == 0 and d == 0:
        continue
      dp[i + 1][eq[i] * d] += 1
    # (3) equal -> equal
    # i桁目までNと一致する時
    # i桁目の数はdigit
    eq[i + 1] = eq[i] * digit
    # (4) 0...0d 型
    # i-1桁目までが0でi桁目が0以外の時
    # i桁目の数dは1以上9以下がOK
    # (d = 0の時は全体が0になってしまうため除外)
    for d in range(1, 10):
      # i = 0 の場合は(2)ですでにカウントしている
      if i == 0:
        continue
      dp[i + 1][d] += 1
  answer =  0

  for p in range(0, len(dp[len(str(N))])):
    if p <= K:
      answer += dp[len(str(N))][p]
  if eq[len(str(N))] <= K:
    answer += 1
  return answer


N, K = map(int, input().split())
ans = calc(N, K)

print(ans)