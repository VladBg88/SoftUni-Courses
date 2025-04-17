n, m = input().split()
n_collection = set()
m_collection = set()

for _ in range(int(n)):
    n_collection.add(input())

for _ in range(int(m)):
    m_collection.add(input())

result = n_collection & m_collection
for num in result:
    print(num)
