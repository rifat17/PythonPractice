import re

phoneRegex  = re.compile(r'\d{3}-\d{3}-\d{4}')

mo  = phoneRegex.search('My Phone Number is 453-121-2334.')

print('Phone Number found : ' + mo.group())

# bdPhoneRe = re.compile(r'(\+88)?01[1356789]\d{8}')
bdPhoneRe = re.compile(r'01[1356789]\d\s*\d\s*\d{6}')

# bdPhoneRe = re.compile(r'(\+88)*?01[1356789]\d{8}')

mo = bdPhoneRe.search('My Phone Number is +88+8801828 797973.')

print(mo)
print('Phone Number found : ' + mo.group())

# Grouping with Parentheses

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My Number is 452-555-3534')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))  # Full match
print(mo.group())   # Full match


phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My Phone number is (445) 555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group())


# Matching Multiple group with the PIPE

heroRegex = re.compile(r'Batman|Tina Fey') # The first occurance of matching will return
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())


heroRegex = re.compile(r'Batman|Tina Fey') # The first occurance of matching will return
mo1 = heroRegex.search('Tina Fey and Batman')
print(mo1.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())       # returns Full matched text
print(mo.group(1))      # returns just the part of the matched text
                        # inside first parentheses group

batRegex = re.compile(r'Bat(wo)?man')
# Here,The (wo)? part of regex means that the pattern 'wo' is an optional group
# (wo)? regex will match that has zero or one isntance of 'wo' in it.
mo1 = batRegex.search('The advanture of Batman')
print(mo1.group())

mo2 = batRegex.search('The advantage of Batwoman')
print(mo2.group())

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.search('My Number is 452-555-5343')
print(mo1.group())
mo2 = phoneNumRegex.search('My Number is 555-5343')
print(mo2.group())

# Matching Zero or More with Star(*)

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Advantures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Advantures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Advantures of Batwowowowoman')
print(mo3.group())


# Matching One or More with plus(+)

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Advantures of Batman')
print(mo1 == None)

mo2 = batRegex.search('The Advantures of Batwoman')
print(mo2.group())

mo3 = batRegex.search('The Advantures of Batwowowowoman')
print(mo3.group())


# Matching specific repetition with Curly Bracket

 # (Ha){3} will match the string 'HaHaHa' But
 # it will mot match 'HaHa'
 # since the latter has only two repeats of the (Ha) Group

# you can specify the range of repetition
# (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', 'HaHaHaHaHa'
# also
# (Ha){3,}
# (Ha){,5}

# These RE are Identical

# (Ha){3}
# (Ha)(Ha)(Ha)

# (Ha){3,5}
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))


haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo1 = haRegex.search('HaHaHaHa') # Match first # 'Ha',ignores rest
print(mo1.group())
mo1 = haRegex.search('HaHa')
print(mo1 == None)

# Matching One or More with the Plus

'''While * means “match zero or more,” the + (or plus) means “match one or
more.” Unlike the star, which does not require its group to appear in the
matched string, the group preceding a plus must appear at least once. It is
not optional.'''

batRegex = re.compile(r'Bat(wo)+man')

mo1 = batRegex.search("The Advantures of Batwoman")

print(mo1.group())

mo2 = batRegex.search("The Advantures of Batwowowowoman")

print(mo2.group())

mo3 = batRegex.search("The Advantage of Batman")

print(mo3 == None)

'''The findall() Method
In addition to the search() method, Regex objects also have a findall()
method. While search() will return a Match object of the first matched text
in the searched string, the findall() method will return the strings of every
match in the searched string.'''

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call: 451-555-9999 Work: 212-555-0000')
# will  reruen 451-555-9999 , a single object, first match only 
print(mo.group()) 


phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # Has no groups
mo = phoneNumRegex.findall('Call: 451-555-9999 Work: 212-555-0000')
print(mo)  #  ['451-555-9999', '212-555-0000']

'''
If there are groups in the regular expression, then findall() will return
a list of tuples. https://www.youtube.com/playlist?list=PLyb_C2HpOQSDxe5Y9viJ0JDqGUCetboxBEach tuple represents a found match, and its items are the
matched strings for each group in the regex. To see findall() in action, enter
the following into the interactive shell (notice that the regular expression
being compiled now has groups in parentheses):
'''

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # Has groups
mo = phoneNumRegex.findall('Call: 451-555-9999 Work: 212-555-0000')
print(mo)  #  [('451', '555', '9999'), ('212', '555', '0000')]

'''
To summarize what the findall() method returns, remember the
following:
1.
When called on a regex with no groups, such as \d\d\d-\d\d\d-\d\d\d\d ,
the method findall() returns a list of string matches, such as ['415-555-
9999', '212-555-0000'] .

2.
When called on a regex that has groups, such as (\d\d\d)-(\d\d\d)-(\d\
d\d\d) , the method findall() returns a list of tuples of strings (one string
for each group), such as [('415', '555', '1122'), ('212', '555', '0000')] .
'''




# Character Classes
'''
In the earlier phone number regex example, you learned that \d could
stand for any numeric digit. That is, \d is shorthand for the regular expres-
sion (0|1|2|3|4|5|6|7|8|9) . 
There are many such shorthand character classes, as shown in Table 7-1.

Table 7-1: Shorthand Codes for Common Character Classes

Shorthand character class               Represents
    \d                      Any numeric digit from 0 to 9.
    \D                      Any character that is not a numeric digit from 0 to 9.
    \w                      Any letter, numeric digit, or the underscore character.
                                (Think of this as matching “word” characters.)
    \W                      Any character that is not a letter, numeric digit, or the
                                underscore character.
    \s                      Any space, tab, or newline character. (Think of this as
                                matching “space” characters.)
    \S                      Any character that is not a space, tab, or newline.




Character classes are nice for shortening regular expressions. The char-
acter class [0-5] will match only the numbers 0 to 5 ; this is much shorter
than typing (0|1|2|3|4|5) .

'''

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 \
                        swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

print(mo)



# Making Your Own Character Classes

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('Robocop eats baby food, BABY FOOD')
print(mo)


'''
You can also include ranges of letters or numbers by using a hyphen.
For example, the character class [a-zA-Z0-9] will match all lowercase letters,
uppercase letters, and numbers.

Note that inside the square brackets, the normal regular expression
symbols are not interpreted as such. This means you do not need to escape
the . , * , ? , or () characters with a preceding backslash. For example, the
character class [0-5.] will match digits 0 to 5 and a period. You do not need
to write it as [0-5\.] .

By placing a caret character ( ^ ) just after the character class’s opening
bracket, you can make a negative character class. A negative character class
will match all the characters that are not in the character class.

'''


consonentRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonentRegex.findall('Robocop eats baby food, BABY FOOD')
print(mo)

# The Caret and Dollar Sign Characters

'''
You can also use the caret symbol ( ^ ) at the start of a regex to indicate that
a match must occur at the beginning of the searched text. Likewise, you can
put a dollar sign ( $ ) at the end of the regex to indicate the string must end
with this regex pattern. And you can use the ^ and $ together to indicate
that the entire string must match the regex—that is, it’s not enough for a
match to be made on some subset of the string.

For example, the r'^Hello' regular expression string matches strings
that begin with 'Hello' .

'''


beginsWithHello = re.compile(r'^Hello')
mo = beginsWithHello.search('Hello World')
print(mo)

mo = beginsWithHello.search('He said hello')
print(mo == None)  #  No match will return a None

# mo = beginsWithHello.search('World. \nHello')
# print(mo)

'''
The r'\d$' regular expression string matches strings that end with a
numeric character from 0 to 9.

'''

endsWithNumber = re.compile(r'\d$')
mo = endsWithNumber.search('Your gpa is 2.94')
print(mo)
mo = endsWithNumber.search('Your gpa is two pont nine four')
print(mo == None) #  No match will return a None



'''
The r'^\d+$' regular expression string matches strings that both begin
and end with one or more numeric characters.

'''
wholeStringNumber = re.compile(r'^\d+$')
mo = wholeStringNumber.search('1234567890')
print(mo)

mo = wholeStringNumber.search('12345x67890')
print(mo == None)

mo = wholeStringNumber.search('12 34567890')
print(mo == None)

'''
The last two search() calls in the previous interactive shell example dem-
onstrate how the entire string must match the regex if ^ and $ are used.

I always confuse the meanings of these two symbols, so I use the mne-
monic “Carrots cost dollars” to remind myself that the caret comes first and
the dollar sign comes last.

'''

# The Wildcard Character
'''
The . (or dot) character in a regular expression is called a wildcard and will
match any character except for a newline.

'''

atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)  # ['cat', 'hat', 'sat', 'lat', 'mat']

mo = atRegex.search('The cat in the hat sat on the flat mat.')
print(mo)  #  <re.Match object; span=(4, 7), match='cat'>

'''
Remember that the dot character will match just one character, which
is why the match for the text flat in the previous example matched only lat .
To match an actual dot, escape the dot with a backslash: \. .

'''

# Matching Everything with Dot-Star

'''
Sometimes you will want to match everything and anything. For example,
say you want to match the string 'First Name:' , followed by any and all text,
followed by 'Last Name:' , and then followed by anything again. You can
use the dot-star ( .* ) to stand in for that “anything.” Remember that the
dot character means “any single character except the newline,” and the
star character means “zero or more of the preceding character.”

'''

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo)  #  <re.Match object; span=(0, 34), match='First Name: Al Last Name: Sweigart'>
print(mo.group())    #  First Name: Al Last Name: Sweigart
print(mo.group(1))   #  Al
print(mo.group(2))   #  Sweigart

'''
The dot-star uses greedy mode: It will always try to match as much text as
possible. To match any and all text in a nongreedy fashion, use the dot, star,
and question mark ( .*? ). Like with curly brackets, the question mark tells
Python to match in a nongreedy way.

'''

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())  #  <To serve man>

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())  #  <To serve man> for dinner.>

'''
Both regexes roughly translate to “Match an opening angle bracket,
followed by anything, followed by a closing angle bracket.” But the string
'<To serve man> for dinner.>' has two possible matches for the closing angle
bracket. In the nongreedy version of the regex, Python matches the shortest
possible string: '<To serve man>' . In the greedy version, Python matches the
longest possible string: '<To serve man> for dinner.>' .

'''

# Matching Newlines with the Dot Character

'''
The dot-star will match everything except a newline. By passing re.DOTALL as
the second argument to re.compile() , you can make the dot character match
all characters, including the newline character.

'''

noNewLineRegex = re.compile('.*')
#  <re.Match object; span=(0, 23), match='Serve the public trust.'>
mo = noNewLineRegex.search('Serve the public trust.\nProtect the innocent\n')
print(mo)


NewLineRegex = re.compile('.*', re.DOTALL)
# <re.Match object; span=(0, 45), match='Serve the public trust.\nProtect the innocent\n'>
mo = NewLineRegex.search('Serve the public trust.\nProtect the innocent\n')
print(mo)

'''
The regex noNewlineRegex , which did not have re.DOTALL passed to the
re.compile() call that created it, will match everything only up to the first
newline character, whereas newlineRegex , which did have re.DOTALL passed to
re.compile() , matches everything. This is why the newlineRegex.search() call
matches the full string, including its newline characters.

'''


# Review of Regex Symbols

'''
This chapter covered a lot of notation, so here’s a quick review of what
you learned:

    The ? matches zero or one of the preceding group.
    The * matches zero or more of the preceding group.
    The + matches one or more of the preceding group.
    The {n} matches exactly n of the preceding group.
    The {n,} matches n or more of the preceding group.
    The {,m} matches 0 to m of the preceding group.
    The {n,m} matches at least n and at most m of the preceding group.
    {n,m}? or *? or +? performs a nongreedy match of the preceding group.
    ^spam means the string must begin with spam.
    spam$ means the string must end with spam.
    The . matches any character, except newline characters.
    \d , \w , and \s match a digit, word, or space character, respectively.
    \D , \W , and \S match anything except a digit, word, or space character,
        respectively.
    [abc] matches any character between the brackets (such as a, b, or c).
    [^abc] matches any character that isn’t between the brackets.

'''

# Case-Insensitive Matching
'''
Normally, regular expressions match text with the exact casing you specify.

regex1 = re.compile('RoboCop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

But sometimes you care only about matching the letters without worry-
ing whether they’re uppercase or lowercase. To make your regex case-insen-
sitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile() .
'''
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('Robocop protects the innocent')
print(mo)  #  <re.Match object; span=(0, 7), match='Robocop'>

mo = robocop.search('ROBOCOP protects the innocent')
print(mo)  #  <re.Match object; span=(0, 7), match='ROBOCOP'>
print(robocop.search('ROBOCOP protects the innocent').group())  #  ROBOCOP
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())
# robocop

