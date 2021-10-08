class Validator:
    def __init__(self):
        pass

    # Function for prompting for user input, accepts a callback and options to include up to two optional parameters in callback call
    def prompt_input(self, question, callback, opt_param_1 = False, opt_param_2 = False ):
        isValid = False
        response = ""
        while(not isValid or response == ""):
            response = input(question)
            if opt_param_1 and opt_param_2:
                isValid = callback(response, opt_param_1, opt_param_2)
            elif opt_param_1:
                isValid = callback(response, opt_param_1)
            else:
                isValid = callback(response)
        return response

    def number_in(self, n, arr):
        try:
            int(n)
        except:
            print('Only numbers are accepted')
            return False
        if int(n) in arr:
            return True
        else:
            print(f"Selection must be one of the following:")
            for number in arr:
                print(f"{number}")
            return False

    def number_between(self, n, a, b):
        try:
            int(n)
        except:
            print('Only numbers are accepted')
            return False
        if int(n) >= a and int(n) <= b:
            return True
        else:
            print(f"Selection must be between {a} and {b}")
            return False
    
    def element_in(self, element, arr):
        if (element) in arr:
            return True
        else:
            return False

    def auto_valid(self, a):
        return a == a

    def is_odd(self, num1):
        try:
            int(num1)
        except:
            print('Only enter numbers')
            return False
        if num1 % 2 !=  0:
            return True
        else:
            print(f'Number must be an odd number')
            return False