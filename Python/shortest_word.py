def find_short(s):
  s = s.lower()
  str_arr = s.split()

  min_length = 100000000
  for word in str_arr:
    if (len(word) < min_length):
      min_length = len(word)

  return min_length

print(find_short("bitcoin take over the world maybe who knows perhaps"))