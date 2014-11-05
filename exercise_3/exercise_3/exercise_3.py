### payment calculator ###
def inp_to_float(X):
    res = float(X)
    return res

whileile True:
    inp = raw_input("Enter hours: ")
    try:
        Hours = float(inp)
        continue
    except:
        print "ERROR: value must be numeric, try again"
        inp = raw_input("Enter hours: ")
        Hours = float(inp)
        #if type(Hours) == float: continue

inp = raw_input("Enter rate: ")
try:
    Rate = float(inp)
except:
    print "ERROR: value must be numeric, try again"
    inp = raw_input("Enter rate: ")
    Rate = float(inp)


print "Pay must be: ", 40 * Rate + (Rate * 1.5 * (Hours - 40))