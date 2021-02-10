import unittest
import requests
from pprint import pprint

pkg_link = "https://github.com/Krande/blender_addons/releases/download/master_0.0.1/bl_measure.zip"


class MyTestCase(unittest.TestCase):
    def test_download_asset(self):
        url = "https://api.github.com/repos/{owner}/{repo}/releases/assets"
        headers = {
            "accept": "application/vnd.github.v3+json",
            "token": ""
        }
        r = requests.get(url, params=dict(owner='Krande', repo='blender_addons'), headers=headers).json()

        pprint(r)



if __name__ == "__main__":
    unittest.main()
