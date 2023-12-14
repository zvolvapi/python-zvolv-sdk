

# Packaging Python Project User Guide
This user guideline walks you through how to package a simple Python project. It will show you how to add the necessary files and structure to create the package, how to build the package, and how to upload it to the Python Package Index (PyPI).




Some of the commands require a newer version of pip, so start by making sure you have the latest version installed:
```
python3 -m pip install --upgrade pip
```
## Requirement Installtion
```
 - pip install pytest
 - pip install coverage
 - pip install wheel
```

## Run Test Case
```
 - python3 -m pytest
    or 
 - pytest
```

## Run tests with coverage
```
 - coverage run -m pytest
     or 
 - python3 -m coverage run -m pytest
```
### Generate Coverage Report:
```
 - coverage report -m
    or 
 - python3 -m coverage report -m
```
## Generating distribution archives
Make sure you have the latest version of PyPA’s build installed:
```
python3 -m pip install --upgrade build
   or 
pip install build
```

Now run this command from the same directory where setup.py file is located:
```
python setup.py sdist
```

build a Python wheel distribution package for your project. This is typically done when you want to distribute your Python project, and a wheel is a binary distribution format that can be installed using the pip package manager.

``` 
python setup.py bdist_wheel
``` 

## Uploading the distribution archives
Finally, it’s time to upload your package to the Python Package Index!

The first thing you’ll need to do is register an account on TestPyPI, which is a separate instance of the package index intended for testing and experimentation. It’s great for things like this readme where we don’t necessarily want to upload to the real index. To register an account, go to https://test.pypi.org/account/register/ and complete the steps on that page. You will also need to verify your email address before you’re able to upload any packages. For more details, see Using TestPyPI.

To securely upload your project, you’ll need a PyPI API token. Create one at https://test.pypi.org/manage/account/#api-tokens, setting the “Scope” to “Entire account”. Don’t close the page until you have copied and saved the token — you won’t see that token again.

A .pypirc file allows you to define the configuration for package indexes (referred to here as “repositories”), so that you don’t have to enter the URL, username, or password whenever you upload a package with twine or flit.

```
# .pypirc file

    [distutils]
    index-servers =
        pypi
        testpypi

    [pypi]
    username = __token__
    password = <PyPI token>

    [testpypi]
    username = __token__
    password = <TestPyPI token>
```

run this command for 
```
chmod 600 ~/.pypirc
```

Now that you are registered, you can use twine to upload the distribution packages. You’ll need to install Twine:
```
python3 -m pip install --upgrade twine
```

Once installed, run Twine to upload all of the archives under dist:
```
python -m twine upload  --repository-url https://upload.pypi.org/legacy/ dist/*
```

You will be prompted for a username and password. For the username, use __token__. For the password, use the token value, including the pypi- prefix.

After the command completes, you should see output similar to this:

```
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: __token__
Uploading ZvArithmetic4-0.1.0/-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.2/8.2 kB • 00:01 • ?
Uploading ZvArithmetic4-0.1.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.8/6.8 kB • 00:00 • ?
```
Once uploaded, your package should be viewable on TestPyPI; for example: https://pypi.org/project/ZvArithmetic4/0.1.0/

## Installing your newly uploaded package
You can use pip to install your package and verify that it works.
```
pip install ZvolvArithmetic
```

The output should look something like this:
```
Collecting ZvolvArithmetic0.1.0
Downloading https://test-files.pythonhosted.org/packages/.../ZvolvArithmetic_0.1.0-py3-none-any.whl
Installing collected packages: ZvolvArithmetic
Successfully installed ZvolvArithmetic-0.1.0
```

You can test that it was installed correctly by importing the package. Make sure you’re still in your virtual environment, then run Python:

```
python3
```
and import the package:
```
    >>> from ZvolvArithmetic import arithmetic_opertion
    >>> result = arithmetic_opertion.add_numbers(10,20)
    >>> print(result)
    >>> 20
    >>> result = arithmetic_opertion.sub_numbers(10,20)
    >>> print(result)
    >>> -10
```
