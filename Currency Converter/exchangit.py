"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: HOANG THAI AN TRAN
Date: 08/29/24
"""

import currency


def main():
    src = input("3-letter code for original currency: ")
    dst = input("3-letter code for the new currency: ")
    amt = input("Amount of the original currency: ")

    assert currency.iscurrency(src) == True
    assert currency.iscurrency(dst) == True

    url = currency.service_response(src, dst, amt)

    assert currency.has_error(url) == False
    assert type(currency.exchange(src, dst, amt)) == float

    src_amt = currency.before_space(currency.get_src(url))

    exc = round(currency.exchange(src, dst, amt), 3)

    print("You can exchange " + src_amt + " " + src
          + " for " + str(exc) + " " + dst + ".")


main()
