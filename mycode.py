def my_function(str):
    name=str
    return name.lower()

def taxCalc(filer,income):
    if  type(income) not in [int,float]:
        return None
    if filer not in ['single','joint'] or income < 0:
        return None
    if filer == 'single':
        if income < 10000:
            return income/10
        elif income < 50000:
            return (9999 / 10) + (income-9999) * .15
        elif income < 100000:
            return 9999 / 10 + 40000 * .15 + (income - 49999) * .2
        else: 
            return 9999 / 10 + 40000 * .15 + 50000 * .2 + (income - 99999) * .25
    if filer == 'joint':
        if income < 20000:
            return income/10
        elif income < 100000:
            return 19999 / 10 + (income-19999) * .15
        elif income < 200000:
            return 19999 / 10 + 80000 * .15 + (income - 99999) * .2
        else: 
            return 19999 / 10 + 80000 * .15 + 100000 * .2 + (income - 199999) * .25