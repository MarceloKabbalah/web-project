# Flask Issues - **Project Under Development**
![open issues](https://img.shields.io/github/issues/MarceloKabbalah/web-project?color=%2319a249) ![open PR](https://img.shields.io/github/issues-pr-closed/MarceloKabbalah/web-project?color=%23f25f56) ![license](https://img.shields.io/github/license/MarceloKabbalah/web-project) ![forks](https://img.shields.io/github/forks/MarceloKabbalah/web-project?style=social)

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
