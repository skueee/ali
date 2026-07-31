# Ali

A tool to create "aliases", custom commands to run much longer ones easily and to manage them.


## Getting Started

### Dependencies

* Linux (tested on Arch. If it does not work on your distro, open an issue)
* Pipx

### Installing

Execute :
```
sudo pipx install https://github.com/skueee/ali.git --global
```
Then :
```
sudo ali configure
```

### Executing program

To create a command, execute `ali create [command name] "[command]"`. You can use the -g or --global flag with sudo to make this command available globally

To list commands, execute `ali manage list`. To delete/edit a command, execute `ali manage [command] [remove/edit]`

## Contributors

<a href = "https://github.com/skueee/ali/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=skueee/ali"/>
</a>

## Features

- Create commands
- Make commands available globally
- Manage commands

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
