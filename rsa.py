import math

def generate_keys(bits): # key size in bits (for number generation)
  # We take some sample numbers or generate them at random and check them using the primality test
  p=104729
  q=1299709
  n = p*q
  phi = (p-1)*(q-1) # Euler's function for n
  e = 65537
  assert math.gcd(e, phi) == 1 # relatively prime numbers
  d = pow(e, -1, phi) # modular inverse of e
  return ((n, e), (n, d))

def encryption(message, public_key):
  n, e = public_key
  c = pow(message, e, n)
  return c

def decryption(ciphertext, private_key):
  n, d = private_key
  message = pow(ciphertext, d, n)
  return message

def str_to_int(txt):
  bites = txt.encode('utf-8')
  return int.from_bytes(bites, byteorder='big')

def int_to_str(num):
  bites_len = (num.bit_length() + 7) // 8
  bites = num.to_bytes(bites_len, byteorder='big')
  return bites.decode('utf-8')

def RSA(message, action, key, is_text=False):

  match action:
    case 'encrypt':
      if is_text:
        return encryption(str_to_int(message), key)
      else:
        return encryption(message, key)
    case 'decrypt':
      if is_text:
        return int_to_str(decryption(message, key))
      else:
        return decryption(message, key)
    case _:
      print("Action not found")
      return

keys = generate_keys(1024)
message = "kot"

encrypted = RSA(message, 'encrypt', keys[0], True)
print(encrypted)

decrypted = RSA(encrypted, 'decrypt', keys[1], True)
print(decrypted)
