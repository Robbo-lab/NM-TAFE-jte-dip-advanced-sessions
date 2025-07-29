import unittest
from src.mock_array import Array

class TestMockArray(unittest.TestCase):
    def setUp(self):
        self.mock_array = Array(max_size=2)  # small size to trigger resize quickly

    def tearDown(self):
        del self.mock_array  # Optional but explicit cleanup

    def test_insert_item_increments_index(self):
        self.assertEqual(self.mock_array.index, -1)
        self.mock_array.append(42)
        self.assertEqual(self.mock_array.index, 0)

    def test_get_inserted_item(self):
        self.mock_array.append(1)
        self.mock_array.append(2)
        self.assertEqual(self.mock_array.get(0), 1)
        self.assertEqual(self.mock_array.get(1), 2)

    def test_get_from_empty_list_raises_error(self):
        with self.assertRaises(IndexError):
            self.mock_array.get(0)

    def test_insert_item_at_position(self):
        self.mock_array.append(10)
        self.mock_array.append(20)
        self.mock_array.insert(99, 1)
        self.assertEqual(self.mock_array.get(1), 99)

    def test_insert_out_of_bounds_raises(self):
        with self.assertRaises(IndexError):
            self.mock_array.insert(88, 5)

    def test_resize_occurs_when_full(self):
        self.mock_array.append(1)
        self.mock_array.append(2)
        # should trigger resize since max_size = 2
        self.mock_array.append(3)
        self.assertEqual(self.mock_array.get(2), 3)

    def test_private_attributes_not_accessible(self):
        with self.assertRaises(AttributeError):
            _ = self.mock_array.__resize
        with self.assertRaises(AttributeError):
            _ = self.mock_array.__instance_count

    def test_class_method_get_instance_count(self):
        # This assumes the test suite is run independently
        self.assertGreaterEqual(Array.get_instance_count(), 1)