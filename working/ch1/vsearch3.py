
def search4vowels(phrase: str) -> set:
    """Return a boolean based on any vowels found."""
    # return any vowels found in a supplied word.
    vowels = set('aeiou')

    """return bool(found)"""
    return vowels.intersection(set(phrase))


print(search4vowels('werkjqkwjebrkajbskjbase;krjasldkfsadf'))
