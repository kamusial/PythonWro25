from kod import fizzbuzz

def test_fizzbuzz_basic():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(9) == 'Fizz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(45) == 'FizzBuzz'
    assert fizzbuzz(150) == 'FizzBuzz'
    assert fizzbuzz(123) == 'Fizz'

def test_fizzbuzz_negstive():
    assert fizzbuzz(-5) == 'Buzz'
    assert fizzbuzz(-1) == 1
    assert fizzbuzz(-12) == 'Fizz'

def test_fizzbuzz_0():
    assert fizzbuzz(0) == None

def test_fizzbuzz_float():
    assert fizzbuzz(5.8) == 'Buzz'
    assert fizzbuzz(5.1) == 'Buzz'
    assert fizzbuzz(-5.8) == 'Buzz'

def test_fizzbuzz_convertable_string():
    assert fizzbuzz('5.8') == 'Buzz'
    assert fizzbuzz('-4.2') == 4
    assert fizzbuzz('-15.9') == 'FizzBuzz'

def test_fizzbuzz_nonconvertable_string():
    assert fizzbuzz('Mama') == None
    assert fizzbuzz('Merita') == None
    assert fizzbuzz('siedem') == None

def test_fizzbuzz_list():
    assert fizzbuzz([1, 2, 3]) == [1, 2, 'Fizz']
    assert fizzbuzz([-1.7, '3.9', '-10.8']) == [1, "Fizz", 'Buzz']

def test_fizzbuzz_notsupported_types():
    assert fizzbuzz({'serek': 3.99}) == None

def test_fizzbuzz_english_numbers():
    assert fizzbuzz('one') == 1
    assert fizzbuzz('One') == 1
    assert fizzbuzz('oNe') == 1
    assert fizzbuzz('oNE') == 1
    assert fizzbuzz('thRee') == 'Fizz'

def test_fizzbuzz_names():
    assert fizzbuzz('Anna') == 4
    assert fizzbuzz('Kamil') == 'Buzz'
    assert fizzbuzz('Rex') == 'Fizz'









print('Koniec')


