import unittest

from inventory_allocator import inventory_allocator

class TestInventoryAllocator(unittest.TestCase):


    def test_inventory_allocator_single_warehouse(self):
        # Order can be shipped using one warehouse
        order_list = {'apple': 1}
        inventory_distribution = [{'name': 'owd', 'inventory': {'apple': 1}}]
        expected_result = [{'owd': {'apple': 1}}]

        result = inventory_allocator(order_list, inventory_distribution)
        self.assertEqual(result, expected_result)


    def test_inventory_allocator_multiple_warehouse(self):
        # Order can be shipped using multiple warehouses

        order_list = {'apple': 10}
        inventory_distribution = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
        expected_result = [{'dm': {'apple': 5}, 'owd': {'apple': 5}}]

        result = inventory_allocator(order_list, inventory_distribution)
        self.assertEqual(result, expected_result)


    def test_inventory_allocator_not_enough_inventory(self):
        # Order cannot be shipped because there is not enough inventory
        order_list = {'apple': 1}
        inventory_distribution = [{'name': 'owd', 'inventory': {'apple': 0}}]
        expected_result = []

        result = inventory_allocator(order_list, inventory_distribution)
        self.assertEqual(result, expected_result)


    def test_inventory_allocator_many_fruits(self):
        # Many fruits in the order list
        order_list = {'apple': 10, 'mango': 12, 'guava': 2, 'grapes': 1}
        inventory_distribution = [
                                    {'name': 'owd',
                                     'inventory': {'apple': 10, 'mango': 5, 'grapes': 3}
                                    },
                                    {'name': 'dm',
                                     'inventory': {'apple': 5, 'mango': 15, 'guava': 8}
                                    }
                                 ]
        expected_result = [
                            {'owd': {'apple': 10, 'mango': 5, 'grapes': 1},
                             'dm': {'mango': 7, 'guava': 2}}
                          ]

        result = inventory_allocator(order_list, inventory_distribution)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
