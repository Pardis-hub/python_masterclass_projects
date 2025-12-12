import os
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

image_endings = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')
Window.size = (600, 500)

class GalleryApp(App):
    def build(self):

        self.image_files = []
        self.index = 0

        # main_layout 
        main_layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        # Entry bar for getting folder path from user and load button
        entry_bar = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.path_entry = TextInput(
            hint_text="Enter folder path...", size_hint_x=0.8, multiline=False
        )
        load_btn = Button(text="Load", size_hint_x=0.2)
        load_btn.bind(on_release=self.load_images)

        entry_bar.add_widget(self.path_entry)
        entry_bar.add_widget(load_btn)

        # Image display 
        self.img = Image(allow_stretch=True, keep_ratio=True)

        # Next and Previous buttons
        btn_bar = BoxLayout(size_hint_y=None, height=50, spacing=10)
        prev_btn = Button(text="Previous")
        next_btn = Button(text="Next")

        prev_btn.bind(on_release=self.show_prev)
        next_btn.bind(on_release=self.show_next)

        btn_bar.add_widget(prev_btn)
        btn_bar.add_widget(next_btn)

        # Add widgets to main_layout
        main_layout.add_widget(entry_bar)
        main_layout.add_widget(self.img)
        main_layout.add_widget(btn_bar)

        return main_layout

    # Loads images when user clicks the Load button
    def load_images(self, *args):

        folder = self.path_entry.text

        if not os.path.isdir(folder):
            self.img.source = ""
            self.image_files = []
            return

        self.image_files = [
            os.path.join(folder, f)
            for f in os.listdir(folder)
            if f.lower().endswith(image_endings)
        ]

        if self.image_files:
            self.index = 0
            self.img.source = self.image_files[self.index]
            self.img.reload()

    def show_next(self, *args):
        if not self.image_files:
            return
        self.index = (self.index + 1) % len(self.image_files)
        self.img.source = self.image_files[self.index]
        self.img.reload()

    def show_prev(self, *args):
        if not self.image_files:
            return
        self.index = (self.index - 1) % len(self.image_files)
        self.img.source = self.image_files[self.index]
        self.img.reload()

GalleryApp().run()
