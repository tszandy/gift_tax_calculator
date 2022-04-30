value = 243700


tax_bracket = [
    (0      ,     0,0.18),
    (10000  ,  1800, 0.2),
    (20000  ,  3800,0.22),
    (40000  ,  8200,0.24),
    (60000  , 13000,0.26),
    (80000  , 18200,0.28),
    (100000 , 23800, 0.3),
    (150000 , 38800,0.32),
    (250000 , 70800,0.34),
    (500000 ,155800,0.37),
    (750000 ,248300,0.39),
    (1000000,345800, 0.4)
]

for tax_value,tax_under_thread_hold_tax,tax_percent in tax_bracket[::-1]:
    if value >= tax_value:
        print("tax amount: {}".format(tax_under_thread_hold_tax+tax_percent*(value-tax_value)))
        break
