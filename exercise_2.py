while True:
    e_mail = str(input("Enter your e-mail: "))
    if not '@' in e_mail:
        validity = False
    if not '.' in e_mail:
        validity = False
    else:
        validity = True
    if validity is True:
        print("Your e mail is valid")
        break
    else:
        print("Your e-mail is not valid")