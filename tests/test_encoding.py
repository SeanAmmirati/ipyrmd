from .test_basic import *

ENCODING_1 = 'cp1252'
ENCODING_2 = 'ASCII'
ENCODING_3 = 'ISO-8859-1'

class TestRmdCP2125(TestRmdBasic):
   default_encoding = ENCODING_1

class TestRmdASCII(TestRmdBasic):
   default_encoding = ENCODING_2

class TestRmdUTF16(TestRmdBasic):
   default_encoding = ENCODING_3

class TestSpinCP2125(TestSpinBasic):
    default_encoding = ENCODING_1

class TestSpinASCII(TestSpinBasic):
    default_encoding = ENCODING_2
    
class TestSpinUTF16(TestSpinBasic):
    default_encoding = ENCODING_3

class TestIpynbCP2125(TestIpynbBasic):
    default_encoding = ENCODING_1

class TestIpynbASCII(TestIpynbBasic):
    default_encoding = ENCODING_2

class TestIpynbUTF16(TestIpynbBasic):
    default_encoding = ENCODING_3

class TestRmdRepeatCP2125(TestRmdRepeat):
    default_encoding = ENCODING_1

class TestRmdRepeatASCII(TestRmdRepeat):
    default_encoding = ENCODING_2

class TestRmdRepeatUTF16(TestRmdRepeat):
    default_encoding = ENCODING_3
