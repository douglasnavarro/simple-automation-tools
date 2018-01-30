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
        footer.txt
        header.txt
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
        footer.txt
        header.txt
        MODEL_NAME_1.Test.001.xml
        MODEL_NAME_1.Test.002.xml
        MODEL_NAME_1.Test.003.xml
        MODEL_NAME_1.xml
        MODEL_NAME_2.Test.001.xml
        MODEL_NAME_2.Test.002.xml
        MODEL_NAME_2.Test.003.xml
        MODEL_NAME_2.xml
```

where MODEL_NAME_1.xml calls every MODEL_NAME_1.Test.xxx.xml file, the same for MODEL_NAME_2 and son on.

## Getting Started

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
2. Browse to root project folder (simple-automation-tools) and run `pytest`

## Authors

* *Douglas Navarro* - Github: [douglasnavarro](https://github.com/douglasnavarro)

*Feel free to contribute. Please first discuss the change or increment you wish to make via issue, email etc.**
