from datetime import datetime

def dominical(year=int) -> str:
    letter, y, c = '', int(str(year)[2:]), int(str(year)[:2])
    index = (y+(y/4)+5*(c % 4)-1)%7
    letters = ['G', 'F', 'E', 'D', 'C', 'B', 'A']
    try: 
        datetime(year, 2, 29) # check for leap year
        first_letter, second_letter = '', ''
        first_letter = letters[int(index)-1]
        if int(index) < 0:
            first_letter = letters[6]
        second_letter = letters[int(index)]
    except ValueError:
        second_letter = letters[int(index)]
    letter = first_letter+second_letter
    print(letter)
    return letter


dominical(2024)
