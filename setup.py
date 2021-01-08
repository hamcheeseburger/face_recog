import io
from setuptools import find_packages, setup


# Read in the README for the long description on PyPI
def long_description():
    with io.open('README.txt', 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme

    setup(name='login',
      version='0.1',
      description='login package',
      long_description=long_description(),
      url='https://github.com/hamcheeseburger/face_recog',
      author='hamcheeseburger',
      author_email='yoo77hyeon.com@gmail.com',
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3.6',
          ],
      zip_safe=False)

    setup(name='login',
          version='0.1',
          description='login package',
          long_description=long_description(),
          url='https://github.com/hamcheeseburger/face_recog',
          author='hamcheeseburger',
          author_email='yoo77hyeon.com@gmail.com',
          packages=find_packages(),
          classifiers=[
              'Programming Language :: Python :: 3.6',
          ],
          zip_safe=False)