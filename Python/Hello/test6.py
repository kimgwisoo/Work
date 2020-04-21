s = ' spam and ham '
print(s.strip())
print(s.rstrip())
print(s.lstrip())

s = '<><abc><defg><><>'
print(s.strip('<>'))
s = 'Hello Java'
print(s.replace( 'Java', 'Python'))