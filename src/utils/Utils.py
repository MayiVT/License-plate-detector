import re
import os
from configparser import ConfigParser
from utils.default_values import PLEASE_UPDATE, CONFIG, T_TESSERACT_PATH, DEFAULT_PATH

def get_path(filename):
    """
    Given a filename, this function searches for a substring enclosed in single quotes
    and returns it. If no such substring is found, an empty string is returned.
    
    :param filename: A string representing the name of a file.
    :return: A string representing the substring enclosed in single quotes in the 
             filename, or an empty string if no such substring is found.
    """
    result = re.search(r"name='(.*?)'", str(filename))
    if result:
        return str(result.group(1))
    else:
        return ""
    
class Config():
    def __init__(self):
        """
        Initializes the object.

        This function checks if the CONFIG file exists. If it does not exist, it calls the create_config() function to create the config file and prints a message asking the user to update it. If the CONFIG file exists, it calls the check_config() function.

        Parameters:
        None

        Returns:
        None
        """
        if not os.path.exists(CONFIG):
            self.create_config()
            print(PLEASE_UPDATE)
            exit(0)
        else:
            self.check_config()

    def get_config(self, path: str) -> str:
        """
        Reads a configuration file and returns the value of a specified path.

        Args:
            path (str): The path to the configuration value.

        Returns:
            str: The value of the specified path in the configuration file.
        """
        config = ConfigParser()

        # Read the file in the main directory
        config.read(CONFIG)
        return str(config["DEFAULT"][path])
    
    def create_config(self):
        """
        Creates a new configuration file with default settings.

        This function initializes a new ConfigParser object and sets the default
        installation path to the value of DEFAULT_PATH. It then writes the
        configuration to a file named CONFIG.

        Parameters:
            self: The instance of the class.

        Returns:
            None
        """
        
        config = ConfigParser()

        config["DEFAULT"] = {
            T_TESSERACT_PATH: DEFAULT_PATH,
        }

        with open(CONFIG, "w") as config_file:
            config.write(config_file)

    def check_config(self):
        """
        Check the configuration and perform necessary actions based on the configuration.

        This function checks the configuration value of the T_INSTALL_PATH key. If the value is not equal to the DEFAULT_PATH, the function does nothing. Otherwise, it prints the PLEASE_UPDATE message and exits the program.

        Parameters:
            self (object): The instance of the class.

        Returns:
            None
        """
        if self.get_config(T_TESSERACT_PATH) != DEFAULT_PATH:
            pass
        else:
            print(PLEASE_UPDATE)
            exit(0)