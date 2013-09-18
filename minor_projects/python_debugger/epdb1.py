#epdb1.py -- experiment with Python debugger
#see http://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/
#for tutorial that acoompanies this script


import pdb


def combine(s1,s2):      # define subroutine combine, which...
    s3 = s1 + s2 + s1    # sandwiches s2 between copies of s1, ...
    s3 = '"' + s3 +'"'   # encloses it in double quotes,...
    return s3            # and returns it.

pdb.set_trace()

a = "aaa"
b = "bbb"
c = "ccc"
final = combine(a,b)
print final