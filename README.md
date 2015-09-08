# rds-create-cpu-alarms

[![Circle CI](https://circleci.com/gh/percolate/rds-create-cpu-alarms.svg?style=svg)](https://circleci.com/gh/percolate/rds-create-cpu-alarms)
[![codecov.io](http://codecov.io/github/percolate/rds-create-cpu-alarms/coverage.svg?branch=master)](http://codecov.io/github/percolate/rds-create-cpu-alarms?branch=master)

Automate the creation of RDS cpu Alarms.
The `Low-cpu` lower-bound limit in the script is 20%, but this can be altered.

# Quick Start
```bash
"""rds-create-cpu-alarms

Script used to create a over 80 pct. CPUUtilization alarm
in AWS CloudWatch for all RDS instances

Usage:
    create-cpu-alarms [options]
    create-cpu-alarms -h | --help

Options:
    -h --help   Show this screen.
    --debug     Don't send data to AWS
"""
```

# Install
```bash
$ pip install rds-create-cpu-alarms
```
