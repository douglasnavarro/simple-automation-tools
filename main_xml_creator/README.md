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
2. Browse to (...)\main_xml_creator
3. Run
```
$ python main_script_creator.py
```

## Running the tests

TODO: pytest

## Authors

* **Douglas Navarro* - [douglasnavarro](https://github.com/douglasnavarro)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to the poorly developed tools I have to use an SQA intern.
