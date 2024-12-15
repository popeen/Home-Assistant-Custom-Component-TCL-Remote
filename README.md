
  
## Home Assistant Custom Component: TCL Remote

[![GitHub Release][releases-shield]][releases]
[![downloads-shield]][release-link]
![Project Stage][project-stage-shield]
[![issues-shield]](issues)
[![License][license-shield]](LICENSE.md)
[![hacs_badge][hacs-shield]][hacs]
[![Buy me a coffee][buymeacoffee-shield]][buymeacoffee]

This custom component will give you two new services for controlling TCL Smart TVs (Non android version). Tested on my S69 series TV.\
I have seen some reports about it working on other brands as well, mainly Thomson

***After installing it using HACS*** you need to register the services, this can be done by two different methods.

**Method 1.**

Click this button to add it using config flow

[![add-integration-shield]][add-integration]

**Method 2.** (Deprecated)

Add the following to your configuration.yaml and then restart Home Assistant
```  
tcl_tv_remote:
```  


**Send key**\
This service will send a key command/button press to your TV, see [Key List](KEYS.md)
|Parameter| What to put |
|--|--|
| ip| Your TVs IP address|
| port| The port your TV listens to, most likely 4123 |
| key | The code of the key you want to "press"|
```  
service: tcl_tv_remote.send_key
data:
  key: TR_KEY_SOURCE
  ip: 192.168.0.181
  port: 4123

```  
**Go to source**\
This service will send the key presses needed for changing the input/source.\
Since we don't know the current input and there is no input specific button this is done by first going to tv input and then we can navigate to the correct one.
|Parameter| What to put |
|--|--|
| ip| Your TVs IP address|
| port| The port your TV listens to, most likely 4123 |
| source | The source/input you want to use, begin counting from 0  |

```
service: tcl_tv_remote.go_to_source
data:
  source: 3
  ip: 192.168.0.181
  port: 4123

```

[downloads-shield]: https://img.shields.io/github/downloads/popeen/Home-Assistant-Custom-Component-TCL-Remote/total
[release-link]: https://github.com/popeen/Home-Assistant-Custom-Component-TCL-Remote/releases
[releases-shield]: https://img.shields.io/github/release/popeen/Home-Assistant-Custom-Component-TCL-Remote.svg
[releases]: https://github.com/popeen/Home-Assistant-Custom-Component-TCL-Remote/releases
[project-stage-shield]: https://img.shields.io/badge/project%20stage-ready%20for%20use-green.svg
[issues-shield]: https://img.shields.io/github/issues-raw/popeen/Home-Assistant-Custom-Component-TCL-Remote.svg
[license-shield]: https://img.shields.io/github/license/popeen/Home-Assistant-Custom-Component-TCL-Remote.svg
[hacs-shield]: https://img.shields.io/badge/HACS-Default-41BDF5.svg
[hacs]: https://github.com/custom-components/hacs
[buymeacoffee-shield]: https://img.shields.io/badge/donation-Buy%20me%20a%20coffee-orange
[buymeacoffee]: https://www.buymeacoffee.com/popeen
[add-integration-shield]: https://my.home-assistant.io/badges/config_flow_start.svg
[add-integration]: https://my.home-assistant.io/redirect/config_flow_start/?domain=tcl_tv_remote
