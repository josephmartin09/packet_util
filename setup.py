import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="packet_util",
    version="0.0.1",
    author="Joseph Martin",
    author_email="joe@jmartintech.com",
    description="Utility to pack and unpack binary data into commonly used python data types.",
    long_description=long_description,
    url="https://github.com/josephmartin09/packet_util",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
