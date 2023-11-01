from cv2 import imread, imshow, waitKey, destroyAllWindows, UMat

class Display():
    def display_image(self, image):
        """
        Display an image.

        Args:
            image_path (str): The path to the image file.

        Returns:
            None
        """
        # Display the image
        imshow("image", image)

        # Wait for a key press
        waitKey(0)

        # Close all windows
        destroyAllWindows()

    def read_image(self, image_path: str):
        return imread(image_path)
