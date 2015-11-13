# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


# target: clean - Clean all ".pyc" files
clean:
	find . -name "*.pyc" -exec rm -rf {} \;


# target: migrate - Migrate all django applications considering app dependencies
migrate:
	python awesome_resume/manage.py makemigrations multisites
	python awesome_resume/manage.py migrate


# target: clean_migration - folders in all django apps
clean_migrations:
	ls awesome_resume/ | grep -v -e 'manage.py' | xargs -I{} rm -rf awesome_resume/{}/migrations/


# target: test - execute project related tests including coding convention and unittest
test:
	flake8 awesome_resume/
	awesome_resume/manage.py test awesome_resume/ -v 2
