"""Practice with NLP using a dispersion plot on 'The Hound of the Baskersville'
with the names of main characters"""

import argparse, sys

import nltk
from nltk.text import Text
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Creates a Dispersion Map from any text and set of words",
                                 usage="COMMAND [-t --text Text File Name] "
                                       "[-l --list Target words separated by a space]")
parser.add_argument('-t', '--text', help="Text File Path")
parser.add_argument('-l', '--list', help="List of Targets", nargs='+')

args = parser.parse_args()

with open(args.text, 'r') as txtFile:
    text = txtFile.read()

tokens = nltk.word_tokenize(text)
tokens = Text(tokens)

dispersion = tokens.dispersion_plot(args.list)

plt.show()