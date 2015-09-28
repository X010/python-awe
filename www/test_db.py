# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'Jeffwu'

from models import User, Blog, Comment
from transwarp.orm import StringField,Field

from transwarp import db

db.create_engine(user='root', passwd='', database='awesome')

u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

print isinstance(u.name,StringField)


#u.insert()

#print 'new user id:', u.id

#u1 = User.find_first('where email=?', 'test@example.com')
#print 'find user\'s name:', u1.name

#u1.delete()

#u2 = User.find_first('where email=?', 'test@example.com')
#print 'find user:', u2
