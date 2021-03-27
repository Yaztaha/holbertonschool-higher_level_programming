#!/usr/bin/python3
"""Tests for Rectangle class"""


import contextlib
import importlib
import io
import models.base
import models.rectangle
import unittest


Rectangle = models.rectangle.Rectangle


class RectangleTests(unittest.TestCase):
    """Tests for Rectangle class"""

    def setUp(self):
        """Refresh Rectangle module for each test"""

        importlib.reload(models.base)
        importlib.reload(models.rectangle)

    def test_Area(self):
        """Compare width and height to result of area method"""

        r = Rectangle(10, 5)
        with self.subTest():
            self.assertEqual(r.area(), 50)
        r.width = 3
        r.height = 7
        with self.subTest():
            self.assertEqual(r.area(), 21)

    def test_Display(self):
        """Test the display module"""

        out = io.StringIO()
        r = Rectangle(4, 6)
        result = "####\n####\n####\n####\n####\n####\n"
        with self.subTest():
            with contextlib.redirect_stdout(out):
                r.display()
            self.assertEqual(out.getvalue(), result)
        out.truncate(0)
        out.seek(0)
        r.width = 2
        r.height = 3
        r.x = 3
        r.y = 2
        result = "\n\n   ##\n   ##\n   ##\n"
        with self.subTest():
            with contextlib.redirect_stdout(out):
                r.display()
            self.assertEqual(out.getvalue(), result)

    def test_TooFewArgs(self):
        """Test for too few args to init"""

        msg = "__init__() missing 1 required positional argument: 'height'"
        with self.assertRaises(TypeError, msg=msg):
            Rectangle(1)

    def test_TooManyArgs(self):
        """Test for too many args to init"""

        msg = "__init___() takes from 3 to 6 positional arguments but 7" \
            "were given"
        with self.assertRaises(TypeError, msg=msg):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_toStr(self):
        """Testing converting rectangle to a string"""

        r = Rectangle(1, 2, 3, 4)
        res = "[Rectangle] (1) 3/4 - 1/2"
        with self.subTest():
            self.assertEqual(str(r), res)
        r.x = 20
        r.y = 20
        res = "[Rectangle] (1) 20/20 - 1/2"
        with self.subTest():
            self.assertEqual(str(r), res)
        r = Rectangle(5, 6, 7, 8, 9)
        res = "[Rectangle] (9) 7/8 - 5/6"
        with self.subTest():
            self.assertEqual(str(r), res)
        r.width = 9
        r.height = 12
        res = "[Rectangle] (9) 7/8 - 9/12"
        with self.subTest():
            self.assertEqual(str(r), res)

    def test_Update(self):
        """Testing update method"""

        r = Rectangle(1, 2, 3, 4)
        args = (
            ("id", "id"), ("width", 1), ("height", 2), ("x", 3), ("y", 4),
            ("extra", 0)
        )
        dic = r.to_dictionary()
        for i in range(len(args)):
            ar = args[:i + 1]
            if i < len(args) - 1:
                dic.update(ar)
            with self.subTest():
                r.update(*(val for _, val in ar))
                self.assertEqual(r.to_dictionary(), dic)
        r.update("99", width=10)
        dic["id"] = "99"
        with self.subTest():
            self.assertEqual(r.to_dictionary(), dic)
        r.update("99", 1, 2, 3, 4)
        dic = r.to_dictionary()
        for i in range(len(args)):
            ar = args[:i + 1]
            if i < len(args) - 1:
                dic.update(ar)
            with self.subTest():
                r.update(**dict(ar))
                self.assertEqual(r.to_dictionary(), dic)

    def test_toDict(self):
        """Tests converting rectangles to a dictionary"""

        r = Rectangle(1, 2, 3, 4)
        d = {'id': 1, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        with self.subTest():
            self.assertEqual(r.to_dictionary(), d)
        r.id = 'id'
        r.width = 30
        r.height = 20
        r.x = 50
        d['id'] = 'id'
        d['width'] = 30
        d['height'] = 20
        d['x'] = 50
        with self.subTest():
            self.assertEqual(r.to_dictionary(), d)
            
