N = list(map(int, input()))

half_len = int(len(N)/2)

front_score = sum(N[:half_len])
back_score = sum(N[half_len:])

if front_score == back_score:
  print("LUCKY")
else:
  print("READY")