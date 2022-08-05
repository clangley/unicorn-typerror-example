from django_unicorn.components import UnicornView
from example.models import Todo

class ListTodosView(UnicornView):
    todos = Todo.objects.none()

    def mount(self):
        self.todos = Todo.objects.all().order_by("-id")[:5]