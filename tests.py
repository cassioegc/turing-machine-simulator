from main import init

#palindrome_detector
assert(init("palindrome_detector.txt", "1001001") == (38, ":)"))
assert(init("palindrome_detector.txt", "") == (3, ":)"))

assert(init("palindrome_detector.txt", "100100") == (15, ":("))
assert(init("palindrome_detector.txt", "10") == (7, ":("))

#binary_addition
assert(init("binary_addition.txt", "110110 101011") == (135, "1100001"))
assert(init("binary_addition.txt", "0 0") == (12, "0"))

#binary_multiplication
assert(init("binary_multiplication.txt", "1101 11010") == (980, "101010010"))
assert(init("binary_multiplication.txt", "1101 0") == (366, "0000"))

#binary_to_decimal_conversion
assert(init("binary_to_decimal.txt", "10110") == (340, "22"))
assert(init("binary_to_decimal.txt", "01") == (23, "1"))

#parentheses_checker
assert(init("parentheses_checker.txt", "12(2+(3^(4-1)))") == (217, ":)"))
assert(init("parentheses_checker.txt", "((12(23)))") == (152, ":)"))

assert(init("parentheses_checker.txt", "12(2+(3^(4-1))))") == (220, ":("))
assert(init("parentheses_checker.txt", "(1)2(2+(3^(4-1))))") == (268, ":("))

#reverse_polish_boolean_calculator
assert(init("reverse_polish_boolean_calculator.txt", "10~1&|0|") == (141, "1"))
assert(init("reverse_polish_boolean_calculator.txt", "10~1&|0|1") == (166, "11"))

#primality_test
assert(init("primality_test.txt", "10") == (280, "10 is prime!"))
assert(init("primality_test.txt", "11") == (500, "11 is prime!"))
assert(init("primality_test.txt", "101") == (1574, "101 is prime!"))
assert(init("primality_test.txt", "111") == (2606, "111 is prime!"))

assert(init("primality_test.txt", "100") == (730, "100 is not prime."))
assert(init("primality_test.txt", "110") == (1127, "110 is not prime."))
assert(init("primality_test.txt", "1000") == (2123, "1000 is not prime."))
assert(init("primality_test.txt", "1001") == (3345, "1001 is not prime."))

#4_state_busy_beaver
assert(init("4state_busy_beaver.txt", "") == (108, "1 111111111111"))
assert(init("4state_busy_beaver.txt", "11") == (106, '1 111111111111'))

#universal_turing_machine
assert(init("universal_turing_machine.txt", "[ L+,0R.,1R.!1L+,1L+,0L.:,0L.,1L.:]1011") == (1974, "[ L+,0R.,1R.:1L+,1L+,0L.:,0L.,1L.!] 1100"))
