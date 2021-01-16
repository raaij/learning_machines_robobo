"""
TODO:
    - Put robobo, prey and vrep packages in a namespace learning_machines_robobo
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='learning_machines_robobo',
    version='1.0.0',
    description='Framework for Learning Machines Course',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ci-group/learning_machines_robobo',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['numpy', 'opencv-python'],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.dll", "*.dylib", "*.so"],
    }
)
