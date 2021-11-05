while True:
    e_mail = str(input("Enter your e-mail: "))
    x="@" in e_mail
    y="." in e_mail
    if(x,y)==(True,True):
        print("Your e-mail is valid.")
        break
    else:
        print("Please enter a valid e-mail.")