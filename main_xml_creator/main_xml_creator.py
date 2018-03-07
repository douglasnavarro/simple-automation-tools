#!/usr/bin/env python
'''
This script scans the RDTool .xml scripts inside a directory and creates a main MODELNAME.xml script
that contains calls to every MODELNAME.Test.xxx.xml found in the same directory.
This is supposed to be a feature from TMX ('Sets' feature) but it generates broken xml files.
'''
import argparse
import pprint
import os
import sys
import platform
import datetime

def load_header(path_to_header_file):
    '''
    Loads header file and return as string
    Args:
        path_to_header_file (str): path to header file
    Return:
        header (str): header file content as string
    '''
    try:
        header_file = open(path_to_header_file, 'r')
        header = header_file.read()
        return header
    except IOError as error:
        print("Couldn't read header file \n(%s)." %error)
        raise

def process_header(header, model_name):
    '''
    Updates header template fields:
        - Last generated (#last_gen#)
        - Author (#author#)
        - Label (#label#)
        - Test Group Id (#group_id#)
    Args:
        header (str): string representing header template loaded
        model_name (str): model name for the main xml script in which this header will be used
    Return:
        processed_header (str): processed header
    '''
    processed_header = header.replace("#label#", model_name)
    processed_header = processed_header.replace('#group_id#', model_name)
    try:
        processed_header = processed_header.replace('#author#', os.getlogin())
    except OSError as error:
        print("Failed getting windows user name!")
        print(error)
        raise
    try:
        processed_header = processed_header.replace("#last_gen#", datetime.datetime.now().strftime("%y-%m-%dT%H:%M"))
    except Exception as error:
        print("Failed getting datetime!")
        print(error)
        raise
    return processed_header

def load_footer(path_to_footer_file):
    '''
    Loads footer file and return as string
    Args:
        path_to_footer_file (str): path to footer file
    Return:
        footer (str): footer file content as string
    '''
    try:
        footer_file = open(path_to_footer_file, 'r')
        footer = footer_file.read()
        return footer
    except IOError as error:
        print("Couldn't read footer file (%s)." %error)
        print(error)
        raise

def scan_for_models(script_folder_path):
    '''
    Scans script_folder_path for model names. The scripts must follow the MODEL_NAME.Test.xxx.xml
    naming convention where xxx is any 3-digit zero-padded integer

    Args:
        script_folder_path (str): Path to folder where test scripts xml files are located.

    Returns:
        models (dict): Dictionary whose keys are models names and values are tests counted.
    '''
    try:
        filenames = os.listdir(script_folder_path)
    except OSError as error:
        print("Error scaning origin directory!")
        print(error)
        raise
    models = {}
    for filename in filenames:
        if '.Test.' in filename:
            model_name = filename.split('.Test.')[0]
            if model_name not in models:
                models[model_name] = 1
            else:
                models[model_name] = models[model_name] + 1
    return models

def create_main_string(model_name, tests_count, header, footer):
    '''
    Creates the content of a MODELNAME.xml script with header and footer based on templates and
    containing calls to every test script found with the same MODELNAME, counted using tests_count.

    Args:
        model_name (str): String that represent the model name
        e.g XFS_SPNAME_COMMAND_SUCCESS

        tests_count (int): Number of tests scripts found for the same model

        header (str): Header template used to generate the MODELNAME.xml

        footer (str): Footer template used to generate the MODELNAME.xml

    Returns:
        main_string (str): A string representing the MODELNAME.xml file, yet not created.
    '''

    main_string = header
    for i in range(1, tests_count + 1):
        main_string += "<INCLUDE FileName=\"" + model_name + ".Test."+ format(i, '03d') +  \
        ".xml\" " + "NameSpace=\"\" TAB=\"10\" LineComment=\"0\"/>" + "\n"
    main_string += footer
    return main_string

def create_main_file(model_name, main_string, destination_folder):
    '''
    Creates a file model_name.xml containing main_string

    Args:
        model_name (str): String that represent the model name

        main_string (str): A string representing the MODELNAME.xml file, yet not created.

        destination_folder (str): destination folder path
    '''
    file_name = model_name + ".xml"
    if destination_folder.endswith("\\") is False:
        destination_folder += "\\"
    dest = destination_folder + file_name
    try:
        with open(dest, 'w+') as file:
            file.write(main_string)
    except IOError as error:
        print("Couldn't open or write to file (%s)." %error)
        raise

def create_unattended_string(models, header, footer):
    '''
    Creates the content of an Unattended.xml script, which calls every main script available for the device.
    
    Args:
        models: dictionary generated by scan_for_models function
        header: (string) from template header
        footer: (string) from template footer
    '''
    unattended = header
    for model_name, test_count in models.items():
        unattended += "<INCLUDE FileName=\"" + model_name + ".xml\" " + "NameSpace=\"\" TAB=\"10\" LineComment=\"0\"/>" + "\n"
    unattended += footer
    return unattended

def create_unattended_file(unattended_string, destination_folder):
    '''
    Creates a Unattended.xml file containing unattended_string
    Args:
        unattended_string: (string) contents of file
        destination_folder: (string) path to output file
    Returns:
        int 0 for success
        int 1 for failure
    '''
    file_name = "Unattended.xml"
    if destination_folder.endswith("\\") is False:
        destination_folder += "\\"
    dest = destination_folder + file_name
    try:
        with open(dest, 'w+') as file:
            file.write(unattended_string)
            return 0
    except IOError as error:
        print("Couldnt open or write to file " + dest + "(%s)." %error)
        raise

def main():
    '''
    main function. gets args from command line and produces model_name.xml files
    using functions defined in main_script_creator.py
    '''
    if platform.system() != 'Windows':
        print("\nThis script only runs properly on Windows.\n")
        sys.exit(1)
    
    if len(sys.argv) <= 1:
        print("\nRunning with default options! Use 'main_xml_creator -h' for help")

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='''This script scans origin folder for test cases scripts and creates a test set script on dest. folder using
        custom header and footer files.''')

    parser.add_argument("origin_folder", \
    nargs='?', default='.\\', help="the directory where the test case scripts are located. default is current directory.")

    parser.add_argument("destination_folder", \
    nargs='?', default='.\\', help="the directory where test set scripts will be saved")

    parser.add_argument("path_to_header", \
    nargs='?', default='.\\header.xml', help="the path to header template file")

    parser.add_argument("path_to_footer", \
    nargs='?', default='.\\footer.xml', help="the path to footer template file")

    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

    parser.add_argument("-cu", "--create_unattended", help="create unattended script", action="store_true")

    args = parser.parse_args()

    try:
        header = load_header(args.path_to_header)
    except IOError:
        sys.exit(1)
    if args.verbose:
        print("Header successfully loaded!\n")

    try:
        footer = load_footer(args.path_to_footer)
    except IOError:
        sys.exit(1)
    if args.verbose:
        print("Footer successfully loaded!\n")

    try:
        models = scan_for_models(args.origin_folder)
    except OSError:
        sys.exit(1)

    if args.verbose:
        print("The folliwng models detected are shown as: {\'model_name\': test_count}\n")
        pprint.pprint(models)
        print()

    for model_name, test_count in models.items():
        header = process_header(header, model_name)
        main_string = create_main_string(model_name, test_count, header, footer)
        try:
            create_main_file(model_name, main_string, args.destination_folder)
        except IOError:
            sys.exit(1)
    if args.verbose:
        print("Created model_name.xml files successfully!")
    
    if args.create_unattended:
        unattended_header = process_header(header, "Unattended")
        unattended = create_unattended_string(models, unattended_header, footer)
        try:
            create_unattended_file(unattended, args.destination_folder)
            if args.verbose:
                print("Created Unattended.xml successfully!")
        except IOError:
            sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()

__author__ = "Douglas Navarro"
__version__ = "1.0"
__status__ = "Development"
