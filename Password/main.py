import random
import string
length = 8
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
print('The password is:', password)