import re

text = 'This is some text -- with punctuation.'

print 'Input text            :', text

# word starting with 't' then another word
regex = re.compile(r'(\bt\w+)\W+(\w+)')
print 'Pattern               :', regex.pattern  #.pattern calls the string that was compiled

match = regex.search(text)
print 'Entire match          :', match.group(0)  #printing out match of entire pattern
print 'Word starting with "t":', match.group(1)	 #printing out first group of the pattern (first the in parenthesis)
print 'Word after "t" word   :', match.group(2)	 #printing out second group of the pattern