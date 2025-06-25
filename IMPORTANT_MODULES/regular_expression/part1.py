print('SaM'.upper() in 'hello Sam'.upper())
import re
mystring='hi my name is Jacob'
print(re.search('Jacob',mystring))#<re.Match object; span=(14, 19), match='Jacob'>
#in jacob j is 14th index and 19 in 19th  index
match=re.search('Jacob',mystring)
print(match.span())
print(match.start())
print(match.end())
mystring='is this a world i am a  man'
matches=re.findall('a',mystring)
print(matches)
for _ in re.finditer('a',mystring):
    print(_.group())