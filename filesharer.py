import os
# To upload files to https://www.filestack.com/
from filestack import Client
# To load the variables from the .env file.
from dotenv import load_dotenv


class FileSharer:
    """
        To upload a file to https://www.filestack.com/.
    """
    load_dotenv()
    # Get an API key from https://www.filestack.com/
    FILESTACK_API_KEY = os.getenv("FILESTACK_API_KEY")

    def __init__(self, filepath, api_key=FILESTACK_API_KEY):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)

        file_link = client.upload(filepath=self.filepath)
        return file_link.url
