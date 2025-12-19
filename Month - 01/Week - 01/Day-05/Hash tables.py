user = {"id": 1, "name": "admin"}

email = user.get("email", "No email found")

#iteration
for key, val in user.items():
    print(f"{key}: {val}")