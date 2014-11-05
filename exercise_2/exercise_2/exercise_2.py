#################################################################
inp = raw_input("Enter hours: ")
try:
    H = float(inp)
except:
    print "ERROR: value must be numeric, try again"
    inp = raw_input("Enter hours: ")
    H = float(inp)
#################################################################
inp = raw_input("Enter rate: ")
try:
    R = float(inp)
except:
    print "ERROR: value must be numeric, try again"
    inp = raw_input("Enter rate: ")
    R = float(inp)
#################################################################

print "Pay must be: ", 40 * R + (R * 1.5 * (H - 40))