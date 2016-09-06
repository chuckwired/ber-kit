#!/usr/local/bin/python

"""
undrain
Given IP address(s), remove any UNLIKE constraint on any Marathon job using a given IP.

optional arguments:
  -h, --help     show this help message and exit
  --url URL      Marathon URL (http://marathon.example.com)
  --hosts HOSTS  Hosts that have finished maintenance

Example Usage:
$ ber-kit undrain --url http://marathon.example.com --hosts 172.31.37.92,172.31.35.101
"""

import sys
import json
import time
import argparse
import requests
import ber_kit.commands.utils as utils

from marathon import MarathonClient
from marathon.models import MarathonConstraint

def unmigrate_tasks(marathon_client, apps_to_update, constraints_to_remove):
  """
  Remove temporary constraints used for host migration
  """
  for appId in apps_to_update.iterkeys():
    print(">>> Unmigrating the following task")
    print(appId)

    # Remove all unrequired constraints
    to_redeploy = marathon_client.get_app(appId)
    for constraint in constraints_to_remove:
        if constraint in to_redeploy.constraints:
            to_redeploy.constraints.remove(constraint)

    # Redeploy
    marathon_client.update_app(appId, to_redeploy, force=True)
  print(">>> Unmigrated all the tasks")

def main(args):
  migration_hosts = args.hosts.split(',')
  marathon_client = MarathonClient(args.url)

  # Get the running marathon application dictionary with constraints
  all_apps = utils.dict_by_key_and_value(lambda x: x.id, lambda y: y.constraints, marathon_client.list_apps())
  print(">>> All Running Applications: ")
  print(json.dumps(all_apps.keys(), sort_keys=True, indent=4, separators=(',', ': ')))

  # Constraints to remove
  sentinels = map(lambda x: MarathonConstraint('hostname', 'UNLIKE', x), migration_hosts)

  # Find all apps with a leftover constraint
  filtered_apps = {}
  for sentinel in sentinels:
      for app_id in all_apps:
          if sentinel in all_apps[app_id]:
              to_update = {app_id: all_apps[app_id]}
              print ">>> Adding app to filtered list: %s" % (app_id)
              filtered_apps.update(to_update)

  # Tasks unmigration
  unmigrate_tasks(marathon_client, filtered_apps, sentinels)

if __name__ == "__main__":
  sys.exit(main())
