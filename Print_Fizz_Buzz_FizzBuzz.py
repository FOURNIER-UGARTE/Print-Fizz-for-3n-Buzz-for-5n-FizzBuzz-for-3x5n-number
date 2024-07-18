#Created by FOURNIER UGARTE Óscar

class Print_Fizz_Buzz_FizzBuzz:
    '''
    Receive a number, for multiples of three print “Fizz” instead of the number, and for the
    multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”
    '''
    @classmethod
    def print_Fizz_Buzz_FizzBuzz_number(cls, number):
        try:
            if ( number % ( 3 * 5 ) ) == 0:
                print('FizzBuzz', end='')
            elif ( number % 3 ) == 0:
                print('Fizz', end='')
            elif ( number % 5 ) == 0:
                print('Buzz', end='')
            else:
                print(str(number), end='')

            return True
        except TypeError:
            print('Sadly', TypeError)
        except ValueError:
            print('Sadly', ValueError)
        finally:
            return False

#Created by Óscar FOURNIER UGARTE