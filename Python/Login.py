def login():
  attempts = 3
  while attempts > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username == "Admin" and password == "Admin":
      print(f"Welcome, {username}!")
      return  # Exit the function if login is successful

    attempts -= 1
    if attempts > 0:
        print(f"Incorrect username or password. You have {attempts} attempts remaining.")
    else:
        print("Too many incorrect login attempts.")

# Example usage (you can remove this part if you only want the function definition)
login()
