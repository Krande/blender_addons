import unittest
import os
import shutil
import requests
from pprint import pprint

# pkg_link = "https://github.com/Krande/blender_addons/releases/download/master_0.0.1/bl_measure.zip"
pkg_link = "https://github.com/Krande/blender_addons/releases/download/bl_measure_0.0.1/bl_measure.zip"

def download_to(destination, url):
    import urllib.request

    os.makedirs(os.path.dirname(destination), exist_ok=True)

    if os.path.isfile(destination) is False:
        with urllib.request.urlopen(url) as response, open(destination, "wb") as out_file:
            shutil.copyfileobj(response, out_file)

class MyTestCase(unittest.TestCase):
    def test_download_asset(self):
        url = "https://api.github.com/repos/{owner}/{repo}/releases/assets"
        url = pkg_link
        headers = {
            "accept": "application/vnd.github.v3+json",
            "token": ""
        }
        # r = requests.get(url, params=dict(owner='Krande', repo='blender_addons'), headers=headers).json()
        download_to('c:/temp/bl_measure.zip', pkg_link)
        # pprint(r)



if __name__ == "__main__":
    unittest.main()
