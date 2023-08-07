'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import Decimal # For the rounding error

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

MAX_ITEM_AMOUNT = 100_000
# TESTS and HACK are solved, but added the following after checking the solution:
MAX_NET = 1e+9
MAX_QUANTITY = 100

def validorder(order: Order):
    net = Decimal('0')
    
    for item in order.items:
        if item.type == 'payment':
            if -1*MAX_ITEM_AMOUNT < item.amount < MAX_ITEM_AMOUNT:
                net += Decimal(str(item.amount))
        elif item.type == 'product':
            # Solved, but added ifs after checking the solution
            if 0 < item.quantity <= MAX_QUANTITY and 0 < item.amount < MAX_ITEM_AMOUNT:
                net -= Decimal(str(item.amount)) * item.quantity
            if MAX_NET < net < -1*MAX_NET:
                return("Total amount exceeded")
        else:
            return("Invalid item type: %s" % item.type)
    
    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
