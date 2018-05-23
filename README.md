# rds-create-cpu-alarms

[![Circle CI](https://circleci.com/gh/percolate/rds-create-cpu-alarms.svg?style=svg)](https://circleci.com/gh/percolate/rds-create-cpu-alarms)
[![codecov.io](http://codecov.io/github/percolate/rds-create-cpu-alarms/coverage.svg?branch=master)](http://codecov.io/github/percolate/rds-create-cpu-alarms?branch=master)

Automate the creation of RDS cpu Alarms.

## Quick Start

```bash
"""rds-create-cpu-alarms

Script used to create CPUUtilization alarms in AWS CloudWatch
for all RDS instances.
A upper-limit threshold needs to be defined.

Usage:
    rds-create-cpu-alarms [options] <threshold> <sns_topic_arn> <region>
    rds-create-cpu-alarms -h | --help

Options:
    -h --help   Show this screen.
    --debug     Don't send data to AWS
"""
```

## Install

```bash
pip install rds-create-cpu-alarms
```
