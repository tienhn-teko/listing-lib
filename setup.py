# coding=utf-8
import setuptools

with open("README.md", "r") as rm:
    README = rm.read()

# with open("HISTORY.md", "r") as h:
#     HISTORY = h.read()

setup_args = dict(
    name='es-listing-lib',
    version_format='{tag}.dev{commitcount}+{gitsha}',
    setup_requires=['setuptools-git-version'],
    long_description=README,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url='https://github.com/tienhn-teko/listing-lib',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)

install_requires = [
    'elastictools'
]

setuptools.setup(
    **setup_args,
    install_requires=install_requires)
