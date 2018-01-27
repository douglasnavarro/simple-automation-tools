#!/usr/bin/env python
'''
This script scans the RDTool .xml scripts inside a directory and creates a main MODELNAME.xml script
that contains calls to every MODELNAME.Test.xxx.xml found in the same directory.
This is supposed to be a feature from TMX ('Sets' feature) but it generates broken xml files.
This may be updated in a later version that will be available god-knows-when.
'''

import os

def list_models(script_folder_path):
    '''
    Scans script_folder_path for model names.

    Args:
        script_folder_path (str): Path to folder where test scripts xml files are located.

    Returns:
        models (dict): Dictionary whose keys are models names and values are tests counted.
    '''

    filenames = os.listdir(script_folder_path)
    models = {}
    for filename in filenames:
        if '.Test.' in filename:
            model_name = filename.split('.Test.')[0]
            if model_name not in models:
                models[model_name] = 1
            else:
                models[model_name] = models[model_name] + 1
    return models

def create_main(model_name, tests_count, header, footer):
    '''
    Creates a MODELNAME.xml script with header and footer based on templates and containing calls
    to every test script found with the same MODELNAME, counted using tests_count.

    Args:
        model_name (str): String that represent the model name
        e.g XFS_SPNAME_COMMAND_SUCCESS

        tests_count (int): Number of tests scripts found for the same model

        header (str): Header template used to generate the MODELNAME.xml

        footer (str): Footer template used to generate the MODELNAME.xml

    Returns:
        main_script (str): A string representing the MODELNAME.xml file, yet not created.
    '''

    main_script = header
    for _ in range(1, tests_count + 1):
        main_script += "<INCLUDE FileName=\"" + model_name +  \
        " \"" + "NameSpace=\"\" TAB=\"10\" LineComment=\"0\"/>\""
    print(main_script)

print(create_main('TESTE', 3, 'MEU HEADER\n', 'MEU FOOTER'))

__author__ = "Douglas Navarro"
__version__ = "1.0"
__status__ = "Development"
