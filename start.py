from utility import *


def ab_start():
    ph0 = Phone('09 5083 5767')
    ph1 = Phone('098083 6767')
    ph2 = Phone('098850 3797')
    ph3 = Phone('099 555 66 88')
    ph4 = Phone('098850 3797')
    ph5 = Phone('098850 3797')
    r0 = Record('Pripa Oleksandr', ph0)
    r0.addphone(ph1)
    r0.addphone(ph2)
    r1 = Record('Pripa Y', ph3)
    r1.addphone(ph4)
    r1.addphone(ph5)
    ab = AdressBook()
    ab.add(r0)
    ab.add(r1)
    return (ab)
   
ab_start()