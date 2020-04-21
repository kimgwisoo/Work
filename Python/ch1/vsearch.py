
# def search4vowels(phrase: str) -> set:
#     """Return any vowels found in a supplied phrase."""          #인자를 str:1개를 받아 반환함
#     vowels = set('aeiou')
#     return vowels.intersection(set(phrase))


def search4letters(letters: str, phrase: str) -> set:
    """Retrun a set of the 'letters' found in 'phrase'."""
    return set(letters) < set(phrase)
    # 인자를 str:2개를 받아 비교하여 반환


def search5letters(letters: str, phrase: str) -> set:
    """Retrun a set of the 'letters' found in 'phrase'."""
    return set(letters) > set(phrase)

    # -------------------------- 집 합 명령어 ---------------------------
    # intersection = & 기호로 사용 가능 하다.     : 교집합
    # union = |                   : 합집합
    # difference = -              : 차집합
    # symmetric_difference = ^    : 대칭차집합
    # issubset =   >=,<=          : 부분집합
    # issuperset =    >,<         : 상위집합


#print(search4letters('Hitch-Hiker', 'aeiou'))
print(search4letters('abc', 'abc'))
print(search5letters('abc', 'abc'))
