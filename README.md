# Drug Review Analysis PRoject
This is a repo for the drug review analysis project for AAI 500. 

## Getting Started

### Cloning this repo
Run each command line-by-line in your terminal to set up the project:

    ```bash
    $ git clone git@github.com:omarsagoo/drug-review-analysis.git
    $ cd drug-review-analysis
    ```

### Python version
The python version that you will use will be automatically set with pyenv. The version it is currently set to use is 3.7.17, this can be modified in the Makefile if needed on line 7. 

### pyenv
In order to run this repo you must have pyenv and pyenv-virtualenv installed. 
- https://github.com/pyenv/pyenv
- https://github.com/pyenv/pyenv-virtualenv

### make
You will also need to have make installed to use all of the easy  to use commands that have been setup for this project. 
Windows installation: 
- https://gnuwin32.sourceforge.net/packages/make.htm
Mac installation:
- https://formulae.brew.sh/formula/make

## Usage

### Running the notebook
After Installing the required tools:

```bash
  $ make run
```

This command will install all the necessary dependencies, start up a virtual environment, create a kernel with the correct python version, then finally run the jupyter notebook. It will open a browser window.

Running this command will set everything up for you, the first time might be a little slow as it downloads and caches all of the dependencies, but all subsequent calls will be relatively quick!

### Adding dependecies
In order to properly add dependencies to the virtual environment you will need to open a console through the notebook. This will ensure that the packages get put into the right place. 

After you install a new package, you must run the following make command:

```bash
    $ make update
```
This command will update the requirements.txt file with the added dependency. 