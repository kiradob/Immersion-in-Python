import os

import pytest
from collections import namedtuple
from main import get_dir_contents


class Test:

    @pytest.fixture
    def dir_item_for_type_check(self):
        DirItem = namedtuple('DirItem', 'name ext is_dir parent')
        return DirItem

    @pytest.fixture
    def dir_item_test_folder(self):
        os.makedirs('test/dir1', exist_ok=True)
        os.makedirs('test/dir2', exist_ok=True)
        open('test/doc1.f1', 'w').close() 
        open('test/doc2.f2', 'w').close()  

    @pytest.fixture
    def dir_item_test_folder_item_names(self):
        return ['dir1', 'dir2', 'doc1', 'doc2'] 

    @pytest.fixture
    def dir_item_test_folder_item_extensions(self):
        return [None, None, '.f1', '.f2']

    def test_number_of_dir_contents(self, dir_item_test_folder):
        path = os.path.abspath('test/')
        tuples = get_dir_contents(path)
        assert len(tuples) == 4

    def test_names_in_test_folder(self, dir_item_test_folder, dir_item_test_folder_item_names):
        path = os.path.abspath('test/')
        tuples = get_dir_contents(path)
        assert [tup.name for tup in tuples] == dir_item_test_folder_item_names

    def test_extensions_in_test_folder(self, dir_item_test_folder, dir_item_test_folder_item_extensions):
        path = os.path.abspath('test/')
        tuples = get_dir_contents(path)
        assert [tup.ext for tup in tuples] == dir_item_test_folder_item_extensions