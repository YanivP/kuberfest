import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='kuberfest',  
    version='0.0.1a',
    scripts=['kbf'] ,
    author="Yaniv Peer",
    author_email="yanivpeer@gmail.com",
    description="A lightweight framework for fast cloud development",
    long_description="Please see: https://github.com/yanivp/kuberfest",
    long_description_content_type="text/markdown",
    url="https://github.com/yanivp/kuberfest",
    packages=setuptools.find_namespace_packages(),
    install_requires=[
        'pyyaml'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)