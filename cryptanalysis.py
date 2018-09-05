import os, sys, math, argparse, os.path

# cipher.py
#
# A command-line toolkit used to analyze the statistical properties of files
#
# Usage:
#
# -i: provide input file name
# -n: provide integer for distribution frequency and n-graph
#
# Example Usage:
#
# -i encrypted.txt -n 1
#
# Copyright 2018 Emmit Parubrub



def read_input(input_file_name):
    """read in file based on name provided"""
    if not os.path.exists(input_file_name):
        print('The file %s does not exist... Exiting now ...' % (input_file_name))
        sys.exit()
    else:
        input_file = open(input_file_name)
        input_file_content = input_file.read()
        input_file.close()
        return input_file_content



class Distribution(object):
    """ Base class for analysis routines for symbol distributions.
        Results are dictionary objects with human readable keys.
        - class copied from Paul A. Lambert
    """
    def to_readable(self):
        """ Convert dictionary of symbols to readable text """
        pp = []
        for nary in self.result:
            pp.append( "{}: {}\n".format( nary, self.result[nary]))
        return ''.join(pp)


class Ngraph(Distribution):
    """ Looking 'n' symbols at a time, create a dictionary
        of the occurrences of the n-ary string of symbols.
        Default is n=1, a monograph.
        - class copied from Paul A. Lambert
    """
    def __init__(self, n=1 ):
        self.n = n

    def analyze(self, text):
        n = self.n
        self.result = {} # results are stored as a dictionary
        for i in range( len(text) - n - 1 ):
            nary = text[ i:i+n ]
            if nary in self.result:
                self.result[nary] += 1
            else:
                self.result[nary] = 1
        return self.result


class n_graph(Distribution, int):
    def analyze(self, text): self.result = Ngraph( n=int ).analyze(text)


dist_dict = {'ng':Ngraph}
dist_name_list =[ key for key in dist_dict]


def write_output(output_file_name, output_content):
    """ write the output file based on output name provided and
        output information
    """
    output_file = open(output_file_name, 'w')
    output_file.write(output_content)
    output_file.close()
    return 0


def parse_args():
    """setsup the argument parser then return correct arguments"""
    parser = argparse.ArgumentParser(description='Encrypt/Decrypt a file')
    parser.add_argument("-i", "--input_file_name", type=str, required=True, dest="input_v",
                        help = 'Please enter an input file name ')
    parser.add_argument("-n", "--distribution selection", type=int, required=True, dest="choice_v",
                        help='Please enter an integer choice to specify the n-gram you'
                             ' would like to print out (must be greater than 0 and less'
                             ' than 20)')
    args = parser.parse_args()
    print(args)
    return args


def check_args(choice, input_file_name):
    """checks argument validity"""
    if choice < 1 or choice > 20:
        print("error, please pick an integer choice greater than 0 and less than 21")
        exit()

    if not os.path.isfile(input_file_name):
        print("error, please input a valid file name (file might "
              "not be in this directory)")
        exit()

def check_caesar(content):
    """ takes in plain text that is longer than 25 chars, english alphabet, and spaces.
        this function prints out all possibilities of a caesar-cipher and its
        corresponding amount of shifts.
    """
    content = content[0:25]
    content.lower()
    alpha_count = 26

    count = 0
    while count < alpha_count:
        data = ""
        for i in content:
            if (chr(ord(i)) == ' '):
                data += ' '
            else:
                if ord(i) == 122:
                    data += 'a'
                else:
                    data += (chr(ord(i) + 1))
        content = data
        print(data + "   -", count, "shifts up")
        count += 1


def print_n_graph(input_file, n):
    """Prints distribution frequency and n-graph.
       Distribution frequency is calculated by
       dividing the values by the amount of characters
       total.
    """
    D = dist_dict['ng']
    dist = D(n)
    text = read_input(input_file)

    temp = dist.analyze(text)

    print()
    print(n, "- gram distribution:")
    print(dist.to_readable())
    print()
    print()
    print("Distribution Frequency: ")

    for i in temp:
        temp[i] = temp[i]/text.__len__()

    for key, value in temp.items():
        print(key + ": ",  value)
    print()
    print()
    print()
    print("brute force caesar cipher check:")
    check_caesar(text)


def main():
    args = parse_args()
    input_file_name = args.input_v
    choice = args.choice_v
    check_args(choice, input_file_name)
    print_n_graph(input_file_name, choice)


if __name__ == '__main__':
    main()