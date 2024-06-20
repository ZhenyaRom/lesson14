def single_same_root(root_word, other_words1='*', other_words2='*', other_words3='*', other_words4='*'):
    other_words = [other_words1, other_words2, other_words3, other_words4]
    same_root = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_root.append(i)
    return same_root


result1 = single_same_root('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_same_root('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
