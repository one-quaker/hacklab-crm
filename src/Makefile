RUN=$(ENV_PYTHON_BIN) manage.py
APP=web_app

dev:
	$(RUN) runserver 0.0.0.0:8000

bot:
	$(ENV_PYTHON_BIN) bot.py

run:
	$(ENV_BIN_ROOT)/gunicorn $(APP).wsgi:application --name $(APP) --workers 2 --bind=0.0.0.0:8000 --reload --log-level=info --log-file=-

clean:
	rm -rfv *~*
	find . -name '*.pyc' -exec rm -fv {} \;

shell:
	$(RUN) shell_plus

makemigrations:
	$(RUN) makemigrations

showmigrations:
	$(RUN) showmigrations

migrate: clean
	$(RUN) migrate

collectstatic:
	$(RUN) collectstatic --noinput

create_admin:
	echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | $(RUN) shell
