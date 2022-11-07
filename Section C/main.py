# Converter for turning an integer into it's word-format equivalent
def num_to_word(num):
    """
    Below are the numbers 1-20, and then 30-90 counting in 10s. 1000s are also included. (E.g: thousand, million, etc.)
    Each integer is respectfully assigned to it's string/ word. (E.g: 11: "eleven")
    These are all core values needed to construct a number in word format.
    With them we can get the word for pretty much any number.
    """
    digits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
              6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
              11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
              15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
              19: 'nineteen', 20: 'twenty',
              30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
              70: 'seventy', 80: 'eighty', 90: 'ninety'}
    thousand = 1000
    million = thousand * 1000
    billion = million * 1000
    trillion = billion * 1000

    """
    Below are the if-statements and calculations needed to construct the number in word format.
    Inside them are additional if/ else-statements that determine whether or not the number is complete.
    """

    # If the value is below 0, then only an error message will be displayed.
    if num < 0:
        return "Please insert a value of 0 or above"

    # If the value is too high, then only an error message will be displayed.
    if num > 999999999999999:
        return "Please a number of lower value"

    # 20 and below
    if num < 20:
        return digits[num]

    # Tens
    if num < 100:
        if num % 10 == 0:
            return digits[num]
        else:
            return digits[num // 10 * 10] + '-' + digits[num % 10]

    # Hundreds
    if num < thousand:
        if num % 100 == 0:
            return digits[num // 100] + ' hundred'
        else:
            return digits[num // 100] + ' hundred and ' + num_to_word(num % 100)

    # Thousands
    if num < million:
        if num % thousand == 0:
            return num_to_word(num // thousand) + ' thousand'
        else:
            return num_to_word(num // thousand) + ' thousand and ' + num_to_word(num % thousand)

    # Millions
    if num < billion:
        if (num % million) == 0:
            return num_to_word(num // million) + ' million'
        else:
            return num_to_word(num // million) + ' million, ' + num_to_word(num % million)

    # Billions
    if num < trillion:
        if (num % billion) == 0:
            return num_to_word(num // billion) + ' billion'
        else:
            return num_to_word(num // billion) + ' billion, ' + num_to_word(num % billion)

    # Trillions
    if num % trillion == 0:
        return num_to_word(num // trillion) + ' trillion'
    else:
        return num_to_word(num // trillion) + ' trillion, ' + num_to_word(num % trillion)


"""
Printing some numbers to give you an example of how the function works.
I only put the print function in the same file to make the explanation simple.
"""
print(num_to_word(90376000010012))
print(num_to_word(-1))
print(num_to_word(999999999999999))
