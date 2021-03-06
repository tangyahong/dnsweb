import setuptools

setuptools.setup(
    name="dnsbackend",
    version="0.1.0",
    url="https://github.com/fourth04/dnsweb",

    author="fourth04",
    author_email="GYangyun@gmail.com",

    description="dns analysis web backend",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
