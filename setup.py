# coding=utf-8
from setuptools import setup

setup(
    name="coverage_bug",
    description="Coverage bug minimal case",
    version=0.1,
    author="Kent Ross",
    author_email="",
    license="MIT",
    package_dir={"": "src"},
    extras_require={
        'test': [
            'pytest-cov',
            'tox',
        ]
    },
)
