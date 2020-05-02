import sys
from io import StringIO
import unittest


def resolve():
    import math

    a, b, n = map(int, input().split())
    if n < b:
        print(math.floor(a * n / b))
    else:
        print(math.floor(a * (b - 1) / b))


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
        input = """5 7 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11 10 9"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
