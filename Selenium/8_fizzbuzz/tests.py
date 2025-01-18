from kod import fizzbuzz

def atest_fizzbuzz_basic():
    assert fizzbuzz(1) == 1
    assert fizzbuzz(2) == 2
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(9) == 'Fizz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(45) == 'FizzBuzz'
    assert fizzbuzz(150) == 'FizzBuzz'
    assert fizzbuzz(123) == 'Fizz'

print('Koniec')


