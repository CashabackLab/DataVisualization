from setuptools import setup
import re
import ast

#Only change __version__ in data_visualization/__init__.py file
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('data_visualization/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    # Needed to silence warnings 
    name='DataVisualization',
    url='https://github.com/CashabackLab/DataVisualization',
    download_url = 'https://github.com/CashabackLab/DataVisualization',
    author='CashabackLab',
    author_email='cashabacklab@gmail.com',
    # Needed to actually package something
    packages=['data_visualization', 'icons'],
    # Needed for dependencies
    install_requires=['numpy', 'matplotlib >= 3.5.0', 'pillow'],
    # *strongly* suggested for sharing
    version=version,
    # The license can be anything you like
    license='MIT',
    description='Python package for visualizing human kinematic data and analytical results, tailored for the Cashaback Lab',
    long_description=open('README.md').read(),
    include_package_data=True,
)
