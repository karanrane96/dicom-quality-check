from setuptools import setup, find_packages

setup(
    name='dicom_quality_check',
    version='0.1.0',
    description='A tool for validating and checking DICOM image quality',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Karan Rane',
    author_email='karanrane96@gmail.com',
    url='https://github.com/karanrane96/dicom_quality_check',
    packages=find_packages(),
    install_requires=[
        'pydicom',
        'numpy',
        'opencv-python',
        'scikit-image',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)