# Flask Issues - **Project Under Development**

Academic Project for Web Programming discipline at Faculdade Nova Roma - FGV

## How to run the project?

#### 1. open terminal and direct it to the locations where the web-project is located.

#### 2. Run the below command.
- 1.	Clone this repository.
- 2.	Create a pipenv with Python 3.7.5
- 3.	Enable pipenv => (pipenv shell).
- 4.	Install the dependencies.
- 5.	Run!!!.
```sh
git clone https://github.com/MarceloKabbalah/web-project.git
cd web-project
pip3 install pipenv
pipenv shell
pip3 install -r requirements.txt
python run.py
```
#### 3. To create new database for the user
- 1.	follow the first step
- 2.	type 'python' in terminal
	- 1. 	from app import db
	- 2.   from app.models import User, Post
	- 3.   User.query.delete()
	- 4.   Post.query.delete()
	- 5.   db.session.commit()
	- 6.   exit()
#### 4. To close the debug feature
- 1.	open run.py
- 2.	make 'debug=True' to 'debug=False' in app.run
## License
Flask Issues is open source software [licensed as MIT](https://github.com/MarceloKabbalah/web-project/blob/master/LICENSE).