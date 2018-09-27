from .test_basic import TestIpynbBasic, TestRmdBasic, TestRmdRepeat, TestSpinBasic

ENCODING_1 = 'cp1252'
ENCODING_2 = 'ASCII'
ENCODING_3 = 'ISO-8859-1'

rmd_repeat = """markdown-0
```{r}
code-1
```

```{r}
code-2
```
```{r}
code-3
```"""

spin_basic = """#' markdown-0-0
#' markdown-0-1

code-1

#' markdown-2-0
#' markdown-2-1

code-3-0
code-3-1
code-3-2
"""

rmd_basic = """markdown-0-0
markdown-0-1

```{r}
code-1
```

markdown-2-0
markdown-2-1

```{r}
code-3-0
code-3-1
code-3-2
```"""

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