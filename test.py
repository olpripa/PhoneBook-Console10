from utility import *

ph0 = Phone('09 5083 5767')
ph1 = Phone('098083 6767')
ph3 = Phone('098850 3797')
ph4 = Phone('099 555 66 88')
ph5 = Phone('098850 3797')
ph6 = Phone('098850 3797')
r = Record('Pripa Oleksandr', ph0, ph1)

print(ph5)
print(ph6)
r.addphone(ph3)
r.addphone(ph4)
r.addphone(ph5)
r.showphone()

# r.delphone(ph1)

r.editphone(ph4, '098083 9898wwww')
r.showphone()
