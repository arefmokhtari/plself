#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
from math import ceil
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def crtiktok(numbers: list) -> list:
    c = 0
    num = []
    for i in numbers:
        if c > 7: break
        for j in numbers:
            num.append(i+j)
        c += 1
    return num
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
num = crtiktok('⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹'.split())
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def gregorian_to_jalali(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    if (gm > 2):
        gy2 = gy + 1
    else:
        gy2 = gy
    days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
    jy = -1595 + (33 * (days // 12053))
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if (days > 365):
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if (days < 186):
        jm = 1 + (days // 31)
        jd = 1 + (days % 31)
    else:
        jm = 7 + ((days - 186) // 30)
        jd = 1 + ((days - 186) % 30)
    return [jy, jm, jd]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def crtime(hour: int, minute: int) -> str: 
    return '﹕'.join([num[hour], num[minute]])
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def crbiotime(hour: int) -> str:
    return ' - { '+['🕛', '🕐', '🕑', '🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙', '🕚'][hour]+' }'
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def jdmonthname(month: int) -> str:
    return ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar', 'Mehr', 'Aban', 'Azar', 'Dey', 'Bahman','Esfand'][month-1]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def send_seasons(month: int, ptn: str = 'm') -> str:
    return ['Spring', 'Summer', 'Fall', 'winter'][(ceil(month/3))-1] if ptn == 'm' else ['Bahar', 'Tabestan', 'Paiiz', 'Zemeston'][(ceil(month/3))-1]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
def send_weekday(day: int) -> str:
    return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][day]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #