inp = raw_input("Enter hours: ")
try:
    hours = float(inp)
except:
    print "ERROR: value must be a number, try again"
    inp = raw_input("Enter hours: ")
    hours = float(inp)

inp = raw_input("Enter rate: ")
try:
    rate = float(inp)
except:
    print "ERROR: value must be a number, try again"
    inp = raw_input("Enter rate: ")
    rate = float(inp)

inp = raw_input("Enter overtime: ")
try:
    over = float(inp)
except:
    print "ERROR: value must be a number, try again"
    inp = raw_input("Enter overtime: ")
    over = float(inp)

over_rate = rate * 1.5

pay = (hours * rate) + (over * over_rate)
print "Pay must be: ", pay
