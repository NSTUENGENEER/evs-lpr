import os
import re
import setuptools


def read_version():
    # importing gpustat causes an ImportError :-)
    __PATH__ = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(__PATH__, 'modelevs_client/__init__.py')) as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  f.read(), re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find __version__ string")


# get project version
__version__ = read_version()

# get project long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# get project requirements list
with open("requirements.txt", "r", encoding="utf-8") as fh:
    packages = fh.read().split("/n")

setuptools.setup(
    name="modelevs-client",
    version=__version__,
    author='',
    author_email='timeviewereltex@yandex.ru',
    description="NSTU tools package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NSTUENGENEER/modelevs-client.git",
    packages=setuptools.find_packages(),
    install_requires=packages,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
    ],
    keywords='modelevs',
    entry_points={
        'console_scripts': ['modelevs_client=modelevs_client:main'],
    },
    python_requires='>=3.6'
)
