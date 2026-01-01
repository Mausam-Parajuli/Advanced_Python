def auth(password):
    value = False
    a,b,c = False,False,False
    if len(password) > 8:
        a = True
    for i in password:
        if i.isupper():
            b = True
        if i.isnumeric():
            c = True
    value = a and b and c
    if value:
        print("Password accepted")
    else:
        print("Password not accepted")
word = "Whatever123"
auth(word)