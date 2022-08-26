# my_cmr.py
import os
import pathlib
from configparser import ConfigParser

from modules import my_inventory
from modules import file_manager

# read config file
file_config = ConfigParser()
file_config.read('config.ini')

# get config info
parent_path = file_config.get('FILES', 'parent')
modules_dir = file_config.get('FILES', 'modules')
data_dir = file_config.get('FILES', 'data')
enhanced_inventory_f = file_config.get('FILES', 'enhanced_inventory')
official_inventory_f = file_config.get('FILES', 'official_inventory')
current_progress_dir = file_config.get('FILES', 'current_progress')
reconciliation_report_f = file_config.get('FILES', 'reconciliation_report')
started_inventory_f = file_config.get('FILES', 'started_inventory')
record_archive_dir = file_config.get('FILES', 'record_archive')

# define paths to data
parent = pathlib.Path(parent_path)
official_inventory = parent.joinpath(data_dir, official_inventory_f)
enhanced_inventory = parent.joinpath(data_dir, enhanced_inventory_f)
saved_progress = parent.joinpath(current_progress_dir, started_inventory_f)
save_current_report = parent.joinpath(current_progress_dir, reconciliation_report_f)
archive = parent.joinpath(record_archive_dir)

# start a new inventory or continue a previous inventory
while True:
    print('\n********************************************\n'
          'WELCOME TO THE CMR RECONCILIATION PROGRAM.\n'
          '********************************************\n'
          'Load previous reconciliation or start new?\n'
          'WARNING: if you select "n", previous reconciliation will be overwritten.\n'
          'SELECT [n/c]')
    new_or_continuing = input()
    print('\n')
    if new_or_continuing == 'n':
        inventory = my_inventory.Inventory(official_inventory, enhanced_inventory, clear_file=saved_progress)
        break
    elif new_or_continuing == 'c':
        inventory = my_inventory.Inventory(official_inventory, enhanced_inventory, continue_inventory=saved_progress)
        break
    else:
        print("Please type 'n' or 'c'")
        continue

# ------------------------------------------------------------------------------------------
# initialize the inventory and see original inventory numbers, input reconciled serial
# numbers and print the report of the reconciliation.
inventory.get_inventory_stats()
inventory.computers_on_hand()
inventory.save_progress(saved_progress)
missing_cpus = inventory.reconcile_inventory()
report = inventory.reconciliation_stats()
file_manager.save_report(missing_cpus, report, save_current_report)

# ------------------------------------------------------------------------------------------
# now open the reconciliation report to display
os.startfile(save_current_report)

# now move the file into the archive folder
file_manager.to_archive(save_current_report, saved_progress, archive)