
from tkinter import SCROLL
from textual.app import App
from textual.widgets import Header, Footer, ScrollView, Placeholder
from textual import views
from textual import events


from rich.text import Text
from rich.table import Table

from textual_inputs import TextInput


class HabitsApp(App):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.title = "Habits"
        
    async def on_load(self):
        await self.bind("q", "quit", "Quit")
        await self.bind("b", "view.toggle('habits_menu')", "Toggle menu")
        
        
    async def on_mount(self):
        self.habit_input = TextInput(name="new_habit", placeholder="Enter new habit: ", title="Input")
        self.footer = Footer()
        self.header = Header()
        self.body = ScrollView()
        self.habits_list = Placeholder(name="Habits")

        await self.view.dock(self.header, edge="top")
        await self.view.dock(self.footer, edge="bottom")
        await self.view.dock(self.habits_list, edge="left", size=30, name="habits_menu")
        await self.view.dock(self.habit_input, self.body, edge="top", name="Tracker")
        # await self.view.dock(self.habit_input, edge="bottom")
        
        
        
if __name__ == "__main__":
    app = HabitsApp()
    app.run()
        