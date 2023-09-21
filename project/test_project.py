from project import input_check,get_level,generate_integer,operation,generate_operation
from unittest.mock import patch


def main():
    test_input_check()
    test_generate_integer()
    test_operation()
    test_generate_operation()


def test_input_check():

    # valid input
    with patch('builtins.input', return_value='42'):
        result1 = input_check(10, 20, '+')
        assert result1 == "42"
        
    # one invalid followed by valid
    with patch('builtins.input', side_effect=['abc', '3.14']):
        result2 = input_check(5, 7, '*')
        assert result2 == "3.14"

    # two invalid followed by valid
    with patch('builtins.input', side_effect=['xyz', 'hello', '0.123']):
        result2 = input_check(5, 7, '*')
        assert result2 == "0.123"

    # three invalid followed by valid
    with patch('builtins.input', side_effect=['xy', 'brandon', 'boo','-0.123']):
        result2 = input_check(5, 7, '*')
        assert result2 == "-0.123"

# Test function for 'get_level()'.
def test_get_level():

    # valid input
    with patch('builtins.input', return_value='1'):
        result1 = get_level()
        assert result1 == 1

    # one invalid followed by valid
    with patch('builtins.input', side_effect=['abc', '3']):
        result2 = get_level()
        assert result2 == 3

    # two invalid followed by valid
    with patch('builtins.input', side_effect=['xyz', '74', '2']):
        result2 = get_level()
        assert result2 == 2

    # three invalid followed by valid
    with patch('builtins.input', side_effect=['xy', '65', 'boo','2']):
        result2 = get_level()
        assert result2 == 2

# Test function for 'generate_integer'.
def test_generate_integer():
    single_range = range(0,10)
    double_range = range(10,100)
    triple_range = range(100,1000)

    assert generate_integer(1) in single_range
    assert generate_integer(2) in double_range
    assert generate_integer(3) in triple_range

# Test function for 'operation'.
def test_operation():
    assert operation(9,3,"+") == 12
    assert operation(6,0,"/") == 0
    assert operation(32,18,"+") == 50
    assert operation(100,100,"*") == 10000
    assert operation(500,500,"-") == 0


# Test function for 'generate_operation'.
def test_generate_operation():
    acceptable_operations = "+-*/"

    assert generate_operation() in acceptable_operations

if __name__ == "__main__":
    main()
