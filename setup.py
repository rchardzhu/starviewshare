# -*- coding: utf-8 -*-
"""
# Created on 2023-12-17
# setup.py: 观星量化setup.py
# Copyright @author: Richard zhu(rchardzhu@gmail.com)，观星量化系统(starview quant system)
# 更多量化投资知识、代码，请加入Python量化实战：https://t.zsxq.com/12uaiVhV5
"""

import ast
import pathlib
import re
from setuptools import find_packages, setup


def get_version_string() -> str:
    """
    Get the starviewshare version number
    :return: version number
    :rtype: str, e.g. '0.1.0'
    """
    with open("starviewshare/__init__.py", "rb") as _f:
        version_line = re.search(
            r"__version__\s+=\s+(.*)", _f.read().decode("utf-8")
        ).group(1)
        return str(ast.literal_eval(version_line))


here = pathlib.Path(__file__).parent
# require = (here / "requirements.txt").read_text(encoding='utf-8').split()
require = ['requests', 'pandas', 'tqdm', 'efinance']
readme = (here / "README.md").read_text(encoding='utf-8')

setup(
    name='starviewshare',
    version=get_version_string(),
    description='A finance tool to get stock,fund and futures data',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/rchardzhu/starviewshare',
    author='Richard Zhu',
    author_email='rchardzhu@gmail.com',
    license="MIT",
    platforms=['any'],
    keywords=['finance', 'quant', 'stock', 'etf', 'futures', 'starviewshare'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=require,
    project_urls={
        'Documentation': 'https://github.com/rchardzhu/starviewshare',
        'Source': 'https://github.com/rchardzhu/starviewshare',
    },
)
