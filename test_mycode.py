import mycode

def test_lowercase():
    assert mycode.my_function("JEFF") == "jeff"

def test_cusp():
    assert mycode.taxCalc('single',9999.99) == 999.999

def test_fakeFiler():
    assert mycode.taxCalc('double',10) == None

def test_negMoney():
    assert mycode.taxCalc('joint',-10) == None

def test_stringIncome():
    assert mycode.taxCalc('joint','hola') == None

def test_norm():
    assert mycode.taxCalc('single',17000) == 999.9 + .15 * 7001