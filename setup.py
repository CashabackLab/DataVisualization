from setuptools import setup

setup(
    # Needed to silence warnings 
    name='DataVisualization',
    url='https://github.com/CashabackLab/DataVisualization',
    download_url = 'https://github.com/CashabackLab/DataVisualization',
    author='CashabackLab',
    author_email='cashabacklab@gmail.com',
    # Needed to actually package something
    packages=['data_visualization'],
    # Needed for dependencies
    install_requires=['numpy', 'matplotlib >= 3.5.0', 'pillow'],
    # *strongly* suggested for sharing
    version='0.6.28',
    # The license can be anything you like
    license='MIT',
    description='Python package for visualizing human kinematic data and analytical results, tailored for the Cashaback Lab',
    long_description=open('README.md').read(),
    include_package_data=True,
)
