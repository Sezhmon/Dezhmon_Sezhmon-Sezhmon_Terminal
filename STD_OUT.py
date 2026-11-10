# Sezhmon Terminal
# Copyright 2026 Mohammad Taha Barati (known as Dezhmon_Sezhmon)
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0



import sys

class ConsoleRedirector:
    def __init__(self, label, scroll):
        self.label = label
        self.scroll = scroll

    def write(self, message):
        if message:
            self.label.text += message
            self.scroll.scroll_y = 0

    def flush(self):
        pass

def Setup_Terminal_Stdout(label, scroll):
    sys.stdout = ConsoleRedirector(label, scroll)