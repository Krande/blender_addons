import sys
import os
import pathlib
import subprocess
import requests
import tarfile
import bz2
import io

CF = "https://anaconda.org/conda-forge/"


def download_to(url, destination_dir):
    destination_dir = pathlib.Path(destination_dir)
    os.makedirs(destination_dir, exist_ok=True)

    response = requests.get(url)
    with tarfile.open(response.content) as tar:
        tar.extractall(destination_dir)



# blender_python = os.environ.get("BLENDER_PY", r"C:\Program Files\Blender Foundation\Blender 3.3\3.3\python")
blender_python = os.environ.get("BLENDER_PY", r"C:\Program Files\Blender Foundation\Blender 3.4\3.4\python")
python_prefix = os.environ.get("pythonLocation", blender_python)

target = pathlib.Path(__file__).parent / "addons/bl_stru_utils/libs/site/packages"
platform = sys.platform
if platform == "win32":
    python_exe = os.path.join(python_prefix, "bin", "python.exe")
# elif sys.platform in ["linux", "linux2"]:
else:
    python_exe = os.path.join(python_prefix, "bin", "python")
pyver = subprocess.run([python_exe, '--version'], capture_output=True, encoding='utf8').stdout.split()[-1]
print(f'Blender Python "{pyver}"')
subprocess.call([python_exe, "-m", "ensurepip"])
subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

# Install pip packages
packages = ["azure.identity", "azure-storage-queue"]
subprocess.call([python_exe, "-m", "pip", "install", "-U", *packages, "-t", target])

# Install conda packages
occ_762_win_py310 = CF + "pythonocc-core/7.6.2/download/win-64/pythonocc-core-7.6.2-py310hf04ff9d_0.tar.bz2"
download_to(occ_762_win_py310, "temp")
print("FINISHED")
