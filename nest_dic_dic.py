users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'priceton'
    },
    'macurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}
for username, user_info in users.items():
    print("\n UserName: " + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\t full_name: ' + full_name.title())
    print('\t location: ' + location.title())
