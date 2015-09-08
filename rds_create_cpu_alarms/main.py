#!/usr/bin/env python
"""create-cpu-alarms

Script used to create a over 80 pct. CPUUtilization alarm
in AWS CloudWatch for all RDS instances

Usage:
    create-cpu-alarms [options]
    create-cpu-alarms -h | --help

Options:
    -h --help   Show this screen.
    --debug     Don't send data to AWS

"""
import boto.ec2
import boto.rds2
from docopt import docopt
from boto.ec2.cloudwatch import MetricAlarm

DEBUG = False


def get_rds_instances():
    """
    Retreives the list of all RDS instances

    Returns:
        (list) List of valid state RDS instances
    """
    rds = boto.rds2.connect_to_region()
    response = rds.describe_db_instances()
    rds_instances = (response[u'DescribeDBInstancesResponse']
                             [u'DescribeDBInstancesResult']
                             [u'DBInstances'])

    return rds_instances


def get_existing_cpuutilization_alarm_names(aws_cw_connect):
    """
    Creates a CPUUtilization alarm for all RDS instances

    Args:
        aws_cw_connect (CloudWatchConnection)

    Returns:
        (set) Existing CPUUtilization alarm names
    """
    assert isinstance(aws_cw_connect,
                      boto.ec2.cloudwatch.CloudWatchConnection)

    existing_alarms = aws_cw_connect.describe_alarms()
    existing_alarm_names = set()

    for existing_alarm in existing_alarms:
        existing_alarm_names.add(existing_alarm.name)

    return existing_alarm_names


def get_cpuutilization_alarms_to_create(rds_instances,
                                        aws_cw_connect):
    """
    Creates a CPUUtilization alarm for all RDS instances

    Args:
        rds_instances (list) ist of all RDS instances
        aws_cw_connect (CloudWatchConnection)

    Returns:
        (set) All CPUUtilization alarms that will be created
    """
    assert isinstance(rds_instances, list)
    assert isinstance(aws_cw_connect,
                      boto.ec2.cloudwatch.CloudWatchConnection)

    alarms_to_create = set()
    existing_alarms = get_existing_cpuutilization_alarm_names(aws_cw_connect)

    for instance in rds_instances:

        # initiate a CPUUtilization MetricAlarm object for each RDS instance
        cpu_utilization_alarm = MetricAlarm(
            name=u'RDS-{}-High-CPUUtilization'.format(
                instance[u'DBInstanceIdentifier']),
            namespace=u'AWS/RDS',
            metric=u'CPUUtilization', statistic='Average',
            comparison=u'>',
            threshold=80,
            period=60, evaluation_periods=50,
            alarm_actions=[u'arn:aws:sns:us-west-1:667005031541:ops'],
            dimensions={u'DBInstanceIdentifier':
                        instance[u'DBInstanceIdentifier']})

        if cpu_utilization_alarm.name not in existing_alarms:
            alarms_to_create.add(cpu_utilization_alarm)

    return alarms_to_create


def main():
    args = docopt(__doc__)

    global DEBUG

    if args['--debug']:
        DEBUG = True

    rds_instances = get_rds_instances()
    aws_cw_connect = boto.ec2.cloudwatch.connect_to_region()
    alarms_to_create = get_cpuutilization_alarms_to_create(
        rds_instances, aws_cw_connect)

    if alarms_to_create:
        if DEBUG:
            for alarm in alarms_to_create:
                print 'DEBUG:', alarm
        else:
            print 'New RDS CPUUtilization Alarms created:'
            for alarm in alarms_to_create:
                print alarm
                aws_cw_connect.create_alarm(alarm)


if __name__ == '__main__':

    main()