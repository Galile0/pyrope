# PyRope - Rocket League Replay Parser
The goal of this Project is to parse and decode replay files of the game Rocket League.
Decoding is done as far as possible, although there may always be new objects added to the game, resulting in parsing errors. In such cases please open an issue, and I'll try to fix it

# Installation

## Requirements
* Bitstring (https://pypi.python.org/pypi/bitstring)
* Python 3+ (Developed on python 3.4 but any 3+ version should work)

## Setup
Grab the source from this git and run
setup.py install 
Note: That's totally untested and until further notice here, shit may break. In case of doubt just copy pyrope to your project root

# Usage

## Getting Started:
```python
from pyrope import Replay

replay = Replay("FILEPATH")
replay.parse_netstream()
```
Depending on the size of your Replay file the parse_netstream() will take some time (For full fledged matches roughly one minute)
Therefor parse_netstream() offers you two objects for commincation while running threaded. These are *qout* for getting progress updates and *ev* as an Event Flag to interrupt the parsing Process. Example for threaded parsing:
```python
import time
from threading import Thread, Event
from queue import Queue

from pyrope import Replay

replay = Replay("FILEPATH")
status = Queue()
stop = Event()
thread = Thread(target=replay.parse_netstream, args=(status, stop))
thread.start()
while True:
    if status.empty():  # wait for status update
        time.sleep(0.1)
        continue
    i = status.get()
    if i == 'done':
        break
    elif i == 'exception':
        exc = status.get()
        raise exc
    elif i % 100 == 0:
        print(i)
```
This prints out the currently processed Frame every 100 Frames parsed. You can also get the amount of total frames for percentage based display with
```python
max(self.replay.netstream, key=int)
```

The stop Event is not used in this example, but you would simply need to call stop.set() to end the thread gracefully. This would allow to restart the netstream parsing from the beginning (Made progress is lost). You can also kill the Thread, but that will likely leave the netstream in a state where it can't be started again until you recreate the replay object from scratch.


## Working with parsed replays
The parsed replay is a dictionary of Frames, in the form {FrameNumber: FrameContent} where FrameContent consists of time information for that frame and another dict with actors which got referenced in that frame. Accessing the information is as easy as accessing the information in a dict structure.
```python
from pyrope import Replay

replay = Replay("FILEPATH")
replay.parse_netstream()
for num, content replay.netstream.items():
    print("Frame %d" % num)
    print("Actors:")
    for shortname, actor_data in content.items():
        print("\tShortname: %s" % shortname)
        print("\tPropertys: %s" % content['data']
```
This will print all Frames with their actors and the Propertys of each actor (Note: You may want to pipe that output since a frame usually lasts 0.04 seconds and a match takes 5 Minutes = 300 seconds = 7500 frames with up to a few dozen actors per frame, and each actor with a handful of propertys. Thats alot of data).

At the time of writing this I have not documented the produced dictionary structure. Therefor it is recommended to simply write the parsed replay in a human readable form on disk and work from there.
```python
from pyrope import Replay

replay = Replay("FILEPATH")
replay.parse_netstream()
with open('/netstream.json', 'w', encoding='utf-8') as outfile:
    outfile.write(replay.netstream_to_json())

with open(filename+'/metadata.json', 'w', encoding='utf-8') as outfile:
    outfile.write(replay.metadata_to_json())
```
The parsed Netstream file can get quite large. Keep that in mind when trying to view it in your preferred editor.

# License
This Project is published under GNU GPL v3.0
It would also be nice if you drop me a notice (Mail or Github) if you made something publicly available using this package.

# Credits and Sources
Existing Parsers which this is partly based on https://github.com/danielsamuels/rocket-league-replays/wiki/Rocket-League-Replay-Parsers

Thread with people working hard on understanding the replay structure http://www.psyonix.com/forum/viewtopic.php?f=33&t=13656

The awesome game Rocket League http://store.steampowered.com/app/252950 owned by Psyonix
