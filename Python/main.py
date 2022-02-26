''' Every digit squared

def square_digits(num):
  num = abs(num)
  result = ''
  
  while (num > 0):
    result = str((num % 10)**2) + result
    num //= 10
  return int(result) if result else 0

print(square_digits(int(input())))

'''

'''

def is_isogram(string):
  string = string.lower()
  word_alphabet = ""
  
  word_arr = list(string)
  
  for letter in word_arr:
    word_alphabet += letter
      
  for char in word_alphabet:
    if (word_alphabet.count(char) > 1):
      return False
  return True

print(is_isogram(str(input())))

'''

'''

def find_short(s):
  s = s.lower()
  str_arr = s.split()

  min_length = 100000000
  for word in str_arr:
    if (len(word) < min_length):
      min_length = len(word)

  return min_length

print(find_short("bitcoin take over the world maybe who knows perhaps"))

'''

'''

import math

def is_square(n):  
  if (n < 0): return False
  
  num_root = math.isqrt(n)

  if (num_root ** 2 == n):
    return True
  return False

print(is_square(int(input())))

'''

'''

# abc -> A-Bb-Ccc
def accum(string):
  string = string.lower()

  counter = 0
  new_string = ""

  for char in string: # abc
    counter += 1
    new_string = new_string + char.upper()
    for i in range(counter - 1):
      new_string = new_string + char.lower()
    if (counter < len(string)): new_string += '-'

  return new_string

print(accum("abc"))

'''

'''

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(word, ending):
  word_length = len(word)
  ending_length = len(ending)

  if (ending_length > word_length): return False

  free_chars = word_length - ending_length

  if (word[free_chars::] == ending): return True

  return False

print(solution('abcde', 'cde'))

'''

'''

def descending_order(num): # 143
  digits_array = [int(d) for d in str(num)] # [1, 4, 3]

  digits_array.sort(reverse=True)

  result = ""

  for number in range(len(digits_array)):
    result += str(digits_array[number])

  return int(result)

print(descending_order(0))

'''

'''

# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

def alphabet_position(text):
  text = text.lower()

  alphabet = "abcdefghijklmnopqrstuvwxyz"

  result = ""

  for char in text:
    if char in alphabet:
      result += str(alphabet.find(char)+1)
      result += " "
    else: 
      result += ""
    
  return result.strip()

print(alphabet_position("The sunset sets at twelve o' clock."))

'''

'''

def solution(s):
  main_list = []

  result_string = ""

  if len(s) % 2 != 0:
    s += "_"

  for i in range(0, len(s), 2):
    main_list.append(s[i:(i + 2)])

  return main_list

print(solution("abc"))

'''

'''

def likes(names): # array
  if (len(names) == 0): return "no one likes this"

  if (len(names) == 1): return f"{names[0]} likes this"

  if (len(names) >= 1 and len(names) <= 2):
    return f"{names[0]} and {names[1]} like this"

  if (len(names) == 3): return f"{names[0]}, {names[1]} and {names[2]} like this"

  if (len(names) > 3):
    return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

print(likes(["Alex", "Jacob", "Mark", "Max"]))

'''

'''

def duplicate_encode(word):

  result_string = ""
  
  for char in word.lower():
    if (word.lower().count(char) == 1): 
      result_string = result_string + "("
    elif (word.lower().count(char) > 1):
      result_string = result_string + ")"

  return result_string

print(duplicate_encode("dtring"))

'''

'''

def increment_string(s):

  stripped_chars = s.rstrip('1234567890')
  digits = s[len(stripped_chars):]
  
  if len(digits) == 0:
    return s + '1'
  else:
    length = len(digits)

    new_digits = 1 + int(digits)
    new_digits = str(new_digits).zfill(length)

    return stripped_chars + new_digits
    
print(increment_string("foo09"))

'''

'''

def find_missing_letter(chars): # list a, b, c, d, f

  alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
  
  main_string = ""

  alphabet = ""
          
  for s in chars:
    main_string += s

  if (alphabet_upper.count(main_string[0]) != 0):
    alphabet = alphabet_upper
  else:
    alphabet = alphabet_lower

  print(alphabet)
  start_index = alphabet.find(main_string[0])
  print(f"Start index in alphabet is {start_index}")
  
  for i in range(start_index, len(main_string)+start_index):
    if ((main_string[i-start_index] == alphabet[i]) and (main_string[i-start_index+1] == alphabet[i+1])):
      print("Едем дальше")
      continue
    else:
      return alphabet[i+1]

print(find_missing_letter(['O','Q','R','S']))

'''

'''

import math

def is_prime(num):

  if (num < 0 or num == 0 or num == 1): return False
  
  counter = 0

  for i in range(1, int(math.sqrt(num)) + 1):
    if (num % i == 0):
      counter += 1
    else:
      continue

  if (counter == 1): return True

  return False

print(is_prime(2))

'''

'''

def meeting(s):
  s_list = s.split(";")
  
  persons_result = []
  
  for i in range(0, len(s_list)): # element: Name:Surname
    
    s_list_person = s_list[i].split(":")
    s_list_person.reverse()
    result_person_list = ", ".join(s_list_person)
    persons_result.append("(" + result_person_list.upper() + ")")

  result_string = ""

  for el in sorted(persons_result):
    result_string += el

  return result_string

print(meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn"))

'(ARNO, ANN)(BELL, JOHN)(CORNWELL, ALEX)(DORNY, ABBA)(KERN, LEWIS)(KORN, ALEX)(META, GRACE)(SCHWARZ, VICTORIA)(STAN, MADISON)(STAN, MEGAN)(WAHL, ALEXIS)'

'''

'''

def tower_builder(floors):
  
  result_list = []
  line_width = (floors * 2) - 1
  
  for i in range(1, 2 * floors, 2):
    stars = "*" * i
    line = stars.center(line_width)
    result_list.append(line)
  
  print(*result_list, sep = "\n")

  return result_list

print(tower_builder(110))

'''

'''

def vowel_indices(word):
  word = word.lower()
  
  vowels = ["a", "e", "i", "o", "u", "y"]
  
  result_list = []

  for i, j in enumerate(word):
    if j in vowels or j in [k for k in vowels]:
      result_list.append(i + 1)

  return result_list

print(vowel_indices("Wordo"))

'''

'''

def reverse_letter(string):
  string = string.lower()
  
  alphabet = "abcdefghijklmnopqrstuvwxyz"

  temp_string = ""

  for char in string:
    if (char in alphabet):
      temp_string = char + temp_string
    else:
      continue

  return temp_string

print(reverse_letter("Ahahsfaf"))

'''

'''

def calculator(txt):
  operand = 0
    
  if ("+" in txt): 
    txt_list = txt.split("+")
    operand = 1
  if ("-" in txt): 
    txt_list = txt.split("-")
    operand = 2
  if ("*" in txt): 
    txt_list = txt.split("*")
    operand = 3
  if ("//" in txt): 
    txt_list = txt.split("//")
    operand = 4
    
  left_dots = txt_list[0].count(".")
  right_dots = txt_list[1].count(".")

  if (operand == 1): return "." * (left_dots + right_dots)
  if (operand == 2): return "." * (left_dots - right_dots)
  if (operand == 3): return "." * (left_dots * right_dots)
  if (operand == 4): return "." * (left_dots // right_dots)
    
print(calculator("..... // ."))

'''