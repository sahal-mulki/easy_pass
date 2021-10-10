from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'easy_pass',         # How you named your package folder (MyLib)
  packages = ['easy_pass'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A library to hash passwords and manage them.',   # Give a short description about your library
  author = 'Muhammad Sahal Mulki',                   # Type in your name
  long_description=long_description,
  long_description_content_type="text/markdown",
  author_email = 'm.sahalmulki@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/sahal-mulki',   # Provide either the link to your github or to your website
  keywords = ['sha-256' 'hash', 'password'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
