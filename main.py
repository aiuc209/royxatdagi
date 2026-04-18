def katta_harflarga_aylantir(royxat):
    for dictionary in royxat:
        for kalit, qiymat in dictionary.items():
            if isinstance(qiymat, str):
                dictionary[kalit] = qiymat.upper()
    return royxat

royxat = [{'a': 'hello', 'b': 123}, {'c': 'world', 'd': 456}]
print(katta_harflarga_aylantir(royxat))
