# this is all original, you can use this in video

import sys
import argparse

print(sys.argv) # default way to get command line arguments

# positional arguments -> arguments required to make the program work correctly
parser = argparse.ArgumentParser() # define the parser
# the argument flag, help for argument, type of input (optional)
# basic usage: python main.py MyName
parser.add_argument("name", help="Input your name here", type=str)
# -- = optional argument. usage: python main.py Jack --age 20 (you can also use -a instead of --age)
parser.add_argument("--age", "-a", help="Input your age here", type=int)
# metavar will clean up the help for the command (optional)
# required=True will let flags become required
parser.add_argument("--old", "-o", metavar='', required=True, help="Are you old, Anon?", type=bool)

# add_mutually_exclusive_group -> prevents multiple flags to be used (--quiet and --verbose should not be used together)
group = parser.add_mutually_exclusive_group()
# store_true -> if flag was added, return true, else, false
group.add_argument("-q", "--quiet", action="store_true", help="Gives short output")
group.add_argument("-v", "--verbose", action="store_true", help="Gives long output")

args = parser.parse_args()

if(args.quiet): # access the argument (has to use long flag, can NOT do args.q)
    print(args.name + " is your name.")
elif(args.verbose):
    print(args.name + " is " + str(args.age or (5000 if args.old else 0)) + " years old. This is a very long output, thanks to the verbose flag.")
else:
    print(args.name + " is " + str(args.age or (5000 if args.old else 0)) + " years old")