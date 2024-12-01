# witholdings

## Federal Tax Withholdings

This python module is based based on Form W-4 and IRS Publication 15-T (2024) entitled [Federal
Income Tax Withholding Methods](https://www.irs.gov/publications/p15t#en_US_2024_publink100020274). 

## How to use it. 

```py
import withholdings
W4 = withholdings.FormW4( filing_status = 'Single', step2c = True, number_of_other_dependents=1)
calc_with = withholdings.Withholdings( W4) 
withheld = calc_with.calc( 8029.69, 12)
agi = calc_with.calculateAGI( 8029.69, 12)
print( agi, withheld)
```

Should return

```py
96356.28 (17394.637199999997, 1449.5530999999999)
```

See test.py
