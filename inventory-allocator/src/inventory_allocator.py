# Anshuma Jain
# Problem: Compute the best way an order can be shipped (called shipments) given inventory across a set of warehouses (called inventory distribution).


def update_shipment_distribution(shipment_distribution, warehouse_name, fruit, order_qty):
    """ Updates the shipment distribution using the given warehouse_name, fruit, and order_qty """
    if warehouse_name not in shipment_distribution:  # if warehouse doesn't exist in the shipment distribution list
        shipment_distribution[warehouse_name] = {fruit: order_qty}  # Example entry: [ { owd: {apple:10} } ]
    elif warehouse_name in shipment_distribution:
        shipment_distribution[warehouse_name][fruit] = order_qty


def inventory_allocator(order_list, inventory_distribution):
    """ Creates a shipment_distribution based on the given order_list and inventory_distribution """

    if order_list == {} or inventory_distribution == []:    # if order list or inventory is empty
        return []

    shipment_distribution = {}                              # to store the output
    while order_list.keys():                                # iterate until order list is empty
        fruit = list(order_list.keys())[0]                  # select the first fruit from the order list
        order_qty = order_list[fruit]                       # obtain order qty for the given fruit

        for warehouse_record in inventory_distribution:                     # loop thru each warehouse
            warehouse_name = warehouse_record['name']
            warehouse_inventory = warehouse_record['inventory']

            if fruit in warehouse_inventory:                                # if the fruit exists in the warehouse inventory
                if warehouse_inventory[fruit] >= order_qty:                 # if there are sufficient fruit qty in this warehouse's inventory
                    update_shipment_distribution(shipment_distribution, warehouse_name, fruit, order_qty)
                    warehouse_inventory[fruit] -= order_qty                 # adjust the warehouse inventory
                    order_qty = 0
                    order_list.pop(fruit)                                   # remove this fruit from the order list
                    break                                                   # back to while loop for the next fruit
                elif 0 < warehouse_inventory[fruit] < order_list[fruit]:    # if partial fruit qty in this warehouse
                    update_shipment_distribution(shipment_distribution, warehouse_name, fruit, warehouse_inventory[fruit])
                    order_qty -= warehouse_inventory[fruit]                 # compute remaining quantity
                    warehouse_inventory[fruit] = 0

        if order_qty != 0:  # if qty is still unfulfilled after going thru all the warehouses
            return []

    return [shipment_distribution]                                          # return a list
