import os
import shutil
import unittest

import requests

pkg_link = "https://github.com/Krande/blender_addons/releases/download/latest/bl_measure.zip"


def download_to(destination, url):
    import urllib.request

    os.makedirs(os.path.dirname(destination), exist_ok=True)

    if os.path.isfile(destination) is False:
        with urllib.request.urlopen(url) as response, open(destination, "wb") as out_file:
            shutil.copyfileobj(response, out_file)


class MyTestCase(unittest.TestCase):
    def test_query_asset_simple(self):
        api_url = "https://api.github.com/repos/Krande/blender_addons/releases/latest"
        r = requests.get(api_url)
        content = r.json()
        tag_name = content["tag_name"]
        download_url = content["assets"][0]
        release = tag_name.split("_")[-1]
        print(release)

    def test_download_asset(self):
        download_to("c:/temp/bl_measure.zip", pkg_link)


if __name__ == "__main__":
    unittest.main()
