#!/usr/bin/env python

import os
import pytest
from .. import main_xml_creator as creator
import datetime

@pytest.fixture
def clean_samples_folder():
    r'''Deletes every file from .\main_xml_creator\\tests\samples folder'''
    folder = r'.\\main_xml_creator\\tests\\samples'
    listdir = os.listdir(folder)
    for file in listdir:
        if listdir == []:
            continue
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)

@pytest.fixture
def create_sample_scripts():
    '''Creates sample test script files in .\\main_xml_creator\\tests\\samples folder'''
    folder = r'.\\main_xml_creator\\tests\\samples\\'
    for set_number in range(1, 4):
        for case_number in range(1, 4):
            file_name = folder + "MODEL_NAME_" + str(set_number) + '.Test.' + \
            format(case_number, '03d') + '.xml'
            with open(file_name, 'w+') as file:
                file.close()

@pytest.fixture
def create_sample_header():
    '''Creates sample header.xml file in .\\main_xml_creator\\tests\\samples'''
    folder = '.\\main_xml_creator\\tests\\samples\\'
    file_name = folder + 'header.xml'
    with open(file_name, 'w+') as file:
        file.write('My sample header\n')
        file.close()

@pytest.fixture
def create_sample_footer():
    '''Creates sample footer.xml file in .\\main_xml_creator\\tests\\samples'''
    folder = '.\\main_xml_creator\\tests\\samples\\'
    file_name = folder + 'footer.xml'
    with open(file_name, 'w+') as file:
        file.write('\nMy sample footer')
        file.close()


@pytest.fixture
def create_test_main_string():
    main_string = """My header
<INCLUDE FileName="MODEL_NAME.Test.001.xml" NameSpace="" TAB="10" LineComment="0"/>
<INCLUDE FileName="MODEL_NAME.Test.002.xml" NameSpace="" TAB="10" LineComment="0"/>
<INCLUDE FileName="MODEL_NAME.Test.003.xml" NameSpace="" TAB="10" LineComment="0"/>
My footer"""
    return main_string

@pytest.fixture
def create_processed_header():
    time =  datetime.datetime.now().strftime("%y-%m-%dT%H:%M")
    author = os.getlogin()
    test_model_name = "TEST_MODEL_NAME"
    header = """This is a sample header with #author#,
                #label#, as well as #group_id# and even
                the date (#last_gen#) it was generated"""
    processed_header = header.replace("#author#", author)
    processed_header = processed_header.replace("#label#", test_model_name)
    processed_header = processed_header.replace("#group_id#", test_model_name)
    processed_header = processed_header.replace("#last_gen#", time)
    return processed_header

def test_scan_for_models_raises_oserror(clean_samples_folder):
    with pytest.raises(OSError):
        creator.scan_for_models("invalid_folder_path")

def test_scan_for_models_success(create_sample_scripts):
    models = creator.scan_for_models('.\\main_xml_creator\\tests\\samples')
    assert models == {'MODEL_NAME_1': 3, 'MODEL_NAME_2': 3, 'MODEL_NAME_3': 3}

def test_load_header_raises_ioerror():
    with pytest.raises(IOError):
        creator.load_header("invalid_folder_path")

def test_load_header_success(create_sample_header):
    header = creator.load_header('.\\main_xml_creator\\tests\\samples\\header.xml')
    assert header == 'My sample header\n'

def test_load_footer_raises_ioerror():
    with pytest.raises(IOError):
        creator.load_footer("invalid_folder_path")

def test_load_footer_success(create_sample_footer):
    footer = creator.load_footer('.\\main_xml_creator\\tests\\samples\\footer.xml')
    assert footer == '\nMy sample footer'

def test_create_main_string_success():
    main_string = """My header
<INCLUDE FileName="MODEL_NAME.Test.001.xml" NameSpace="" TAB="10" LineComment="0"/>
<INCLUDE FileName="MODEL_NAME.Test.002.xml" NameSpace="" TAB="10" LineComment="0"/>
<INCLUDE FileName="MODEL_NAME.Test.003.xml" NameSpace="" TAB="10" LineComment="0"/>
My footer"""
    assert creator.create_main_string('MODEL_NAME', 3, 'My header\n', 'My footer') == main_string

def test_create_main_file_raises_ioerror():
    main_string = """My header
<INCLUDE FileName="MODEL_NAME.Test.001.xml" NameSpace="" TAB="10" LineComment="0"/>
<INCLUDE FileName="MODEL_NAME.Test.002.xml" NameSpace="" TAB="10" LineComment="0"/>
<INCLUDE FileName="MODEL_NAME.Test.003.xml" NameSpace="" TAB="10" LineComment="0"/>
My footer"""
    with pytest.raises(IOError):
        creator.create_main_file('MODEL_NAME', main_string, 'invalid_destination_folder')

def test_create_main_file_success(create_test_main_string):
    assert creator.create_main_file('MODEL_NAME', create_test_main_string, '.\\main_xml_creator\\tests\\samples') == 0
    assert 'MODEL_NAME.xml' in os.listdir('.\\main_xml_creator\\tests\\samples')

def test_process_header_success(create_processed_header):
    header = """This is a sample header with #author#,
            #label#, as well as #group_id# and even
            the date (#last_gen#) it was generated"""
    assert creator.process_header(header, "TEST_MODEL_NAME") == create_processed_header.processed_header