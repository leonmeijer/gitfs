# Copyright 2014-2016 Presslabs SRL
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import threading


class _AtomicCounter:
    """Thread-safe integer counter. Replaces unmaintained atomiclong package."""

    def __init__(self, val=0):
        self._val = val
        self._lock = threading.Lock()

    def increment(self, n=1):
        with self._lock:
            self._val += n

    def decrement(self, n=1):
        with self._lock:
            self._val -= n

    @property
    def value(self):
        with self._lock:
            return self._val


syncing = threading.Event()
sync_done = threading.Event()

push_successful = threading.Event()
push_successful.set()

fetch_successful = threading.Event()
fetch_successful.set()

idle = threading.Event()
idle.clear()

read_only = threading.Event()
fetch = threading.Event()
shutting_down = threading.Event()

writers = _AtomicCounter(0)

remote_operation = threading.Lock()
