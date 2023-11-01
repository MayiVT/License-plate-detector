import cv2
import imutils
import pytesseract

from utils.default_values import T_TESSERACT_PATH
from utils.Utils import Config

from modules.file_selector import Selector
from modules.display import Display

class LPD:
    def __init__(self):
        tesseract_path = Config.get_config(Config(), T_TESSERACT_PATH)
        print(tesseract_path)
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

        display = Display()

        img_path = Selector().select_file()
        image = Display.read_image(Display(), img_path)
        display.display_image(image)

        convert_to_gray = self.convert_to_gray(image)
        display.display_image(convert_to_gray)

        reduce_noise = self.reduce_noise(convert_to_gray)
        display.display_image(reduce_noise)

    def convert_to_gray(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    def reduce_noise(self, img):
        return cv2.bilateralFilter(img, 11, 17, 17)
