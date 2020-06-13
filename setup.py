from distutils.core import setup

import setuptools

with open("README.md", "r", encoding="utf8") as f:
    readme = f.read()

setup(
    name="kloppy",
    version="0.5.2",
    author="Koen Vossen",
    author_email="info@koenvossen.nl",
    url="https://github.com/PySport/kloppy",
    packages=setuptools.find_packages(exclude=["tests"]),
    license="BSD",
    description="Standardizing soccer tracking- and event data",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved",
        "Topic :: Scientific/Engineering",
    ],
    entry_points={
        "console_scripts": ["kloppy-query = kloppy.cmdline:run_query"]
    },
    install_requires=["lxml>=4.5.0", "requests>=2.0.0", "networkx>=2.4"],
    extras_require={
        "test": ["pytest", "pandas>=1.0.0"],
        "development": ["pre-commit"],
    },
)
