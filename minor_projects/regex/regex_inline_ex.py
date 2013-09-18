import re

pattern = """
^					# beginning of string
M{0,4}				# thousands - 0 TO 4 M's
(CM|CD|D?C{0,3})	# hundreds - 900 (CM) 400 (CD), 0 - 300 (0 TO 3 C'S),
					#			OR 500-800 (D, FOLLOWED BY 0 TO 3 C'S)
(XC|XL|L?X{0,3})	# tens - 90 (XC), 40 (XL), 0 - 30 (0 TO 3 X'S), 
					# or 50-80 (L, followed by 0 to 3 X's)
(IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
$                   # end of string
"""

s1 = re.search(pattern, 'M', re. VERBOSE)
s2 = re.search(pattern, 'MCMLXXXIX', re.VERBOSE)
s3 = re.search(pattern, "MMMMDCCCLXXXVIII", re.VERBOSE)
s4 = re.search(pattern, "M") #will not be detected because it doesn't have the re.VERBOSE flag!!


s_tot = [s1, s2, s3, s4]

for item in s_tot:	
	print item