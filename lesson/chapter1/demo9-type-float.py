#type of float

print(3.14,type(3.14))

print(1.1+2.1)
print(1.1+2.2) #得3.3000000000000003 , float計算可能有誤

from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))  #導人 decimal , 得3.3正確