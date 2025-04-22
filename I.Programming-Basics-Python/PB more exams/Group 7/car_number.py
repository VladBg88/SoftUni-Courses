start = int(input())
end = int(input())

for i in range(start, end + 1):
    for j in range(start, end + 1):
        for k in range(start, end + 1):
            for l in range(start, end + 1):

                if i % 2 == 0:
                    if l % 2 != 0:
                        if i > l:
                            if (j + k) % 2 == 0:
                                print(f'{i}{j}{k}{l}', end=' ')
                else:
                    if i % 2 != 0:
                        if l % 2 == 0:
                            if i > l:
                                if (j + k) % 2 == 0:
                                    print(f'{i}{j}{k}{l}', end=' ')
