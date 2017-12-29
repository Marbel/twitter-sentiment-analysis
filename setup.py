"""
Tool for analysing sentiment in replies of a twitter post or a twitter profile.
"""
from setuptools import find_packages, setup
import re
import io

dependencies = ['appjar', 'matplotlib', 'ta-lib', 'tensorflow', 'python-twitter']

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    io.open('twitter-sentiment-analysis/_version.py', encoding='utf_8_sig').read()
).group(1)

setup(
    name='twitter-sentiment-analysis',
    version=__version__,
    url='https://github.com/Marbel/twitter-sentiment-analysis',
    license='MIT',
    author='Jan-Andre Moebis',
    author_email='das.marbel@googlemail.com',
    description='Tool for analysing sentiment in replies of a twitter post or a twitter profile.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'twitter-sentiment-analysis = twitter-sentiment-analysis.start:start',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
