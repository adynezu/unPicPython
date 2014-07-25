import unittest
import mock
from nova.virt.hyperv import vmutils

class TestSetVmMemory(unittest.TestCase):
	def test_set_vm_memory_true(self):
		dynamic_memory_ratio = 2
		max_mem = long(2048)
		mock_mem_set = mock.MagicMock()
		mock_mem_set = vmsettig.associators(
			wmi_result_class=self._MEMORY_SETTING_DATA_CLASS)[0]
		mock_mem_set.Limit = max_mem
		self.assertEqual(mock_mem_set.Limit, 2048)
		mock_mem_set.DynamicMemoryEnabled = True
		self.assertEqual(mock_mem_set.DynamicMemoryEnabled, True)
		reserved_mem = min(
			long(max_mem / dynamic_memory_ratio) >> 1 << 1, 
			max_mem)
		mock_mem_set.Reservation = reserved_mem
		self.assertEqual(mock_mem_set.Reservation, 
			min( long(max_mem / dynamic_memory_ratio) 
				>> 1 << 1, max_mem))
		mock_mem_set.VirtualQuantity = reserved_mem
   		self.assertEqual(mock_mem_set.VirtualQuantity, 
			min( long(max_mem / dynamic_memory_ratio) 
				>> 1 << 1, max_mem))

    def test_set_vm_memory_false(self):
		dynamic_memory_ratio = 2
		max_mem = long(2048)
		mock_mem_set = mock.MagicMock()
		mock_mem_set = vmsettig.associators(
			wmi_result_class=self._MEMORY_SETTING_DATA_CLASS)[0]
		mock_mem_set.Limit = max_mem
		self.assertEqual(mock_mem_set.Limit, 2048)
		mock_mem_set.DynamicMemoryEnabled = False
		self.assertEqual(mock_mem_set.DynamicMemoryEnabled, False)
		reserved_mem = max_mem
		mock_mem_set.Reservation = reserved_mem
		self.assertEqual(mock_mem_set.Reservation, 
			long(2048))
		mock_mem_set.VirtualQuantity = reserved_mem
   		self.assertEqual(mock_mem_set.VirtualQuantity, 
			long(2048))
