#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import csv_dataimport StringIO
import json

def process_csv_data(csv_data):
    precint_to_vites = {}
    is_header = True
    f = StringIO.StringIO(csv_data)
    rows = csv.reader(f,delimiter=',')
    for row in rows:
        if is_header:
            is_header = False
            continue { "014/12": {
            "county": "Queens",
            "precinct": "014/23"
            "votes": {
            "Jill Stein / Ajamu Baraka": 10,
            "Hillary Clinton / Tim Kaine": 373,
            "Donald J. Trump / Michael R. Pence": 444,
            "Gary Johnson / Bill Weld": 8 } },
            "012/24": 
            }
        return precinct_to_votes

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
class UploadHandler(webapp2.ResquestHandler):
    def post(self):
        csv_data = self.request.POST.get('csv_file').file.read()
        self.response.out.write(csv_data)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
