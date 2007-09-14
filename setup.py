from setuptools import setup, find_packages
import sys, os

version = '0.8.1'

f = open(os.path.join(os.path.dirname(__file__), 'docs', 'index.txt'))
long_description = f.read().strip()
f.close()

setup(name='virtualenv',
      version=version,
      description="Virtual Python Environment builder",
      long_description=long_description,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
      ],
      keywords='setuptools deployment installation distutils',
      author='Ian Bicking',
      author_email='ianb@colorstudy.com',
      url='http://pypi.python.org/pypi/virtualenv',
      license='MIT',
      modules=['virtualenv'],
      include_package_data=True,
      zip_safe=False,
      entry_points="""
      [console_scripts]
      virtualenv = virtualenv:main
      """,
      )