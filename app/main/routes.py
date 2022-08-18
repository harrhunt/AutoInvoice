from flask import render_template, current_app as app
from app.main import bp
from clockipy import Clockify


@bp.route("/")
def index():
    clockify = Clockify(app.config["CLOCKIFY_API_KEY"])
    workspaces = clockify.get_workspaces()
    projects = []
    users = []
    for workspace in workspaces:
        projects.extend(clockify.get_active_projects(workspace["id"]))
        users.extend(clockify.get_users(workspace["id"]))
    return render_template("index.html", workspaces=workspaces, projects=projects, users=users)
