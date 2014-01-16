from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    version='0.9.0',
    name='FuelSDK',
    description='ExactTarget Fuel SDK for Python',
    long_description=readme,
    author='ExactTarget',
    author_email='code@exacttarget.com',
    py_modules=['ET_Client'],
    packages=find_packages(),
    package_data={'FuelSDK': ['*.xml']},
    url='https://github.com/ExactTarget/FuelSDK-Python',
    license='MIT',
    install_requires=[
        'pyjwt>=0.1.5',
        'requests>=1.1.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2.7',
    ],
)
