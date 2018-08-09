import setuptools

setuptools.setup(
    name="dnsweb",
    version="0.1.0",
    url="https://github.com/fourth04/dnsweb",

    author="fourth04",
    author_email="524135921@qq.com",

    description="An opinionated, minimal cookiecutter template for Python packages",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        "Flask-Cors==3.0.3",
        "Flask==0.12.2",
        "IPy==0.83",
        "SQLAlchemy==1.2.1",
        "Werkzeug==0.14.1",
        "botocore==1.10.36",
        "future==0.16.0",
        "greenlet==0.4.12",
        "incremental==17.5.0",
        "ipykernel==4.6.1",
        "ipython-genutils==0.2.0",
        "ipython==6.2.1",
        "ipywidgets==7.1.1",
        "jinja2-time==0.2.0",
        "jsonschema==2.6.0",
        "jupyter-core==4.4.0",
        "nose==1.3.7",
        "numpy==1.14.0",
        "numpydoc==0.7.0",
        "pandas==0.22.0",
        "pickleshare==0.7.4",
        "pycosat==0.6.3",
        "requests-file==1.4.3",
        "requests-html==0.9.0",
        "requests==2.18.4",
        "scipy==1.0.0",
        "unicodecsv==0.14.1",
        "wincertstore==0.2",
        "xlrd==1.1.0"
    ],

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
