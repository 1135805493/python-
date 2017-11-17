def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
    print "ok"
    

try:
    functionName(3)                
except "Invalid level!":
    print 1
else:
    print 2
finally:
    print 3    
