from tkinter import filedialog
from utils.Utils import get_path

class Selector():
    def select_file(self) -> str:
        """
        Selects a file using a file dialog and returns the path of the selected file.

        Returns:
            str: The path of the selected file.
        """
        filename = filedialog.askopenfiles(
            defaultextension=".jpg", 
            filetypes=[("JPG Files", "*.jpg"), ("PNG Files", "*.png")]
        )
        return get_path(filename)
