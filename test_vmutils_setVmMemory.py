import unittest
import mock
from nova.virt.hyperv import vmutils

class TestSetVmMemory(unittest.TestCase):
	def _lookup_vm(self):
        	mock_vm = mock.MagicMock()
        	self._vmutils._lookup_vm_check = mock.MagicMock(
        		return_value=mock_vm)
	        mock_vm.path_.return_value = self._FAKE_VM_PATH
		return mock_vm

	def _test_set_vm_memory_dynamic(self, dynamic_memory_ratio):
        	mock_vm = self._lookup_vm()
        	mock_s = self._vmutils._conn.Msvm_VirtualSystemSettingData()[0]
        	mock_s.SystemType = 3
        	mock_vmsetting = mock.MagicMock()
		mock_vmsetting.associators.return_value = [mock_s]
        	self._vmutils._modify_virt_resource = mock.MagicMock()
        	self._vmutils._set_vm_memory(mock_vm, mock_vmsetting,
                                     self._FAKE_MEMORY_MB,
                                     dynamic_memory_ratio)

        	self._vmutils._modify_virt_resource.assert_called_with(
            	mock_s, self._FAKE_VM_PATH)
        if dynamic_memory_ratio > 1:
            self.assertTrue(mock_s.DynamicMemoryEnabled)
        else:
            self.assertFalse(mock_s.DynamicMemoryEnabled)
