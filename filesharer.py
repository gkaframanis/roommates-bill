import os
from filestack import Client
from dotenv import load_dotenv


class FileSharer:

    load_dotenv()
    YOUR_API_KEY = os.getenv("YOUR_API_KEY")

    def __init__(self, filepath, api_key=YOUR_API_KEY):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)

        file_link = client.upload(filepath=self.filepath)
        return file_link.url
