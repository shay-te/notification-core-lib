# NotificationCoreLib
NotificationCoreLib is built using [Core-Lib](https://github.com/shay-te/core-lib).

## Example

```python
import hydra
from notification_core_lib import NotificationCoreLib

hydra.core.global_hydra.GlobalHydra.instance().clear()
hydra.initialize(config_path='../../notification_core_lib/config')

# Create a new NotificationCoreLib using hydra (https://hydra.cc/docs/next/advanced/compose_api/) config
notification_core_lib = NotificationCoreLib(hydra.compose('notification_core_lib.yaml'))
```

## License
Core-Lib in licenced under [MIT](https://github.com/shay-te/core-lib/blob/master/LICENSE)
