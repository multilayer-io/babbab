
## Contributing to Babbab

Thank you for your interest in contributing to Babbab! Before you begin writing code, please read through this document. 
First, it is important that you share your intention to contribute, based on the type of contribution.

Please first search through Babbab [issues](https://github.com/multilayer-labs/babbab/issues). If the feature is not listed, please create a new issue. 
If you would like to work on any existing issue, please comment and assign yourself to the issue and file a pull request.

This document covers some of the technical aspects of contributing to Babbab.

## Developing Babbab & Set-up

To develop Babbab on your machine, you can follow the set-up instructions. 

### Prerequisites

Python >= 3.8

Install flit if you don't have it
```python3 -m pip install flit```

### Set-up

First clone the repo:

```git clone https://github.com/multilayer-labs/babbab.git```

Next open the repo and install dependencies:

```cd babbab && flit install -s --deps develop```

### Codebase structure
Babbab is split across three different files:
* core - where everything runs
* stats - where the stats are defined
* viz - where the visualization elements are composed

There is also a notebooks section, demonstrating how everything works. Please verify these notebooks still work correctly following your contribution.

### Unit testing

Before you submit your pull request, please ensure you have written a unit test for your code and all unit tests are passing.
You can check this by visiting the babbab home directory and running pytest command:

```pytest```

### Linting

There is currently no linter.

### Writing documentation

Please make sure you add documentation to your functions. Please use [Google Style docstrings](https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html).
