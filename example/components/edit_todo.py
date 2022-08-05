from django_unicorn.components import UnicornView


class EditTodoView(UnicornView):
    todo = None
    is_editing = False
    title = ""

    def edit(self):
        self.is_editing = True

    def cancel(self):
        self.is_editing = False

    def save(self):
        self.todo.save()
        self.cancel()