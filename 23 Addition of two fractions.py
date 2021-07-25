a = int(input('Enter the numerator for 1st fraction :'))
b = int(input('Enter the denominator for the 1st fraction :'))
c = int(input('Enter the numerator for 2nd fraction :'))
d = int(input('Enter the denominator for the 2nd fraction :'))
if(b==d):
    Fraction =a+c
    print('Addition of two fractions are :' + str(Fraction) + '/' + str(b))
else:
    #to find the sum
    #denominators should be same
    #apply cross Multiplication
    Fraction = (a*d) + (c*b)
    print('Addition of fractions are :' + str(Fraction) + '/' + str(b *d))