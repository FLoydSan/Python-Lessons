print " -= Welcome to currency exchanger =-"
print ""
user_exit = 0

while user_exit != 'q':
    print ""
    print "Type 1 if you want to change UAH to USD"
    print "Type 2 if you want to change UAH to EUR"
    print "Type 3 if you want to change UAH to RUB"
    print "Type 4 if you want to change USD to UAH"
    print "Type 5 if you want to change EUR to UAH"
    print "Type 6 if you want to change RUB to UAH"
    print ""
    inp = raw_input("Your choice: ")
    try:
        choice = int(inp)
    except:
        inp = raw_input("Your were wrong, try it again: ")
        choice = int(inp)

    if choice == 1:
        inp = raw_input("Input your UAH amount here: ")
        try:
            uah = float(inp)
        except:
            inp = raw_input("ERROR: Value must be numeric, try again: ")
            uah = float(inp)
        print "You have ", uah / 12.9555495, "USD"
        user_exit = raw_input("Type q for exit program or any key to start again: ")

    if choice == 2:
        inp = raw_input("Input your UAH amount here: ")
        try:
            uah = float(inp)
        except:
            inp = raw_input("ERROR: Value must be numeric, try again: ")
            uah = float(inp)
        print "You have ", uah / 16.2255302, "EUR"
        user_exit = raw_input("Type q for exit program or any key to start again: ")
       
    if choice == 3:
        inp = raw_input("Input your UAH amount here: ")
        try:
            uah = float(inp)
        except:
            inp = raw_input("ERROR: Value must be numeric, try again: ")
            uah = float(inp)
        print "You have ", uah / 16.2255302, "EUR"
        user_exit = raw_input("Type q for exit program or any key to start again: ")

    if choice == 4:
        inp = raw_input("Input your USD amount here: ")
        try:
            usd = float(inp)
        except:
            inp = raw_input("ERROR: Value must be numeric, try again: ")
            usd = float(inp)
        print "You have ", usd * 12.9555495, "UAH"
        user_exit = raw_input("Type q for exit program or any key to start again: ")

    if choice == 5:
        inp = raw_input("Input your EUR amount here: ")
        try:
            eur = float(inp)
        except:
            print "ERROR: Value must be numeric, try again: "
            eur = float(inp)
        print "You have ", eur * 16.2255302, "UAH"
        user_exit = raw_input("Type q for exit program or any key to start again: ")

    if choice == 6:
        inp = raw_input("Input your RUB amount here: ")
        try:
            rub = float(inp)
        except:
            print "ERROR: Value must be numeric, try again: "
            rub = float(inp)
        print "You have ", rub * 16.2255302, "UAH"
        user_exit = raw_input("Type 'q' to quit program or press 'ENTER' to start again")
