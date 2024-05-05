def tower_builder(n_floors):
    tower =[]
    for n in range(n_floors):
        spaces = n_floors - n - 1
        stars = (n+1)*2-1
        level = ''
        for space in range(spaces):
            level = level + ' '
        for star in range(stars):
            level = level + '*'
        for space in range(spaces):
            level = level + ' '
        tower.append(level)
    return tower