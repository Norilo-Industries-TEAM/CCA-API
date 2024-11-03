from setuptools import setup, find_packages

setup(
    name='PyCCA',
    version='1.0',
    packages=find_packages(),
    description='Python Compression and Decompression API using CCA Method.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Norilo Industries TEAM',
    author_email='olamundo9117@gmail.com',
    url='https://github.com/Norilo-Industries-TEAM/CCA-API',
    install_requires=[
        'lzma',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows',
    ],
    python_requires='>=3.7',
)
