from exam.models import User, Project, Task


def create_project_mutate(name, description, owner, assignees):
    owner = User.objects.get(pk=owner)
    project = Project(
        name=name,
        description=description,
        owner=owner,
        assignees=assignees
    )
    project.save()
    return project

def create_task_mutate(name, description, owner, assignees, project, status, deadline):
    owner = User.objects.get(pk=owner)
    task = Task(
        name=name,
        description=description,
        owner=owner,
        assignees=assignees,
        project=project,
        status=status,
        deadline=deadline
    )
    task.save()
    return task