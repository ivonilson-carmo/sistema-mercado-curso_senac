def showTitleCustom(*text):
    print()
    print('=' * 34)
    for item in text:
        print(item)
    print('=' * 34)

def showTitleCenterCustom(center_size, *text):
    print()
    print('=' * 34)
    for item in text:
        print(f'{item}'.center(center_size))
    print('=' * 34)