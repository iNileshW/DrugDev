# Technical Test

## Getting Started

Download the test file and uncompress it [here](https://cdn.glitch.com/cd885eee-f9d0-40ff-b200-f8b9553ca169%2Ftest.zip?1533120666668)

### Information you will need

- The url for you want to test against is `https://sprinkle-burn.glitch.me/`
- A valid user credentials are belo
  - email: `test@drugdev.com`
  - password: `supers3cret`

### Complete Behave tests

1.  Fix broken tests
    - Open test/behave/features/steps/login.py
    - You will find that the methods have not been completed as they raise the NotImplemented Error.
    - According to the descripted scenario, fill in the necessary steps to pass the test.
2.  What changes could you make to the features to make them better for testing?
3.  Are there any features that you think should be added to improve the testing?

### Fix broken postman tests

- Install and Open PostMan on your machine.
- Open the collection `test/postman/collections/WorldsBestApp.json`
- Setup the environment `test/postman/environments/local.json`

1.  Try to run it and you'l find that some of the tests are broken. Fix them.
2.  Can the test be improved in anyway?

---

# Tips

## Requirements

- [nodejs >= 8](https://nodejs.org/en/)
- [Postman](https://www.getpostman.com/)
- [python3](https://www.python.org/)

## Install on Mac

```
brew install node
brew install python
brew install pipenv
brew cask install postman
brew cask install chromedriver
```

# Install on Windows

```
choco install selenium-chrome-driver
choco install nodejs
choco install postman
choco install python
python -m pip install -U pip
pip install pipenv
```

## Behave

[Behave](https://behave.readthedocs.io/en/latest/) is BDD testing framework for python. You can
use [selenium](http://selenium-python.readthedocs.io/) to implement your tests.

### Setup

Make sure you have everything installed above

```
cd behave
pipenv --python 3.6
pipenv shell
pipenv install
```

### Running tests

`behave`

## Postman

Check that the apis are returning the desired results. You can use the ui tool information for importing the files can be found [here](https://www.getpostman.com/docs/v6/postman/collections/data_formats). If you wish to use the cli
tool directions are below.

### Running Postman Test cli

#### Run all

`npx newman run postman/collections/*.json -e postman/environments/local.json`

#### Run one

`npx newman run postman/collections/WorldsBestApp.json -e postman/environments/local.json`
"# DrugDev" 
