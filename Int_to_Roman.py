def int_to_roman(num):
    roman = [[1, 'I'], [5, 'V'], [10, 'X'], [50, 'L'], [100, 'C'],
             [500, 'D'], [1000, 'M']]
    d = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    num = num[-1::-1]
    s = ''
    for i in range(0, len(num)):
        x = int(num[i]) * (10 ** i)
        if x == 0:
            continue
        if d.get(x, 0):
            g = d.get(x)
            s = f'{g}{s}'
            continue
        else:
            ro = roman[i * 2:i + 3 + 1]
            if x < ro[1][0]:
                h = ro[0][0] * 3
                if x <= h:
                    m = ro[0][1]
                    g = f'{m * (x // ro[0][0])}'
                    s = f'{g}{s}'
                else:
                    m = ro[1][0] - x
                    k = (m // ro[0][0]) * ro[0][1]
                    g = f'{k}{ro[1][1]}'
                    s = f'{g}{s}'
            else:
                p = ro[1][1]
                h = ro[0][0] * 3
                print(f'h={h}')
                if x - ro[1][0] <= h:
                    m = ro[0][1]
                    print(m)
                    g = f'{m * ((x - ro[1][0]) // ro[0][0])}'
                    s = f'{p}{g}{s}'
                else:
                    if x >= 900:
                        ro = roman[i * 2:i + 3 + 2]
                    m = ro[2][0] - x
                    print(f'm={m}')
                    k = (m // ro[0][0]) * ro[0][1]
                    g = f'{k}{ro[2][1]}'
                    s = f'{g}{s}'

    print(s)
if __name__=="__main__":
    int_to_roman(input("enter the number"))

