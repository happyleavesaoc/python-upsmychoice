from setuptools import setup

setup(
    name='upsmychoice',
    version='1.0.1',
    description='Python 3 API for UPS My Choice, a way to track packages.',
    url='https://github.com/happyleavesaoc/python-upsmychoice/',
    license='MIT',
    author='happyleaves',
    author_email='happyleaves.tfr@gmail.com',
    packages=['upsmychoice'],
    install_requires=['beautifulsoup4==4.5.1', 'python-dateutil==2.6.0', 'requests==2.12.4'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ]
)
