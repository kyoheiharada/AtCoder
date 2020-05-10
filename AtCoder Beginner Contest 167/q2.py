import sys
from io import StringIO
import unittest


def resolve():
    a, b, c, k = map(int, input().split())
    if a >= k:
        print(k)
    elif a + b >= k:
        print(a)
    else:
        print(a - (k - a - b))


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """2 1 1 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2000000000 0 0 2000000000"""
        output = """2000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
