from setuptools import setup

setup(
    name='snapshotanalyzer',
    version='0.1',
    author="Eduardo Verde",
    author_email="eduardo.eddy.verde94@gmail.com",
    description="SnapshotAnalyzer is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/eiab30p/snapshotanalyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)