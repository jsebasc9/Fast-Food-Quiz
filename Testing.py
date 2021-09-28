users = ["Test User", "Real User 1", "Real User 2","Test User", "Real User 2"]
for index, user in enumerate(users):
    if index == 0:
        print("Extra verbose output for:", user)
    print(user)