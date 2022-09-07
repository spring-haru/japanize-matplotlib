# encoding: utf8
import glob
from setuptools import find_packages, setup

additional_files = []
for filename in glob.iglob('./japanize_matplotlib/**', recursive=True):
    additional_files.append(filename.replace('./japanize_matplotlib/', ''))


setup(name='japanize-matplotlib',
      version='1.1.3',
      description='matplotlibのフォント設定を自動で日本語化する',
      author='uehara1414',
      author_email='akiya.noface@gmail.com',
      url='https://github.com/uehara1414/japanize-matplotlib',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      license='MIT License',
      packages=find_packages(),
      install_requires=['matplotlib'],
      include_package_data=True,
      package_data={'japanize_matplotlib': additional_files})
