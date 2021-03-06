from setuptools import setup

APP=['main.py']

options = {
    'argv_emulation':True
}

setup(
        app=APP,
        options={'py2app':options},
        setup_requires=['py2app']
)