def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    summ = '{}{}{}'.format(one, delimiter, two)
    return summ.upper()
print(get_summ("Learn","Python"))

