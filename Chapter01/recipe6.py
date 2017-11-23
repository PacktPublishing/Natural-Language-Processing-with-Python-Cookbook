from nltk.corpus import wordnet as wn

woman = wn.synset('woman.n.01')
bed = wn.synset('bed.n.01')

print(woman.hypernyms())
woman_paths = woman.hypernym_paths()

for idx, path in enumerate(woman_paths):
    print('\n\nHypernym Path :', idx + 1)
    for synset in path:
        print(synset.name(), ', ', end='')



types_of_beds = bed.hyponyms()
print('\n\nTypes of beds(Hyponyms): ', types_of_beds)

print(sorted(set(lemma.name() for synset in types_of_beds for lemma in synset.lemmas())))