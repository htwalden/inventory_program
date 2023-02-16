# my_cmr.py
import os
import pathlib
from configparser import ConfigParser
import pathlib
from modules import my_inventory
from modules import file_manager

# get relative data folder
PATH = pathlib.Path(__file__).parent
official_inventory = PATH.joinpath('./data/official_inventory.txt').resolve()
enhanced_inventory = PATH.joinpath('./data/enhanced_inventory.csv').resolve()
saved_progress = PATH.joinpath('./current_progress/started_inventory.txt').resolve()
save_current_report = PATH.joinpath('./current_progress/reconciliation_report.txt').resolve()
archive = PATH.joinpath('./record_archive').resolve()


# start a new inventory or continue a previous inventory
while True:
    print('\n********************************************\n'
          'WELCOME TO THE CMR RECONCILIATION PROGRAM.\n'
          '********************************************\n'
          'Load previous reconciliation or start new?\n'
          'WARNING: if you select "n", previous reconciliation will be overwritten.\n'
          'SELECT [n/c]')
    try:
        new_or_continuing = input()
        print('\n')
        if new_or_continuing == 'n':
            inventory = my_inventory.Inventory(official_inventory, enhanced_inventory, clear_file=saved_progress)
            break
        elif new_or_continuing == 'c':
            inventory = my_inventory.Inventory(official_inventory, enhanced_inventory,
                                               continue_inventory=saved_progress)
            break
        else:
            print("Please type 'n' or 'c'")
            continue
    except Exception as e:
        print(e)

# ------------------------------------------------------------------------------------------
# initialize the inventory and see original inventory numbers, input reconciled serial
# numbers and print the report of the reconciliation.
inventory.get_inventory_stats()
inventory.validate_data()
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