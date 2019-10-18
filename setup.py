from setuptools import setup

setup(
    name="pygnore",
    version="1.0",
    py_modules=['pygnore'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        pygnore=pygnore:main
    ''',
)