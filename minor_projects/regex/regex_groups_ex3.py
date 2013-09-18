#naming your pattern groups:

import re

text = 'This is some text -- with punctuation.'

print text
print

for pattern in [ r'^(?P<first_word>\w+)', 
                 r'(?P<last_word>\w+)\S*$',                      #notation ?P<first_word> to name the group first_word                 r'(?P<last_word>\w+)\S*$',
                 r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
                 r'(?P<ends_with_t>\w+t)\b',
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print 'Matching "%s"' % pattern
    print '  ', match.groups()
    print '  ', match.groupdict()                               #prints out the assosciated group name with the match in dictionary format
    print