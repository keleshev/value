from setuptools import setup

import value


setup(
    name=value.__name__,
    version=value.__version__,
    author='Vladimir Keleshev',
    author_email='vladimir@keleshev.com',
    description='Implementation of Value Object pattern',
    license='MIT',
    keywords='value object pattern',
    url='http://github.com/halst/value',
    py_modules=[value.__name__],
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: MIT License',
    ],
)
