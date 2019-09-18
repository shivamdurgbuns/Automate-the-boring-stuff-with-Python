from getpass import getpass

while True:
    print('Who are you?')
    name=input()
    user=('Aman','aman','AMAN')
    if name not in user:
        continue
    print("Hello, Aman. What is your password?")
    password=getpass('Password:')
    if password == 'swordfish':
        break
    else:
        print("Wrong password. Try again.")
print("Access granted.")
