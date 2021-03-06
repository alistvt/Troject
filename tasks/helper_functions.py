from .models import Task
import logging

logger = logging.getLogger(__name__)

def getTasksCategorized(tasks):
    """
    getTasksCategorized(tasks)
    gets a queryset
    and returns a `dict` containing keys
    which are `group name` and values are
    that group's tasks
    """
    groups = Task.Groups.choices
    grouped = dict()
    for group, groupName in groups:
        grouped[groupName] = tasks.filter(group=group)
    return grouped
