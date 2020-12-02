from setuptools import setup

setup(
    name='upsmychoice',
    version='1.0.7',
    description='Python 3 API for UPS My Choice, a way to track packages.',
    url='https://github.com/happyleavesaoc/python-upsmychoice/',
    license='MIT',
    author='happyleaves',
    author_email='happyleaves.tfr@gmail.com',
    packages=['upsmychoice'],
    install_requires=['beautifulsoup4>=4.6.0', 'python-dateutil>=2.8.0', 'requests>=2.20.0'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)
