import unittest

class TestStringMethods(unittest.TestCase):

    def test_read_image_1(self):
        # get the function to read image and check if image exists, if exists = true
        self.assertTrue(true)

    def test_detect_license_plate(self):
        # get the image and check if there is a license plate detected
        self.assertTrue(true)

    def test_text_license_plate(self):
        # get the text from the license plate
        self.assertEqual("test license plate")

if __name__ == '__main__':
    unittest.main()