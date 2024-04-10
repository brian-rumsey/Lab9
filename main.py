def encoder(password):
    for num in password:
        if num <= 6:
            num += 3
        else:
            num -= 7
    return password

def decoder(encrypted_password):
    for num in encrypted_password:
        if num > 2:
            num -= 3
        else:
            num += 7
    return encrypted_password