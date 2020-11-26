import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ascii_magic", # Replace with your own username
    version="1.0.0",
    author="Leandro Barone",
    author_email="web@leandrobarone.com.ar",
    description="Converts pictures into ASCII art",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeandroBarone/python-ascii_magic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=['colorama', 'Pillow'],
)