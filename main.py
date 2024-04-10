def encoder(password):
    for num in password:
        if num <= 6:
            num += 3
        else:
            num -= 7
    return password