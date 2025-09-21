# Character sets
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()"

all_chars = letters + digits + symbols

length = int(input("Enter password length: "))

# A very simple pseudo-random generator
password = ""
seed = length * 7 + 3  # simple seed

for i in range(length):
    seed = (seed * 3 + i * 5) % len(all_chars)
    password += all_chars[seed]

print("Generated password:", password)
 
