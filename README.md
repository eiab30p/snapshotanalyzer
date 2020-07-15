# snapshotanalyzer

Demo Project to manage AWS EC2 instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the AWS cli. e.g.

`aws configure --profile shotty`

## Running

`pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>`

_command_ is instances, volumes, or snapshots
_subcommand_ - depends on command
_project_ is optional
