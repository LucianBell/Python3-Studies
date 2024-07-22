def get_day_week(day):
    days = {
        (1, 7): 'Weekend',
        tuple(range(2,7)): 'Week day',
    }
    chosen_day = (classification for numbers, classification in days.items() if day in numbers)
    return next(chosen_day)

test = 4

ha = get_day_week(test)
print(ha)
