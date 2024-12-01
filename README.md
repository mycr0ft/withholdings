# witholdings

## Federal Tax Withholdings

This python module is based based on Form W-4 and IRS Publication 15-T (2024) entitled [Federal
Income Tax Withholding Methods](https://www.irs.gov/publications/p15t#en_US_2024_publink100020274). 

## How to use it. 

Here we have a US Taxpayer who earns a gross monthly income (after non-taxable deductions) of $8,029.69. 
They are paid monthly. They have submitted to their employer a [Form W-4](https://www.irs.gov/pub/irs-pdf/fw4.pdf)
as required. They claim to have one dependent over 17 and are filing as Single with an extra job and have checked the box in Step 2(c).   

```py
import withholdings
W4 = withholdings.FormW4( filing_status = 'Single', step2c = True, number_of_other_dependents=1)
calc_with = withholdings.Withholdings( W4) 
withheld = calc_with.calc( 8029.69, 12)
agi = calc_with.calculateAGI( 8029.69, 12)
print( agi, withheld)
```

Should return the estimated adjusted gross income for the taxpayer, the amount of tax withholdings for the year 
and the amount per their paycheck. 

```py
96356.28 (17394.637199999997, 1449.5530999999999)
```

## The W-4 class

The following options are available to represent the Form W-4: 
```py
class FormW4(object):
    """Represents the data from a Form W-4 2020 or after"""
    def __init__( self, filing_status : str = "Single", 
                  step2c : bool = False,
                  number_of_qualifying_children_under_17: int = 0,
                  number_of_other_dependents : int = 0,
                  other_income : float = 0.0,
                  deductions : float = 0.0,
                  extra_withholding: float = 0.0 )
```
the following values are available for the `filing_status` for a taxpayer:
```py
filing_statuses = set( [ "Single", "Married filing seperately", "Married filing jointly", "Head of household" ])
```

## the Withholdings class

I use the method entitled Percentage Method Tables for Automated Payroll Systems and Withholding on Periodic Payments of Pensions and Annuities and have copied the rate tables and attempted to follow the method precisely. 

The withholdings class constructor takes a single parameter, a FormW4 object. 
```py
class Withholdings( object):
    """Finds the total withholdings from paychecks and per the withholdings tablees"""
    def __init__( self, W4 ):
```

We pass to the `calc` method only two parameters: 
```py
def calc( self,  total_wages_in_pay_period :float, 
                 number_of_pay_periods_per_year : int)
```

This returns the yearly withholding and the per-pay-period withholding. 


