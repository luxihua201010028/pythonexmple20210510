favorite_language = {
    'jen': ['python', 'java', 'ruby'],
    'sea': ['C', 'vb'],
    'edward': ['ruby', 'css'],
    'phil': ['python', 'html']
}
for me, lan in favorite_language.items():
    print("\n" + me.title() + "'s" "fav language are ")
    for language in lan:
        print("\t" + language.title())
