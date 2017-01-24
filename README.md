# ghief - git thief

*A backup script for batch updating remote repositories*

[![Build Status](https://travis-ci.org/MatthiasLohr/ghief.svg)](https://travis-ci.org/MatthiasLohr/ghief)

## Usage
```
usage: ghief [-h] [-l LIST] [-v] [--debug]

optional arguments:
  -h, --help            show this help message and exit
  -l LIST, --list LIST  Specify repository list file
  -v, --verbose         Be chatty
  --debug               Enabled debugging output
```

## repository list file

The repository list file is a simple YAML file with following structure:

```yamlex
repositories:
  - source: /home/user/my-project
    target: git@remote:/home/user/my-project
    
   ...
```


## Development

### Setting up the development environment

* Clone the source code to your local machine with ```git clone```
* ```cd``` into the source code directory
* Create a virtual environment with ```virtualenv venv```
* Activate the virtual environment with ```source venv/bin/activate```
* Install the plugin in editable mode with ```pip install -e .```
