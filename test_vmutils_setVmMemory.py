import unittest
import mock
from nova.virt.hyperv import vmutils

class TestSetVmMemory(unittest.TestCase):
	def test_set_vm_memory(self):
		mock = mock.MagicMock()
       		
