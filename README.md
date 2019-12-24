# Flask Issues - **Project Under Development**
![GitHub](https://img.shields.io/github/license/MarceloKabbalah/web-project?color=blue)![Python version](https://img.shields.io/github/pipenv/locked/python-version/MarceloKabbalah/web-project)![Flask version](https://img.shields.io/github/pipenv/locked/dependency-version/MarceloKabbalah/web-project/flask)![Github Status](https://img.shields.io/pypi/status/Flask)
![GitHub last commit](https://img.shields.io/github/last-commit/MarceloKabbalah/web-project)![GitHub issues](https://img.shields.io/github/issues/MarceloKabbalah/web-project)[![Code Style Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black/)

![GitHub watchers](https://img.shields.io/github/watchers/MarceloKabbalah/web-project?style=social)![GitHub stars](https://img.shields.io/github/stars/MarceloKabbalah/web-project?style=social)![GitHub forks](https://img.shields.io/github/forks/MarceloKabbalah/web-project?style=social)

Academic Project for Web Programming discipline at Faculdade Nova Roma - FGV

## How to run the project?

#### 1. open terminal and direct it to the locations where the web-project is located.

#### 2. Run the below command.
- Clone this repository.
- Create a pipenv with Python 3.7.5
- Enable pipenv => (pipenv shell).
- Install the dependencies.
- Run!!!.
```PYTHON
git clone https://github.com/MarceloKabbalah/web-project.git
cd web-project
pip3 install pipenv
pipenv shell
pip3 install -r requirements.txt
python run.py
```
#### 3. To create new database for the user
- Follow the first step
- Type 'python' in terminal
```MYSQL
from app import db
from app.models import User, Post
User.query.delete()
Post.query.delete()
db.session.commit()
exit()
```
#### 4. To close the debug feature
- Open run.py
- Make 'debug=True' to 'debug=False' in app.run


## Contributing
1. Faça o _fork_ do projeto (<https://github.com/yourname/yourproject/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_