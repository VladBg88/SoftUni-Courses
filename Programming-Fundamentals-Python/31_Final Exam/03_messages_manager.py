messages_capacity_per_user = int(input())
users = {}


while True:
    command = input()
    if command == "Statistics":
        break

    command = command.split('=')
    action = command[0]

    if action == 'Add':
        username = command[1]
        sent_messages = int(command[2])
        received_messages = int(command[3])
        if username not in users:
            users[username] = {'sent_messages': sent_messages, 'received_messages': received_messages}
    elif action == "Message":
        sender = command[1]
        receiver = command[2]
        if sender in users and receiver in users:
            users[sender]['sent_messages'] += 1
            users[receiver]['received_messages'] += 1
            if users[sender]['sent_messages'] + users[sender]['received_messages'] >= messages_capacity_per_user:
                print(f"{sender} reached the capacity!")
                del users[sender]
            if users[receiver]['sent_messages'] + users[receiver]['received_messages'] >= messages_capacity_per_user:
                print(f"{receiver} reached the capacity!")
                del users[receiver]
    elif action == "Empty":
        username = command[1]
        if username in users:
            del users[username]
        if username == 'All':
            users.clear()

print(f"Users count: {len(users)}")
for user, data in users.items():
    print(f"{user} - {data['sent_messages'] + data['received_messages']}")
