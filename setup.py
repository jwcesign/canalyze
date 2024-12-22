from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', 'r', encoding='utf-8') as f:
    license = f.read()

setup(
    name='canalyze',
    version='0.2.0',
    description='A cloud analysis tool designed to identify opportunities for cost savings in your cloud infrastructure.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='jwcesign',
    author_email='jwcesign@gmail.com',
    url='https://github.com/jwcesign/canalyze',
    entry_points={
        'console_scripts': [
            'canalyze=canalyze.cli:main'  # Replace 'main' and 'main' with the actual module and function
        ]
    },
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['boto3', 'rich'],  # Add dependencies here if your project has any
    python_requires='>=3.6',  # Specify minimum Python version
    include_package_data=True,
    zip_safe=False
)
