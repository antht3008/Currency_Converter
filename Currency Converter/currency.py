"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: HOANG THAI AN TRAN
Date: 08/29/2024
"""

import introcs

APIKEY = 'HLugVC8ROW2Tp47dsdhA8edzynsHBX6yQpMPE9u2poQe'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    pass

    assert introcs.count_str(s, ' ') > 0

    coma_pos = introcs.index_str(s, ' ')
    slice_before = s[:coma_pos]
    return slice_before


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    pass

    assert introcs.count_str(s, ' ') > 0

    coma_pos = introcs.index_str(s, ' ')
    slice_after = s[coma_pos + 1:]
    return slice_after


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """
    assert introcs.count_str(s, '"') > 1

    first_quote = introcs.index_str(s, '"')
    second_quote = introcs.index_str(s, '"', first_quote + 1)
    slice_quote = s[first_quote + 1:second_quote]
    return slice_quote


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    pass

    src_pos = introcs.find_str(json, 'src') + 4
    slice_after_src = json[src_pos + 1:]
    src = first_inside_quotes(slice_after_src)
    return src


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    pass

    dst_pos = introcs.find_str(json, 'dst') + 4
    slice_after_dst = json[dst_pos + 1:]
    dst = first_inside_quotes(slice_after_dst)
    return dst


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    pass

    error_pos = introcs.find_str(json, 'error') + 5
    slice_error = first_inside_quotes(json[error_pos + 1:])

    isTrue = introcs.isalpha(slice_error[0:2])

    return isTrue


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

        '{"success": true, "src": "<src-amount>", "dst": "<dst-amount>", "error": ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    choose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition: src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition: dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float or int
    """
    assert introcs.isfloat(str(amt)) == True
    assert introcs.isalpha(src) == True
    assert introcs.isalpha(dst) == True

    url = 'https://ecpyfac.ecornell.com/python/currency/fixed?src='
    url = url + src + '&dst=' + dst + '&amt=' + str(amt)
    url = url + '&key=HLugVC8ROW2Tp47dsdhA8edzynsHBX6yQpMPE9u2poQe'

    return introcs.urlread(url)


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    pass

    assert introcs.isalpha(currency) == True

    url = service_response(currency, 'USD', 2)
    error = not (has_error(url))

    return error


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition: src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition: dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition: amt is a float or int
    """

    assert iscurrency(src) == True
    assert iscurrency(dst) == True
    assert introcs.isfloat(str(amt)) == True

    url = service_response(src, dst, amt)
    currency_to = get_dst(url)
    currency_to = before_space(currency_to)
    return float(currency_to)


