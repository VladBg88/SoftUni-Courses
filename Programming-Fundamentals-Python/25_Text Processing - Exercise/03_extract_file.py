line = input().split("\\")
line = line[-1:-2:-1]
filename, extension = line[0].split(".")

print(f"File name: {filename}")
print(f"File extension: {extension}")
