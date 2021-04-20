PH = float(input('digite um valor do PH: '))
if PH < 7.0:
    print('solução ácida')
elif PH == 7.0:
    print('solução neutra')
else:
    print('solução básica')