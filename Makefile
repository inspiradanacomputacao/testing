clean:
	find . -name "*.pyc" -exec rm -rf {} \;

migrate:
	python manage.py migrate
migrations:
	python manage.py makemigrations
user:
	python manage.py createsuperuser

shell:
	python manage.py shell