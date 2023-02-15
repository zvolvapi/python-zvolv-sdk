from distutils.core import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

__version__ = None
exec(open(f"{here}/slack_sdk/version.py").read())

long_description = ""
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as readme:
    long_description = readme.read()


setup(
    name = 'zvolv_sdk',         # How you named your package folder (MyLib)
    version=__version__,
    packages = ['zvolv_sdk'],   # Chose the same as "name"
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'The Zvolv API Platform SDK for Python',   # Give a short description about your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Akshay Jadhav',                   # Type in your name
    author_email = 'akshay@zvolv.com',      # Type in your E-Mail
    python_requires=">=3.6.0",
    url = 'https://github.com/zvolvapi/python-zvolv-sdk',   # Provide either the link to your github or to your website
    download_url = 'https://github.com/zvolvapi/python-zvolv-sdk/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['zvolv', 'zvolv-api', 'web-api', 'sdk', 'rest-api-client'],   # Keywords that define your package best
    install_requires=[            # I get to this in a second
        'validators',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)