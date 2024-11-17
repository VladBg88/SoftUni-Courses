import re

number_of_planets = int(input())
decrypted_text = ""
destroyed_planets = {}
attacked_planets = {}

for planet in range(number_of_planets):
    text = input()
    key = int(len(re.sub(r"(?i)[^star]*", "", text)))
    decrypted_message = [chr(ord(x) - key) for x in text]
    decrypted_text = "".join(decrypted_message)

    pattern = r"@(?P<name>[A-Z-a-z]+)[^\@\,\-\!\:\>]*:(?P<population>\d+)[^\@\,\-\!\:\>]*!(?P<attack_type>A|D)![^\@\,\-\!\:\>]*->(?P<soldier_count>\d+)"
    matches = re.finditer(pattern, decrypted_text)
    if matches:
        for match in matches:
            name = match.group("name")
            population = int(match.group("population"))
            attack_type = match.group("attack_type")
            soldier_count = int(match.group("soldier_count"))

            if attack_type == "A":
                if name not in attacked_planets:
                    attacked_planets[name] = []
                attacked_planets[name].append(population)
                attacked_planets[name].append(soldier_count)
            elif attack_type == "D":
                if name not in destroyed_planets:
                    destroyed_planets[name] = []
                destroyed_planets[name].append(population)
                destroyed_planets[name].append(soldier_count)

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")
