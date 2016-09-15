#!/usr/local/bin/python

"""
drain
Given IP address, add an UNLIKE constraint on any Marathon job using that slave.

optional arguments:
  -h, --help     show this help message and exit
  --url URL      Marathon URL (http://marathon.example.com)
  --hosts HOSTS  Hosts going to go for maintenance
  --force        Set deployment to be 'force=true'

Example Usage:
$ ber-kit drain --url http://marathon.example.com --hosts 172.31.37.92,172.31.35.101
"""

import sys
import json
import time
import argparse
import requests
import ber_kit.commands.utils as utils

from marathon import MarathonClient
from marathon.models import MarathonConstraint

def migrate_tasks(marathon_client, tasks, hosts, force=False):
  """
  Migrate tasks from the hosts going to go for maintenance
  """
  for app_id in tasks.iterkeys():
    print(">>> Migrating the following tasks")
    print(app_id)

    # Redeploy all the applications running on maintenance hosts by adding constraints
    # Generate constraints list
    constraints_to_add = map(lambda host: MarathonConstraint('hostname', 'UNLIKE', host), hosts)

    # Generate app to deploy
    app_to_redeploy = marathon_client.get_app(app_id)
    task_host = tasks[app_id].host
    for constraint in constraints_to_add:
        if constraint.value == task_host:
            app_to_redeploy.constraints.append(constraint)

    # Clean the app
    app_to_redeploy.tasks = []
    if app_to_redeploy.container:
        app_to_redeploy.fetch = []

    # Redeploy
    marathon_client.update_app(app_id, app_to_redeploy, force=force)

  print(">>> Migrated all the tasks")

def main(args):
  migration_hosts = args.hosts.split(',')
  marathon_client = MarathonClient(args.url)

  # Get the running marathon application dictionary
  running_instances = utils.dict_by_key_and_value(lambda x: x.id, lambda y: y.instances, marathon_client.list_apps())
  print(">>> Total Running Applications: ")
  print(json.dumps(running_instances, sort_keys=True, indent=4, separators=(',', ': ')))

  # Get the running marathon applications for all hosts which are going for maintenance
  all_tasks = marathon_client.list_tasks()
  filtered_tasks = [task for task in all_tasks if task.host in migration_hosts]
  dicted_tasks = utils.dict_by_key(lambda x: x.app_id, filtered_tasks)

  print(">>> Total Running Application: ")
  print(json.dumps(dicted_tasks.keys(), sort_keys=True, indent=4, separators=(',', ': ')))

  # Tasks migration
  migrate_tasks(marathon_client, dicted_tasks, migration_hosts, args.force)

if __name__ == "__main__":
  sys.exit(main())
