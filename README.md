# Cryptanalysis Program


This program is a command-line toolkit used to analyze the statistical properties of encrypted files.
The 1st paragraph of information lists the selected gram distribution and lists out the corresponding
characters along with the number of times the character appears. The 2nd paragraph of information displays
each characters distribution frequency. The 3rd paragraph of information displays each possible caesar cipher
variation with its corresponding amount of shifts. The last paragraph is a visual representation of the attempted
poly-alphabetic cipher break in which the highest character frequency is paired with the highest frequency 
in the English language (taken from Pavel Mička's website, which cites Robert Lewand's Cryptological Mathematics)
This is output into a file called output.txt. Please note that the poly-alphabetic cipher will only work
with a file that holds large amounts of data like a digitalized book. 

## Usage

-i: provide input file name  
-o: provide an integer for distribution frequency and n-graph

```
 Example: ./cryptanalysis.py -i encrypted.txt -n 1
```

## References

Referenced - Paul Lambert, professor at the University of San Francisco,  wrote the class Ngraph in which I used a majority of his code 

---
Website - [Wikipedia - Letter Frequency](https://en.wikipedia.org/wiki/Letter_frequency)

Notes - letter frequency of the english language found under "Relative frequencies of 
letters in the English language" section

---
Citation - Department of the Army. Basic CryptAnalysis. 1970.

Notes - Poly-alphabetic solution idea taken from section 9-3 "Solution by frequency matching" in


