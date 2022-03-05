from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='duckjobs',
  version='6.94.20',
  description="DuckJobs is a DSCJobs API client, that's stupid, useless, bloated, and probably slept with your girlfriend last night.",
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  url='',  
  author='ZeroTwo36 ',
  author_email='zerotwo36@protonmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='dscjobs discord duck', 
  packages=find_packages(),
  install_requires=['requests'] 
)