def fizzbuzz(x):
    if isinstance(x, list):
        result_list = []
        for element in x:
            element = abs(element)
            if element % 3 == 0 and element % 5 == 0:
                result_list.append('FizzBuzz')
            elif element % 3 == 0:
                result_list.append('Fizz')
            elif element % 5 == 0:
                result_list.append('Buzz')
            else:
                result_list.append(element)
        return result_list
    else:
        x = abs(x)
        if x % 3 == 0 and x % 5 == 0:
            return 'FizzBuzz'
        elif x % 3 == 0:
            return 'Fizz'
        elif x % 5 == 0:
            return 'Buzz'
        return x