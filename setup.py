import io
import os
from setuptools import setup




__version__ = '1.0.0'
__author__ = 'Ivan Pilipovic'

description = 'Scrape picture and/or videos from Instagram. Scrape by username or hashtag.'
here = os.path.abspath(os.path.dirname(__file__))

# load requirements
with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

setup(
    name='instagram_py',
    version=__version__,
    description=description,
    long_description=documentation,
    author=__author__,
    author_email='contact.timgrossmann@gmail.com',
    packages=['instapy'],
    py_modules='instapy',
    license="GPLv3",
    keywords=["instagram", "automation", "scrape", "download picture", "download video", "bot"],
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Environment :: Console",
                 "Environment :: Win32 (MS Windows)",
                 "Environment :: MacOS X",
                 "Environment :: Web Environment",
                 "Environment :: Other Environment :: VPS",
                 "Intended Audience :: End Users/Desktop",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: GNU General Public License v3",
                 "Operating System :: Microsoft :: Windows",
                 "Operating System :: POSIX :: Linux",
                 "Operating System :: MacOS :: MacOS X",
                 "Operating System :: Unix",
                 "Programming Language :: Python",
                 "Programming Language :: JavaScript",
                 "Programming Language :: SQL",
                 "Topic :: Internet :: Browsers",
                 "Topic :: Other/Nonlisted Topic :: Automation :: Selenium",
                 "Topic :: Utilities",
                 "Natural Language :: English"],
    install_requires=dependencies,
    extras_require={"test":["pytest", "tox"]},
    include_package_data=True,
    python_requires=">=2.7",
    platforms=["win32", "linux", "linux2", "darwin"]
    )



