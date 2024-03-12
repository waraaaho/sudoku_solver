import validate, retrieve


"""build in method"""
# create 4 test cases to validate functions: validate_9x9_input, validate_3x3, validate_hline, validate_vline

def test_validate_9x9_input():
    assert validate.validate_9x9_input('123456789234567891345678914567891245678912356789123467891234578912345689123456791') == True
    assert validate.validate_9x9_input('123456789234567891345678914567891245678912356789123467891234578912345689123456791234567') == False
    assert validate.validate_9x9_input('12345678923456789134567891456789124567891235678912346789123457891234568912345679123456789') == False
    assert validate.validate_9x9_input('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678 ') == False

def test_validate_3x3():
    assert validate.validate_3x3(retrieve.get_square(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),'top','top')) == True
    assert validate.validate_3x3(retrieve.get_square(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),'top','top')) == True
    assert validate.validate_3x3(retrieve.get_square(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),'top','top')) == True
    assert validate.validate_3x3(retrieve.get_square(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),'top','top')) == True

def test_validate_hline():
    assert validate.validate_hline(retrieve.get_hline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),0)) == True
    assert validate.validate_hline(retrieve.get_hline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),1)) == True
    assert validate.validate_hline(retrieve.get_hline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),2)) == True
    assert validate.validate_hline(retrieve.get_hline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),3)) == True

def test_validate_vline():
    assert validate.validate_vline(retrieve.get_vline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),0)) == True
    assert validate.validate_vline(retrieve.get_vline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),1)) == True
    assert validate.validate_vline(retrieve.get_vline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),2)) == True
    assert validate.validate_vline(retrieve.get_vline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),3)) == True

"""unittest method"""
# create 4 test cases to validate functions: validate_9x9_input, validate_3x3, validate_hline, validate_vline
import unittest

class TestValidate(unittest.TestCase):

    def test_validate_9x9_input(self):
        print('~ test_validate_9x9_input')
        self.assertEqual(validate.validate_9x9_input('123456789234567891345678914567891245678912356789123467891234578912345689123456791'), True)
        self.assertEqual(validate.validate_9x9_input('123456789456789123789123456234567891567891234891234567345678912678912345912345678'), True)
        self.assertEqual(validate.validate_9x9_input('12345678923456789134567891456789124567891235678912346789123457891234568912345679123456789'), False)
        self.assertEqual(validate.validate_9x9_input('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678 '), False)
        
    def test_validate_3x3(self):
        print('\n\n~ test_validate_3x3')
        self.assertEqual(validate.validate_3x3(retrieve.get_square(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),'top','top')), False)
        self.assertEqual(validate.validate_3x3(retrieve.get_square(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),'bot','bot')), False)
        self.assertEqual(validate.validate_3x3(retrieve.get_square(retrieve.transform_str_to_df('123456789456789123789123456234567891567891234891234567345678912678912345912345678'),'bot','top')), True)
        self.assertEqual(validate.validate_3x3(retrieve.get_square(retrieve.transform_str_to_df('123456789456789123789123456234567891567891234891234567345678912678912345912345678'),'mid','top')), True)
                      
    def test_validate_hline(self):
        print('\n\n~ test_validate_hline')
        self.assertEqual(validate.validate_hline(retrieve.get_hline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),0)), True)
        self.assertEqual(validate.validate_hline(retrieve.get_hline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),1)), True)
        self.assertEqual(validate.validate_hline(retrieve.get_hline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),2)), False)
        self.assertEqual(validate.validate_hline(retrieve.get_hline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),3)), False)
        
    def test_validate_vline(self):
        print('\n\n~ test_validate_vline')
        self.assertEqual(validate.validate_vline(retrieve.get_vline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),0)), False)
        self.assertEqual(validate.validate_vline(retrieve.get_vline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),1)), False)
        self.assertEqual(validate.validate_vline(retrieve.get_vline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),2)), False)
        self.assertEqual(validate.validate_vline(retrieve.get_vline(retrieve.transform_str_to_df('1234567892345678913456789145678912456789123567891234678912345789123456891234567912345678'),3)), False)

        
if __name__ == '__main__':
    print('Hi')
    unittest.main()

"""How to Use unittest and Flask Template"""
import main
import unittest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_home(self):
        result = self.app.get('/')
        # Make your assertions
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, b'Hello, World!')
        