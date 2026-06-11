password=input("Enter your password: ")
has_uppercase=False
has_lowercase=False
has_digit=False
has_special=False
for char in password:
    if char.isupper():
        has_uppercase=True
    elif char.islower():
        has_lowercase=True
    elif char.isdigit():
        has_digit=True
    elif not char.isalnum():
        has_special=True
score=0
if len(password)>=8:
    score+=1
if has_uppercase:
    score+=1
if has_lowercase:
    score+=1
if has_digit:
    score+=1
if has_special:
    score+=1
print("password Analizer")
print("--------------------")
print(f"password: {password}")
print(f"length>= 8: {len(password)>=8}")
print(f"has uppercase: {has_uppercase}")
print(f"has lowercase: {has_lowercase}")
print(f"has digit: {has_digit}")
print(f"has special character: {has_special}")
if score==4:
    print("password strength: strong")
elif score>=3:
    print("password strength: medium")
else :
    print("password strength: weak")
    