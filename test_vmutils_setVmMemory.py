import unittest
import mock
from nova.virt.hyperv import vmutils

class TestSetVmMemory(unittest.TestCase):
	def test_set_vm_memory(self):
		mock = mock.MagicMock()
        self._vmutils._lookup_vm_check = mock.MagicMock(
            return_value=mock)
        mock.path_.return_value = self._FAKE_VM_PATH
        return mock

