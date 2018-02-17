# Main XML creator

This is a tool for creating test set scripts from a bunch of test case scripts. This tool is for windows users only, considering the context that motivated its creation.

Test case script folder **before** running *main xml creator*:
```
C:.
│   main_script_creator.py
│   README.md
│   __init__.py
│
└───samples
        footer.xml
        header.xml
        MODEL_NAME_1.Test.001.xml
        MODEL_NAME_1.Test.002.xml
        MODEL_NAME_1.Test.003.xml
        MODEL_NAME_2.Test.001.xml
        MODEL_NAME_2.Test.002.xml
        MODEL_NAME_2.Test.003.xml
```

and **afeter** running **main xml creator**
```
C:.
│   main_script_creator.py
│   README.md
│   __init__.py
│
└───samples
        footer.xml
        header.xml
        MODEL_NAME_1.Test.001.xml
        MODEL_NAME_1.Test.002.xml
        MODEL_NAME_1.Test.003.xml
        MODEL_NAME_1.xml
        MODEL_NAME_2.Test.001.xml
        MODEL_NAME_2.Test.002.xml
        MODEL_NAME_2.Test.003.xml
        MODEL_NAME_2.xml
```

where MODEL_NAME_1.xml calls every MODEL_NAME_1.Test.xxx.xml file, the same for MODEL_NAME_2 and so on.

## Compiled executables

If you simply want to quickly use the tool download an executable.
```
.\main_xml_creator.exe -h
usage: main_xml_creator.exe [-h] [-v]
                            [origin_folder] [destination_folder]
                            [path_to_header] [path_to_footer]

This script scans origin folder for test cases scripts and creates a test set
script on dest. folder using custom header and footer files.

positional arguments:
  origin_folder       the directory where the test case scripts are located.
                      default is current directory. (default: .\)
  destination_folder  the directory where test set scripts will be saved
                      (default: .\)
  path_to_header      the path to header template file (default: .\header.xml)
  path_to_footer      the path to footer template file (default: .\footer.xml)

optional arguments:
  -h, --help          show this help message and exit
  -v, --verbose       increase output verbosity (default: False)
```

(*) Windows x64: [Download](https://github.com/douglasnavarro/simple-automation-tools/raw/master/main_xml_creator/dist/main_xml_creator.exe)


## How to contribute: Getting Started

Either [download](https://github.com/douglasnavarro/simple-automation-tools/archive/master.zip) the project .zip or run

```
git clone https://github.com/douglasnavarro/simple-automation-tools
```

### Prerequisites

You will need python 3 installed. If you don't have it, download it from the official [python.org](https://www.python.org/) page. Don't forget to add python to PATH.

## Run a demo

1. Start powershell (WIN+R powershell)
3. Browse to project folder you unzipped or cloned
4. Run
```
python main_xml_creator
```
5. Check arguments required:
```
the following arguments are required: origin_folder, destination_folder, path_to_header,path_to_footer
```
6. To produce the main scripts from the MODEL_NAME_1 and MODEL_NAME_2 tests found in the sample folder, run
```
python main_xml_creator .\main_xml_creator\samples\ .\main_xml_creator\samples .\main_xml_creator\samples\header.txt .\main_xml_creator\samples\footer.txt -v
```
7. Run `tree /f` to check that the MODEL_NAME_1.xml and MODEL_NAME_2.xml files were indeed created.
8. Run `get-content .\main_xml_creator\samples\MODEL_NAME_1.xml` to check the file created.

## Running the tests

1. Install pytest by running `pip install pytest`
2. Browse to root project folder (simple-automation-tools) and run `pytest -v`

## Building

1. Install pyinstaller by running `pip install pyinstaller`
2. Run pyinstaller `main_xml_creator.py --onefile` to produce main_xml_creator.exe on build folder.

## Authors

* *Douglas Navarro* - Github: [douglasnavarro](https://github.com/douglasnavarro)

*Feel free to contribute. Please first discuss the change or increment you wish to make via issue, email etc.**
