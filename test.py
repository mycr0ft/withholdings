import withholdings
W4 = withholdings.FormW4( filing_status = 'Married filing jointly', step2c = False, number_of_other_dependents=1)
calc_with = withholdings.Withholdings( W4) 
withheld = calc_with.calc( 7029.69, 12) 
print( "yearly withholdings       = $ {0:4.2f}".format( withheld[0]))
print( "per paycheck withholdings = $ {0:4.2f}".format( withheld[1]))
