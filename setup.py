import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Encoder",
    version="1.1",
    author="Viktor Sevastyanov",
    author_email="mivallion@example.com",
    description="Encoder library for Raspberry Pi for measuring quadrature encoded signals.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mivallion/Encoder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    keywords = [
        "raspberrypi",
        "encoder",
        "gpio"
    ]
)
