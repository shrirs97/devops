import unittest


class TestApplication(unittest.TestCase):

    def test_application(self):
        name = "VVCE"
        self.assertEqual(name, "VVCE")
        print("Hello")
       


if __name__ == "__main__":
    unittest.main()
