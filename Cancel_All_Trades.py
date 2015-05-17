import Cryptsy
import time

PublicKey = ''
PrivateKey = ''
        
print "Cancelling all trades."
print "  Sleeping 10 sec. (abort possible)"

time.sleep(10)

print "Cancelling trades."

exchange = Cryptsy.Api(PublicKey, PrivateKey)

result = exchange.cancel_all_orders()

try:

    for entry in result['return']:
        
        print str(entry)
        
except Exception as e:
    
    print "No orders to cancel."
    
    print "Success : " + str(result['success'])
    
print "Completed."