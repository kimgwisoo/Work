s = "I Like Python. I Like Java Also"
print(s.count('Like'))

print(s.find('Like'))
print(s.find('Like', 5))
print(s.find('JS'))
print(s.rfind('Like'))

# print(s,index('JS'))
print(s.rindex('Like'))

print(s.startswith('I Like'))
print(s.startswith('Like', 2))
print(s.endswith('Also'))
print(s.endswith('Java', 0, 26))