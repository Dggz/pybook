
# Testing
import errno
import unittest
import io
import example

from io import StringIO
from unittest.mock import patch


sample_data = io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
\r
''')


class Tests(unittest.TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            example.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)

    @patch('example.urlopen', return_value=sample_data)
    def test_dowprices(self, mock_urlopen):
        p = example.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                         {'IBM': 91.1,
                          'AA': 13.25,
                          'MSFT': 27.72})

    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')

    def test_bad_int_ctx(self):
        with self.assertRaisesRegex(ValueError, 'invalid literal .*'):
            r = parse_int('N/A')

    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail('IOError not raised')


# A simple function to illustrate
def parse_int(s):
    return int(s)

import sys
def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out,verbosity=verbosity).run(suite)

if __name__ == '__main__':
    with open('testing.out', 'w') as f:
        main(f)

"""

The interesting thing about this recipe is not so much the task of getting test 
results redirected to a file, but the fact that doing so exposes some notable 
inner workings of the unittest module.

At a basic level, the unittest module works by first assembling a test suite. 
This test suite consists of the different testing methods you defined. 
Once the suite has been assembled, the tests it contains are executed.

These two parts of unit testing are separate from each other. 
The unittest.TestLoader instance created in the solution is used to assemble a 
test suite. The loadTestsFromModule() is one of several methods it defines to 
gather tests. In this case, it scans a module for TestCase classes and extracts 
test methods from them. If you want something more fine-grained, the 
loadTestsFromTestCase() method (not shown) can be used to pull test methods 
from an individual class that inherits from TestCase.

The TextTestRunner class is an example of a test runner class. The main purpose 
of this class is to execute the tests contained in a test suite. This class is 
the same test runner that sits behind the unittest.main() function. However, 
here we’re giving it a bit of low-level configuration, including an output file 
and an elevated verbosity level.

Although this recipe only consists of a few lines of code, it gives a hint as 
to how you might further customize the unittest framework. To customize how 
test suites are assembled, you would perform various operations using the 
TestLoader class. To customize how tests execute, you could make custom test 
runner classes that emulate the functionality of TextTestRunner. Both topics 
are beyond the scope of what can be covered here. However, documentation for 
the unittest module has extensive coverage of the underlying protocols. 

"""


# if __name__ == '__main__':
#     unittest.main()
