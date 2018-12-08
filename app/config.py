import re


class Config:
    def __init__(self, file):
        """
            :param file: Path to .env file
        """
        self.file = file
        self.config = dict()
        self.load()

    def __getitem__(self, key):
        """
            Get configuration file entry
            :param key: Name of configuration entry
            :return: Value of configuration entry selected by key
        """
        return self.config[key]

    def load(self):
        """
            Load configuration from .env file
            :return:
        """
        pattern = r'([A-Z0-9_-]+)=([^\n]+)'
        with open(self.file, 'r') as file:
            content = file.readlines()
            for line in content:
                match = re.match(pattern, line)
                if match:
                    self.config[match[1]] = match[2]
