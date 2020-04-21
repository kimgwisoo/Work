
def search4vowels(word):
    """Return a boolean based on any vowels found."""
    # return any vowels found in a supplied word.
    vowels = set('aeiou')
    found = vowels.intersection(set(word))

    """return bool(found)"""
    return found


print(search4vowels('sky'))
