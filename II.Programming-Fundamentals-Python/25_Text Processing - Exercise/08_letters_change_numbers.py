line = input().split()
line = [word.strip() for word in line]
total_sum = 0

for word in line:
    number = int(word[1:-1])
    first_letter = word[0]
    last_letter = word[-1]

    if first_letter.isupper():
        number /= (ord(first_letter) - 64)
    elif first_letter.islower():
        number *= (ord(first_letter) - 96)

    if last_letter.isupper():
        number -= (ord(last_letter) - 64)
    elif last_letter.islower():
        number += (ord(last_letter) - 96)

    total_sum += number

print(f"{total_sum:.2f}")
