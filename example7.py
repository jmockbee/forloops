def validate_users(users):
    for user in users:
        if is_valid(user):
            print(user + " is valid")
        else:
            print(user + " is invalid")


validate_users(["purplecat"])


# the square brackets calls the function not the string
