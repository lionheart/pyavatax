from distutils.core import setup
# python setup.py sdist bdist_wininst upload

setup(
    name='PyAvaTax',
    url = 'http://github.com/activefrequency/pyavatax/',
    author = 'John Obelenus',
    author_email = 'jobelenus@activefrequency.com',
    version='0.1dev',
    install_requires = ['requests>=0.14.1', 'decorator>=3.4.0'],
    package_data = {
        '': ['*.txt', '*.rst', '*.md']
    },
    packages=['pyavatax',],
    license='BSD',
    long_description=open('README.md').read(),
)
