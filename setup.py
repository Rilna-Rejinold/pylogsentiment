from setuptools import setup

setup(name='pylogsentiment',
      version='0.0.1',
      description='Sentiment analysis for event logs.',
      long_description='Sentiment analysis for event logs.',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
      ],
      keywords='sentiment analysis, event logs',
      url='http://github.com/studiawan/pylogsentiment/',
      author='Hudan Studiawan',
      author_email='studiawan@gmail.com',
      license='MIT',
      packages=['pylogsentiment'],
      entry_points={
          'console_scripts': [
              'pylogsentiment = pylogsentiment.pylogsentiment:main'
          ],
      },
     install_requires=[
    'nerlogparser',
    'scikit-learn>=0.24.2',
    'keras>=2.6.0',
    'keras-metrics>=0.0.4',
    'imbalanced-learn>=0.8.1',
    'pyparsing>=2.4.6',
    'tensorflow',
    'h5py>=3.1.0'
],
      include_package_data=True,
      zip_safe=False)
