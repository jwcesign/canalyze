from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='canalyze',
    version='0.1.0',
    description='A cloud analysis tool designed to identify opportunities for cost savings in your cloud infrastructure.',
    long_description=readme,
    author='jwcesign',
    author_email='jwcesign@gmail.com',
    url='https://github.com/jwcesign/canalyze',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)