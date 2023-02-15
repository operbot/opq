# This file is placed in the Public Domain.


"object programming queue"


from setuptools import setup


def read():
    return open("README.rst", "r").read()


setup(
    name="opq",
    version="10",
    author="Bart Thate",
    author_email="operbot100@gmail.com",
    url="http://github.com/operbot/opq",
    zip_safe=True,
    description="object programming queue",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license="Public Domain",
    packages=["opq"],
    scripts=["bin/opq"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)
