# Liturgical Dates

Just a collections of functions for calculating liturgical dates. The goal is not to be scientifically accurate, but to be accurate according to the Gregorian Calendar. The dates for the moon are rarely off by more than a day, and work with this margin of error until about the year 5200.

## Convert an interger to roman numerals

Not a date, but a useful function for the correct output of the epact.

```python
def interger_to_roman(A=int) -> int:
    romans = {
        1: "I", 5: "V", 10: "X", 50: "L", 100: "C",
        500: "D", 1000: "M", 5000: "G", 10000: "H",
    }
    div, result = 1, ''
    while A >= div:
        div *= 10
    div /= 10
    while A:
        last_num = int(A / div)
        if last_num <= 3:
            result += (romans[div]*last_num)
        elif last_num == 4:
            result += (romans[div]+romans[div*5])
        elif 5 <= last_num <= 8:
            result += (romans[div*5]+(romans[div]*(last_num-5)))
        elif last_num == 9:
            result += (romans[div]+romans[div*10])
        A = floor(A % div)
        div /= 10
    return result
```

## Dominical Letter
```python
def dominical(year=int) -> str:
    letter, y, c = '', int(str(year)[2:]), int(str(year)[:2])
    index = (y+(y/4)+5*(c % 4)-1) % 7
    letters = ['G', 'F', 'E', 'D', 'C', 'B', 'A']
    first_letter, second_letter = '', ''
    try:
        datetime(year, 2, 29)
        first_letter = letters[int(index)-1]
        if int(index) < 0:
            first_letter = letters[6]
        second_letter = letters[int(index)]
    except ValueError:
        second_letter = letters[int(index)]
    letter = first_letter+second_letter
    return letter
```

## Golden Number
```python
def golden_number(year=int) -> int:
    return (year+1) % 19
```

## Epact (for the years 1600-5199)
```python
def epact_adjust(year=int) -> int:
    l, s, c = 0, 0, int(str(year)[:2])
    if c % 2:
        l = -1
    if not (c-2) % 4:
        l = -1
    if not c % 3:
        if not (c-17) % 25:
            s = 0
        else:
            s = 1
    if not (c-18) % 25:
        s = 1
    return l + s


def epact_build(adjust=int) -> list:
    build_base, day, x = [], 1, 0
    while x != 19:
        day += 11*(x if x == 0 else 1)
        if day > 30:
            day -= 30
        build_base.append(day)
        x += 1
    build = []
    for y in build_base:
        y += adjust
        if y > 31:
            y -= 31
        elif y <= 0:
            y += 31
        build.append(y)
    return build


def epact(year=int) -> str:
    e, base, i = '', 1600, 0
    while year >= base:
        i += epact_adjust(year)
        year -= 100
    epact_list = epact_build(i)
    e = interger_to_roman(epact_list[golden_number(year)-1])
    if e == 'XXXI':
        e = '*'
    return e
```
## Letter of the Martyrology

Still working on this one.