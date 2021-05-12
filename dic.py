favorite_language = {
    'jen': 'python',
    'sea': 'C',
    'edward': 'ruby',
    'phil': 'python'
}
for key, value in favorite_language.items():
    print(key.title() + "'s favorite language is " +
          value.title() + '.')
print('------------------------------------')
for key in favorite_language.keys():
    print(key.title())
print('------------------------------------')
for value in favorite_language.values():
    print(value.title())
print('------------------------------------')
for key in favorite_language:
    print(key.title())
print('------------------------------------')
for language in set(favorite_language.values()):
    print(language)
