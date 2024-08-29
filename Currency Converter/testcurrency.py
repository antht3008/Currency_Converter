"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: HOANG THAI AN TRAN
Date: 08/29/2024
"""

import introcs
import currency

def test_before_space():

    """Test procedure for before_space"""

    result = currency.before_space('2.324 USD')
    introcs.assert_equals('2.324', result)

    print('Testing before_space')

    result = currency.before_space('12.234  USD')
    introcs.assert_equals('12.234', result)

    result = currency.before_space('12.3 2 USD')
    introcs.assert_equals('12.3', result)

    result = currency.before_space(' 12.34USD')
    introcs.assert_equals('', result)


def test_after_space():

    """Test procedure for after_space"""

    print('Testing after_space')

    result = currency.after_space('2.324 USD')
    introcs.assert_equals('USD', result)

    result = currency.after_space('12.234  USD')
    introcs.assert_equals(' USD', result)

    result = currency.after_space('12.3 2 USD')
    introcs.assert_equals('2 USD', result)

    result = currency.after_space('12.34USD ')
    introcs.assert_equals('', result)


def test_first_inside_quotes():

    """Test procedure for first_inside_quotes"""

    print('Testing first_inside_quotes')

    result = currency.first_inside_quotes('A " B " C D')
    introcs.assert_equals(' B ', result)

    result = currency.first_inside_quotes('""""""')
    introcs.assert_equals('', result)

    result = currency.first_inside_quotes('"     "')
    introcs.assert_equals('     ', result)

    result = currency.first_inside_quotes('A " " B " C " D')
    introcs.assert_equals(' ', result)


def test_get_src():

    """Test procedure for get_src"""

    print('Testing get_src')

    result = currency.get_src(
            '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)

    result = currency.get_src(
             '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars', result)

    result = currency.get_src(
             '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    result = currency.get_src(
             '{"success":false,"src":  "","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_get_dst():

    """Test procedure for get_dst"""

    print('Testing get_dst')

    result = currency.get_dst(
            '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)

    result = currency.get_dst(
             '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros', result)

    result = currency.get_dst(
             '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)

    result = currency.get_dst(
             '{"success":false,"src":  "","dst":  "","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_has_error():

    """Test procedure for has_error"""

    print('Testing has_error')

    result = currency.has_error(
             '{"success" :false,"src":  "","dst":  "","error":"Source currency code is invalid."}')
    introcs.assert_equals(True, result)

    result = currency.has_error(
             '{"success":  false,"src":  "","dst":  "","error":  "Source currency code is invalid."}')
    introcs.assert_equals(True, result)

    result = currency.has_error(
             '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals(False, result)

    result = currency.has_error(
             '{"success":true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error":""}')
    introcs.assert_equals(False, result)


def test_service_response():

    """Test procedure for service_response"""

    print('Testing service_response')

    result = currency.service_response('USD', 'EUR', 1)
    introcs.assert_equals(
        '{"success": true, "src": "1.0 United States Dollar", "dst": "0.886407 Euros", "error": ""}'
        , result)

    result = currency.service_response('USD', 'EUR', -2)
    introcs.assert_equals(
        '{"success": true, "src": "-2.0 United States Dollars", "dst": "-1.772814 Euros", "error": ""}'
        , result)

    result = currency.service_response('UDD', 'EUR', -2)
    introcs.assert_equals(
        '{"success": false, "src": "", "dst": "", "error": "The rate for currency UDD is not present."}'
        , result)

    result = currency.service_response('usd', 'EAR', 2.32)
    introcs.assert_equals(
        '{"success": false, "src": "", "dst": "", "error": "The rate for currency EAR is not present."}'
        , result)


def test_iscurrency():

    """Test procedure for iscurrency"""

    print('Testing iscurrency')

    result = currency.iscurrency('USD')
    introcs.assert_equals(True, result)

    result = currency.iscurrency('usd')
    introcs.assert_equals(True, result)

    result = currency.iscurrency('USDASD')
    introcs.assert_equals(False, result)


def test_exchange():

    """Test procedure for exchange"""

    print('Testing exchange')

    result = currency.exchange('USD', 'EUR', 2)
    introcs.assert_floats_equal(1.772814 ,result)

    result = currency.exchange('USD', 'EUR', -2)
    introcs.assert_floats_equal(-1.772814 ,result)


#Script code
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print('All tests completed successfully.')