
# Maya Murphy

from functools import reduce

""" COFFEE SIZE """

size = input('Do you want small, medium, or large? ').lower()
sizeList = ["small", "medium", "large"]
checkSize = False if size in sizeList else True

# If size coffee is not clear, reconfirm size.
while (checkSize):
    if (size not in sizeList):
        print('')
        print('I\'m sorry I did not get that.')
        size = input('Did you want a small, medium, or large? ').lower()
    else:
        checkSize = False


""" COFFEE TYPE """

type = input('Do you want brewed, espresso, or cold press? ').lower()
typeList = ['brewed', 'espresso', 'cold press']
checkType = False if type in typeList else True

# If coffee type is not clear, reconfirm type.
while (checkType):
    if (type not in typeList):
        print('')
        print('I\'m sorry I did not get that.')
        type = input('Did you want brewed, espresso, or cold press?').lower()
    else:
        checkType = False


""" FLAVOR """

getChoice = input('Do you want a flavored syrup? (yes or no) ').lower()
choices = ['yes', 'no']
checkChoice = False if getChoice in choices else True

# If choice to add flavor is not clear, reconfirm choice.
while (checkChoice):
    if (getChoice not in choices):
        print('')
        print('I\'m sorry I did not get that.')
        getChoice = input(
            'Did you want a flavored syrup? (yes or no) ').lower()
    else:
        checkChoice = False

flavor = ''
if getChoice == 'yes':
    flavor = input('Hazelnut, vanilla, or caramel? ')
    print('')
    msg = 'You asked for a {} cup of {} coffee with {} syrup.'.format(
        size, type, flavor)
elif getChoice == 'no':
    print('')
    msg = 'You asked for a {} cup of {} coffee.'.format(size, type)


""" ORDER SUMMARY """

print(msg)
options = [size, type, getChoice]
cost = {
    'small': 2,
    'medium': 3,
    'large': 4,
    'brewed': 0,
    'espresso': .50,
    'cold press': 1,
    'yes': .50,
    'no': 0
}

itemizedCost = list(map(lambda option: cost[option], options))
total = reduce(lambda a, b: a + b, itemizedCost)
subtotal = total
tipMsg = subtotal + (subtotal * .15)
print('Your cup of coffee costs $ {}'.format(total))
print('The price with a tip is $ {}'.format(tipMsg))
