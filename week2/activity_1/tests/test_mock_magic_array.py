import unittest
from unittest.mock import patch
from src.mock_array import Array

class TestMockArray(unittest.TestCase):
    def setUp(self):
        self.mock_array = Array(max_size=2)  # small size to trigger resize quickly

    def tearDown(self):
        del self.mock_array

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
        with patch.object(Array, "_Array__resize") as mock_resize:
            self.mock_array.append(1)
            self.mock_array.append(2)
            self.mock_array.append(3)  # Should trigger resize
            mock_resize.assert_called_once()

    def test_private_attributes_not_accessible(self):
        with self.assertRaises(AttributeError):
            _ = self.mock_array.__resize
        with self.assertRaises(AttributeError):
            _ = self.mock_array.__instance_count

    def test_class_method_get_instance_count(self):
        self.assertGreaterEqual(Array.get_instance_count(), 1)

    def test_patched_instance_count_method(self):
        with patch('src.mock_array.Array.get_instance_count', return_value=999) as mock_method:
            self.assertEqual(Array.get_instance_count(), 999)
            mock_method.assert_called_once()
