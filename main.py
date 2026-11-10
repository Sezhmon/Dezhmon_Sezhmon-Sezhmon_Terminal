# Sezhmon Terminal
# Copyright 2026 Mohammad Taha Barati (known as Dezhmon_Sezhmon)
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0





from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

from STD_OUT import Setup_Terminal_Stdout
import Commands


Main_Welcome_Logo = r"""
 ____           _                           
/ ___|  ___ ___| |__  _ __ ___   ___  _ __  
\___ \ / _ \_  / '_ \| '_ ` _ \ / _ \| '_ \ 
 ___) |  __// /| | | | | | | | | (_) | | | |
|____/ \___/___|_| |_|_| |_| |_|\___/|_| |_|"""



Main_Welcome_Text = """
In the name of God, the Most Gracious, the Most Merciful

Hello everyone .
____________________________________________
To begin, please enter the /help command .
____________________________________________
To visit our official website, please enter the /site command .
____________________________________________
For more information, please enter the /info command .
____________________________________________

 """

class MainApp(App):
    
    def build(self):
        
        layout = BoxLayout(orientation='vertical', padding = 20, spacing = 10)
        
        self.prompt = "Sezhmon==>   "
        
        self.Terminal_Label = Label(
            text = Main_Welcome_Logo + "\n" + Main_Welcome_Text,
            font_size=24,
            #multiline=True,
            #readonly=True,
            halign = "left",
            valign = "top",
            #background_color=(0.7, 0.7, 0.7, 0.9),
            color=(0, 0.3, 0.8, 1),
            
            #use_bubble = False,
            #use_handles = False,
            size_hint_y = None,
            font_name = "Mat/Fonts/Normal/Normal.ttf"
        )
        

        
        self.Command_Input = TextInput(
            
            hint_text = "Enter Sezhmon Terminal Command",
            font_size = 28,
            size_hint_y = None,
            height = 100,
            multiline = False,
            
            background_color = (0.7, 0.7, 0.7, 0.9),
            foreground_color = (0, 0.3, 0.8, 1),
            
        )
        
        self.Terminal_Label.bind(width=lambda inst, w: setattr(inst, 'text_size', (w, None)))
        
        self.Terminal_Label.bind(texture_size=lambda inst, s: setattr(inst, 'height', s[1]))
        
        self.Terminal_Scroll = ScrollView(do_scroll_x=False, bar_width=10)
        
        self.Terminal_Scroll.add_widget(self.Terminal_Label)
        
        self.Command_Input.bind(on_text_validate = self.On_Enter_Pressed)
        
        
        layout.add_widget(self.Command_Input)
        layout.add_widget(self.Terminal_Scroll)
        
        Setup_Terminal_Stdout(self.Terminal_Label, self.Terminal_Scroll)
        
        
        return layout
    
    
    
    
    
    
    
    def On_Enter_Pressed(self, instance):
            
            Current_Command = instance.text.strip()
            
            instance.text = ""
            
            if not Current_Command:
                
                return
            
            
            self.Terminal_Label.text += f"\n{self.prompt}{Current_Command}\n"
            
            Commands.Commands(Current_Command)
            
            if Current_Command == "clear":
            	
            	self.Terminal_Label.text = self.prompt
            
            
            if Current_Command == "old-langu":
            	
            	self.Terminal_Label.font_name = "Mat/Fonts/Old/Old.TTF"
            	
            
            if Current_Command == "normal-langu":
            	
            	self.Terminal_Label.font_name = "Mat/Fonts/Normal/Normal.ttf"
            	
            	
            
            #self.Terminal_Box.cursor = self.Terminal_Box.get_cursor_from_index(len(self.Terminal_Box.text))
            
            self.Terminal_Scroll.scroll_y = 0
        
if __name__ == '__main__' :
    
    MainApp().run()