from fabric import Connection
from invoke import run, task
from project import local_settings


@task(aliases=["d"])
def deploy(c):
    conn = Connection(local_settings.FABRIC_HOST)
    conn.run("cd ~ && "
             f"source {local_settings.FABRIC_VIRTUAL_ENV}/bin/activate && "
             f"cd {local_settings.FABRIC_WD} && "
             "git checkout master && "
             "git reset HEAD --hard && "
             "git clean -f -d && "
             "git pull && "
             "pip install --upgrade pip && "
             "pip install -r requirements.txt && "
             "python manage.py migrate && "
             "python manage.py collectstatic --no-input && "
             f"sudo {local_settings.FABRIC_RESTART_PROJECT} && "
             f"sudo {local_settings.FABRIC_RESTART_NGINX} ")


@task(aliases=["f"], default=True)
def full(c):
    run("git pull && git push")
    deploy(c)
