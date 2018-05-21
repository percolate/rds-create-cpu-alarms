from setuptools import setup
from rds_create_cpu_alarms.constants import VERSION

setup(
    name='rds-create-cpu-alarms',
    version=VERSION,
    description=('AWS Cloudwatch RDS Tool for creating CPUUtilization Metric '
                 'Alarms'),
    url='https://github.com/percolate/rds-create-cpu-alarms',
    author='Mihailo Pavlisin',
    author_email='mihailo@percolate.com',
    license='GPLv3',
    keywords='aws rds2 rds cpu alarms cloudwatch boto',
    packages=['rds_create_cpu_alarms'],
    install_requires=[
        'boto',
        'docopt'
    ],
    entry_points={
        'console_scripts': [
            'rds-create-cpu-alarms=rds_create_cpu_alarms.main:main'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: System :: Systems Administration"
    ]
)
