### payment calculator ###
def inp_to_float(X):
    res = float(X)
    return res

def computepay(h, r):
    p = 40 * Rate + (r * 1.5 * (h - 40))
    return p

inp = raw_input("Enter hours: ")
try:
    Hours = float(inp)
except:
    print "ERROR: value must be numeric, try again"
    inp = raw_input("Enter hours: ")
    Hours = float(inp)

inp = raw_input("Enter rate: ")
try:
    Rate = float(inp)
except:
    print "ERROR: value must be numeric, try again"
    inp = raw_input("Enter rate: ")
    Rate = float(inp)


print "Pay must be: ", computepay(Hours, Rate)