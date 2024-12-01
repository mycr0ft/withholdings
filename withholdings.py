filing_statuses = set( [ "Single", "Married filing seperately", "Married filing jointly", "Head of household" ])

class FormW4(object):
    """Represents the data from a Form W-4 2020 or after"""
    def __init__( self, filing_status : str = "Single", 
                  step2c : bool = False,
                  number_of_qualifying_children_under_17: int = 0,
                  number_of_other_dependents : int = 0,
                  other_income : float = 0.0,
                  deductions : float = 0.0,
                  extra_withholding: float = 0.0 ):
        
        if filing_status in filing_statuses:
            self.filing_status = filing_status
        else:
            raise Exception( 'invalid filing status')
        self.step2c = step2c
        self.other_income = other_income
        self.deductions = deductions
        self.extra_withholding = extra_withholding
        self.number_of_qualifying_children_under_17 = number_of_qualifying_children_under_17
        self.number_of_other_dependents = number_of_other_dependents 
        return
    
    @property
    def line3( self) -> float:
        return self.number_of_qualifying_children_under_17*2000 + self.number_of_other_dependents*500

withholding_tables = {'Single': {False: [{'A': 0.0, 'B': 6000.0, 'C': 0.0, 'D': 0.0, 'E': 0.0},
   {'A': 6000.0, 'B': 17600.0, 'C': 0.0, 'D': 10.0, 'E': 6000.0},
   {'A': 17600.0, 'B': 53150.0, 'C': 1160.0, 'D': 12.0, 'E': 17600.0},
   {'A': 53150.0, 'B': 106525.0, 'C': 5426.0, 'D': 22.0, 'E': 53150.0},
   {'A': 106525.0, 'B': 197950.0, 'C': 17168.5, 'D': 24.0, 'E': 106525.0},
   {'A': 197950.0, 'B': 249725.0, 'C': 39110.5, 'D': 32.0, 'E': 197950.0},
   {'A': 249725.0, 'B': 615350.0, 'C': 55678.5, 'D': 35.0, 'E': 249725.0},
   {'A': 615350.0, 'B': '', 'C': 183647.25, 'D': 37.0, 'E': 615350.0}],
  True: [{'A': 0.0, 'B': 7300.0, 'C': 0.0, 'D': 0.0, 'E': 0.0},
   {'A': 7300.0, 'B': 13100.0, 'C': 0.0, 'D': 10.0, 'E': 7300.0},
   {'A': 13100.0, 'B': 30875.0, 'C': 580.0, 'D': 12.0, 'E': 13100.0},
   {'A': 30875.0, 'B': 57563.0, 'C': 2713.0, 'D': 22.0, 'E': 30875.0},
   {'A': 57563.0, 'B': 103275.0, 'C': 8584.25, 'D': 24.0, 'E': 57563.0},
   {'A': 103275.0, 'B': 129163.0, 'C': 19555.25, 'D': 32.0, 'E': 103275.0},
   {'A': 129163.0, 'B': 311975.0, 'C': 27839.25, 'D': 35.0, 'E': 129163.0},
   {'A': 311975.0, 'B': '', 'C': 91823.63, 'D': 37.0, 'E': 311975.0}]},
 'Married filing seperately': {False: [{'A': 0.0,
    'B': 6000.0,  'C': 0.0,  'D': 0.0, 'E': 0.0},
   {'A': 6000.0, 'B': 17600.0, 'C': 0.0, 'D': 10.0, 'E': 6000.0},
   {'A': 17600.0, 'B': 53150.0, 'C': 1160.0, 'D': 12.0, 'E': 17600.0},
   {'A': 53150.0, 'B': 106525.0, 'C': 5426.0, 'D': 22.0, 'E': 53150.0},
   {'A': 106525.0, 'B': 197950.0, 'C': 17168.5, 'D': 24.0, 'E': 106525.0},
   {'A': 197950.0, 'B': 249725.0, 'C': 39110.5, 'D': 32.0, 'E': 197950.0},
   {'A': 249725.0, 'B': 615350.0, 'C': 55678.5, 'D': 35.0, 'E': 249725.0},
   {'A': 615350.0, 'B': '', 'C': 183647.25, 'D': 37.0, 'E': 615350.0}],
  True: [{'A': 0.0, 'B': 7300.0, 'C': 0.0, 'D': 0.0, 'E': 0.0},
   {'A': 7300.0, 'B': 13100.0, 'C': 0.0, 'D': 10.0, 'E': 7300.0},
   {'A': 13100.0, 'B': 30875.0, 'C': 580.0, 'D': 12.0, 'E': 13100.0},
   {'A': 30875.0, 'B': 57563.0, 'C': 2713.0, 'D': 22.0, 'E': 30875.0},
   {'A': 57563.0, 'B': 103275.0, 'C': 8584.25, 'D': 24.0, 'E': 57563.0},
   {'A': 103275.0, 'B': 129163.0, 'C': 19555.25, 'D': 32.0, 'E': 103275.0},
   {'A': 129163.0, 'B': 311975.0, 'C': 27839.25, 'D': 35.0, 'E': 129163.0},
   {'A': 311975.0, 'B': '', 'C': 91823.63, 'D': 37.0, 'E': 311975.0}]},
 'Married filing jointly': {False: [{'A': 0.0,
    'B': 16300.0,  'C': 0.0, 'D': 0.0, 'E': 0.0},
   {'A': 16300.0, 'B': 39500.0, 'C': 0.0, 'D': 10.0, 'E': 16300.0},
   {'A': 39500.0, 'B': 110600.0, 'C': 2320.0, 'D': 12.0, 'E': 39500.0},
   {'A': 110600.0, 'B': 217350.0, 'C': 10852.0, 'D': 22.0, 'E': 110600.0},
   {'A': 217350.0, 'B': 400200.0, 'C': 34337.0, 'D': 24.0, 'E': 217350.0},
   {'A': 400200.0, 'B': 503750.0, 'C': 78221.0, 'D': 32.0, 'E': 400200.0},
   {'A': 503750.0, 'B': 747500.0, 'C': 111357.0, 'D': 35.0, 'E': 503750.0},
   {'A': 747500.0, 'B': '', 'C': 196669.5, 'D': 37.0, 'E': 747500.0}],
  True: [{'A': 0.0, 'B': 14600.0, 'C': 0.0, 'D': 0.0, 'E': 0.0},
   {'A': 14600.0, 'B': 26200.0, 'C': 0.0, 'D': 10.0, 'E': 14600.0},
   {'A': 26200.0, 'B': 61750.0, 'C': 1160.0, 'D': 12.0, 'E': 26200.0},
   {'A': 61750.0, 'B': 115125.0, 'C': 5426.0, 'D': 22.0, 'E': 61750.0},
   {'A': 115125.0, 'B': 206550.0, 'C': 17168.5, 'D': 24.0, 'E': 115125.0},
   {'A': 206550.0, 'B': 258325.0, 'C': 39110.5, 'D': 32.0, 'E': 206550.0},
   {'A': 258325.0, 'B': 380200.0, 'C': 55678.5, 'D': 35.0, 'E': 258325.0},
   {'A': 380200.0, 'B': '', 'C': 98334.75, 'D': 37.0, 'E': 380200.0}]},
 'Head of household': {False: [{'A': 0.0,
    'B': 13300.0,  'C': 0.0, 'D': 0.0, 'E': 0.0},
   {'A': 13300.0, 'B': 29850.0, 'C': 0.0, 'D': 10.0, 'E': 13300.0},
   {'A': 29850.0, 'B': 76400.0, 'C': 1655.0, 'D': 12.0, 'E': 29850.0},
   {'A': 76400.0, 'B': 113800.0, 'C': 7241.0, 'D': 22.0, 'E': 76400.0},
   {'A': 113800.0, 'B': 205250.0, 'C': 15469.0, 'D': 24.0, 'E': 113800.0},
   {'A': 205250.0, 'B': 257000.0, 'C': 37417.0, 'D': 32.0, 'E': 205250.0},
   {'A': 257000.0, 'B': 622650.0, 'C': 53977.0, 'D': 35.0, 'E': 257000.0},
   {'A': 622650.0, 'B': '', 'C': 181954.5, 'D': 37.0, 'E': 622650.0}],
  True: [{'A': 0.0, 'B': 10950.0, 'C': 0.0, 'D': 0.0, 'E': 0.0},
   {'A': 10950.0, 'B': 19225.0, 'C': 0.0, 'D': 10.0, 'E': 10950.0},
   {'A': 19225.0, 'B': 42500.0, 'C': 827.5, 'D': 12.0, 'E': 19225.0},
   {'A': 42500.0, 'B': 61200.0, 'C': 3620.5, 'D': 22.0, 'E': 42500.0},
   {'A': 61200.0, 'B': 106925.0, 'C': 7734.5, 'D': 24.0, 'E': 61200.0},
   {'A': 106925.0, 'B': 132800.0, 'C': 18708.5, 'D': 32.0, 'E': 106925.0},
   {'A': 132800.0, 'B': 315625.0, 'C': 26988.5, 'D': 35.0, 'E': 132800.0},
   {'A': 315625.0, 'B': '', 'C': 90977.25, 'D': 37.0, 'E': 315625.0}]}}

def find_line( agi, filing, w4_checkbox ):
    """Find the applicable line in the withholdings tables"""
    tab = withholding_tables[filing][w4_checkbox]
    for line in tab:
        if (line['A'] <= agi): 
            if line['B'] != '':
                if (line['B'] > agi):
                    return line
            else:
                return line

class Withholdings( object):
    """Finds the total withholdings from paychecks and per the withholdings tablees"""
    def __init__( self, W4 ):
        self.W4 = W4

    def calculateAGI( self, 
                      total_wages_in_pay_period : float,
                      number_of_pay_periods_per_year : int ):
        Line_1c = total_wages_in_pay_period * number_of_pay_periods_per_year
        Line_1e = self.W4.other_income + Line_1c
        Line_1f = self.W4.deductions # W4_4b_Deductions
        if self.W4.step2c:
            Line_1g = 0
        elif self.W4.filing_status == 'Married filing jointly':
            Line_1g = 12900
        else:
            Line_1g = 8600
        Line_1h = Line_1f + Line_1g
        Line_1i = Line_1e - Line_1h 
        if Line_1i < 0:
            Line_1i = 0
        return Line_1i

    def calc( self, 
              total_wages_in_pay_period :float, 
              number_of_pay_periods_per_year : int):
        agi = self.calculateAGI(  total_wages_in_pay_period, number_of_pay_periods_per_year )
        l = find_line( agi, self.W4.filing_status, self.W4.step2c)
        # print( self.W4.line3)
        yearly_withholding = ( agi - l['A'] )*l['D']*0.01 + l['C'] - self.W4.line3 
        payperiod_withholding = yearly_withholding / number_of_pay_periods_per_year
        return yearly_withholding, payperiod_withholding
