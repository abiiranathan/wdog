# Watch Dog

### __author__ = 'Dr. Abiira Nathan'

A File system watch dog. Fit for monitoring and reloading a server
configuration file.
Based on watchdog module

# Installation
```pip install wdog```

Example Usage:
```
from wdog import WatchDog
import config

def reload_config():
    print("Reload server configiguration file")
    import importlib
    importlib.reload(config)
    # Assuming config reads reads settings from config.ini


dog = WatchDog(callback=reload_config, folder_to_track='.',
include_patterns=['*/config.ini'])
try:
    dog.monitor_forever()
except(KeyBoardInterrupt, EOFError):
    print('Bye!')

```
You can extend this to do some fancy things.