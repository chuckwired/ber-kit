import multiprocessing
from setuptools import setup, find_packages

from ber_kit import __version__

setup(name='ber-kit',
    version= __version__,
    description='Toolkit to manage rolling upgrades on a Marathon cluster',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: System :: Systems Administration',
    ],
    keywords='marathon',
    url='http://bitbucket.org/connectedsolutions/ber-kit',
    author='Charles Rice, Cake Solutions',
    author_email='devops@cakesolutions.net',
    license='GNU GPLv3',
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'marathon>=0.8.6',
    ],
    entry_points = {
        'console_scripts': [
            'ber-kit=ber_kit.main:main',
        ],
    },
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock',
        'coverage',
    ],
    zip_safe=False)
