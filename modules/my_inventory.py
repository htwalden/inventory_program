# my_inventory_module
from csv import reader


class Inventory:

    def __init__(self, original_inventory, enhanced_inventory, continue_inventory=None, clear_file=None):
        self.original_inventory = original_inventory  # the serials from the offical records (.txt no header)
        self.enhanced_inventory = enhanced_inventory  # serials with locations derived from original (.csv with header)
        self.continue_inventory = continue_inventory
        self.clear_file = clear_file

        # open and read the original inventory as a set
        with open(self.original_inventory) as oi:
            self.serials = oi.read().split("\n")
            self.serials = set(self.serials)
            self.total_computers = len(self.serials)
            oi.close()

        # open the enhanced inventory and make a dict serial:location
        with open(self.enhanced_inventory) as ei:
            self.locations = list(reader(ei))
            self.locations = self.locations[1:]
            self.locations = {item: location for item, location in self.locations}
            ei.close()

        # combine the ensure the original serials that may not be in enhanced are added
        for item in self.serials:
            if item not in self.locations:
                self.locations[item] = "Location Unknown"

                # create a way to load a preexisting inventory job or start a new one
        if self.continue_inventory is not None:
            with open(self.continue_inventory) as on_hand:
                self.computers_found = on_hand.read().split("\n")
                on_hand.close()
                for item in self.computers_found:
                    if item == '':
                        self.computers_found.remove(item)
        else:
            self.computers_found = []

        # clear the started_inventory if continue_inventory is none
        if self.continue_inventory is None:
            open(self.clear_file).close()

    # check the length of the original inventory, return message to user
    def get_inventory_stats(self):
        return print(f'***INVENTORY STATUS*** \n'
                     f'There are {self.total_computers} computers in the inventory \n'
                     f'Computers accounted for: {len(self.computers_found)}\n'
                     '********************************************************\n'
                     'Begin the reconciliation below...')

    # process user inputting serial numbers, return list of serials
    def computers_on_hand(self):
        print('Add serial numbers. Type \'done\' when complete.')
        while True:
            answer = input()
            if (answer not in self.serials) and (answer != 'done'):
                print('Serial number not found in inventory')
            if answer == 'done':
                break
            if answer in self.computers_found:
                print('DUPLICATE number...Serial number already accounted for.')
            elif (answer in self.serials) and (answer not in self.computers_found):
                self.computers_found.append(answer)
                print('Serial number successfully added')
                continue
        return self.computers_found

    # write the list of serials to a file that were found for future use
    def save_progress(self, save_progress):
        with open(save_progress, "w") as progress:
            for item in self.computers_found:
                progress.write(f'{item}\n')
            progress.close()

    # check the serials we found against the master inventory return serials and locations
    # of computers that are not found but are in the master inventory
    def reconcile_inventory(self):
        missing_computers = {item: loc for item, loc in self.locations.items() if item not in self.computers_found}
        return missing_computers

    # create reports to the user notifying how many computers are found vs missing
    def reconciliation_stats(self):
        if len(self.computers_found) == len(self.serials):
            rpt1 = (f'***Reconciliation complete:***' '\n''\n'
                    f'There is a total of {len(self.serials)} in the inventory' '\n''\n'
                    f'Computers found: {len(self.computers_found)}' '\n''\n'
                    f'All computers accounted for...inventory complete')
            return rpt1
        else:
            missing_count = len(self.serials) - len(self.computers_found)
            missing_percentage = round(100 * (missing_count / len(self.serials)))
            rpt5 = (f'***Reconciliation complete:***' '\n''\n'
                    f'There is a total of {len(self.serials)} in the inventory' '\n''\n'
                    f'Computers found: {len(self.computers_found)}'  '\n''\n'
                    f'Computers missing: {missing_count}' '\n'
                    f'Missing percentage of total: {missing_percentage}%' '\n''\n'
                    f'The following computers are missing: \n')
            return rpt5

