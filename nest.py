print('------列表当中嵌套字典---------------')
aliens = []
for alin_number in range(10):
    dic_alien = {'color': 'green', 'speed': 'low', 'point': 50}
    aliens.append(dic_alien)
print(len(aliens), aliens)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'high'
        alien['point'] = '100'
print(len(aliens),aliens)
