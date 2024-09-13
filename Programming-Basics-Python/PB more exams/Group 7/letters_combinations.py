start_letter = str(input())
end_letter = str(input())
skip_letter = str(input())
counter = 0

for i in range(ord(start_letter), ord(end_letter) + 1):
    if i == ord(skip_letter):
        continue

    for k in range(ord(start_letter), ord(end_letter) + 1):
        if k == ord(skip_letter):
            continue

        for j in range(ord(start_letter), ord(end_letter) + 1):
            if j == ord(skip_letter):
                continue

            print(chr(i) + chr(k) + chr(j), end=' ')
            counter += 1

print(counter)
