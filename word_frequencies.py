import re, sys
from collections import defaultdict


""" Analysis of Runtime Complexity """

""" Given the structure of the methods, there are no operations that exceed an O(N)
complexity, with the exception of the call to "sorted" which is done in the 
third method and is of O(N log N) complexity. The call to sorted is higher in complexity
than any other operation done, and as a result causes run times to slightly exceed 
linear growth. As the input size doubles, the run time result is 2 * Log N, N being the 
problem size."""


def read_file(filename):
    """ Reads the contents of the passed file into a list. The contents, or 'tokens' are split
     with all characters that are not considered alphanumeric. This massive list with all valid
     alphanumeric tokens, is returned."""
    line_list = []
    input_text = open(filename, 'r')
    for line in input_text:
        line_list.extend(re.findall('[0-9a-zA-Z]+', line))
    return line_list


def tokenize(line_list):
    """ Takes the passed parameter of the list returned by the previous method and returns a
     dictionary which is has the token's as keys and their respective frequencies as
     values. Case is ignored in all tokens, and they are as a result all lowercase."""
    token_dict = defaultdict(int)
    for x in line_list:
        x = str(x).lower()
        token_dict[x] += 1
    return token_dict


def display_tokens(token_dict):
    """ Sorts the dictionary produced by the previous method, first by descending frequency
    then resolves ties alphabetically. Also prints the tokens and frequencies of the newly
    sorted dictionary."""
    for x in sorted(token_dict.items(), key = lambda (x, y): (-y, x)):
        print(str(x[0]) + " - " + str(x[1]))


def run_module(inputfile):
    """ The main method that does the method calls and runs the program."""
    line_list = read_file(inputfile)
    token_dict = tokenize(line_list)
    display_tokens(token_dict)


if __name__ == '__main__':
    """ Error handling for invalid or corrupted files as well as anything else that could unexpectedly occur. """
    try:
        run_module(sys.argv[1])
    except IOError:
        print ("The file entered was invalid.")
    except Exception:
        print "Unexpected error: ", sys.exc_info()[0]
        