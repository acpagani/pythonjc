dict = {
    "name": 2,
    "job": 3,
    "phone": None}

for data in dict.values():
    print(data)
    if data is None:
        print("eita".capitalize())
