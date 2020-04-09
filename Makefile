dev:
	export FLASK_ENV=development;
	export FLASK_APP=webapp.py;
	flask run;
	flask init-db;