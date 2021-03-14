def rotationalCipher(str_in, rotation_factor):
"""Code to return a rotational cipher.""" 
  out = ''
  for i in str_in:
    if i.isupper():
      out += chr((ord(i) + rotation_factor - ord('A')) % 26 + ord('A'))
    elif i.islower():
      out += chr((ord(i) + rotation_factor - ord('a')) % 26 + ord('a'))
    elif i.isnumeric():
      out += chr((ord(i) + rotation_factor - ord('0')) % 10 + ord('0'))
    else:
      out += i

  return out

# Example:
input_1 = "All-convoYs-9-be:Alert1."
rotation_factor_1 = 4

# should return "Epp-gsrzsCw-3-fi:Epivx5."
rotationalCipher(input_1, rotation_factor_1)