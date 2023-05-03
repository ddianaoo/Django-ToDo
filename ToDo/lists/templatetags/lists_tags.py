from django import template
from lists.models import *
from django.db.models import *
from django.db.models import Q

register = template.Library()


@register.inclusion_tag('lists/show_notifications.html')
def get_need_todo_by_list(user=None, id=None):
    tasks = Task.objects.filter(Q(list__user__id=user.id)&Q(list__invite=1)&Q(is_done=0)&Q(list__id=id))
    time_now = datetime.time(datetime.now())

    tasks_past = []
    tasks_future = []
    for task in tasks:
        if time_now < task.at_time:
            tasks_future += [task]
        else:
            tasks_past += [task]
    return {"tasks_past": len(tasks_past), "tasks_future": len(tasks_future)}