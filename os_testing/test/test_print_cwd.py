from unittest import TestCase, mock

from app.print_cwd import PrintCWD


class TestPrintCWDMockingModule(TestCase):

	def setUp(self):
		self.printcwd = PrintCWD()

	def test_using_context_manager(self):
		with mock.patch('app.print_cwd.os') as mocked_os:
			self.printcwd.work_on()
			mocked_os.getcwd.assert_called_once()

	@mock.patch('app.print_cwd.os')
	def test_using_decorator(self, mocked_os):
		self.printcwd.work_on()
		mocked_os.getcwd.assert_called_once()


	def test_using_return_value(self):
		"""Note 'as' in the context manager is optional"""
		with mock.patch('app.print_cwd.os.getcwd', return_value='testing'):
			assert self.printcwd.work_on() == 'testing'

	@mock.patch('app.print_cwd.print')
	@mock.patch('app.print_cwd.os.getcwd', return_value='testing')
	def test_calculator_add_method_mock_result_valid_input_invalid_output(self,mocked_os,mock_print):
		assert self.printcwd.work_on() == 'testing'
		mock_print.assert_called_once_with('Working on testing')


	def test_patch_dict(self):
		with mock.patch('app.print_cwd.print') as mock_print:
			with mock.patch('app.print_cwd.os.getcwd', return_value='/home/'):
				with mock.patch.dict('app.print_cwd.os.environ', {'MY_VAR': 'testing'}):
					self.assertEqual(self.printcwd.work_on_env(), '/home/testing')
					mock_print.assert_called_once_with('Working on /home/testing')

	@mock.patch('app.print_cwd.os.getcwd', return_value='/home/')
	@mock.patch('app.print_cwd.print')
	@mock.patch.dict('app.print_cwd.os.environ', {'MY_VAR': 'testing'})
	def test_patch_builtin_dict_decorators(self, mock_print, mock_getcwd):
		self.assertEqual(self.printcwd.work_on_env(), '/home/testing')
		mock_print.assert_called_once_with('Working on /home/testing')