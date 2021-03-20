from setuptools import setup

setup(
    name='nnssa',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:kingsleyzissou/nnssa.git',
    author='Gianluca Zuccarelli',
    author_email='20079110@mail.wit.ie',
    license='unlicense',
    packages=['nnssa'],
    package_dir={'nnssa', 'src/'},
    zip_safe=False
)
