# Ali

A tool to create "aliases", custom commands to run much longer ones easily and to manage them.


## Getting Started

### Dependencies

* Linux (tested on Arch. If it does not work on your distro, open an issue)
* Pipx

### Installing

Execute :
```
sudo pipx install git+https://github.com/skueee/ali.git --global
```
Then :
```
sudo ali configure
```

### Executing program

To create an alias, execute `ali create [alias] "[command]"`. You can use the -g or --global flag with sudo to make this alias available globally

To list aliases, execute `ali manage list`. To delete/edit an alias, execute `ali manage [alias] [remove/edit]`

## Contributors

<a href = "https://github.com/skueee/ali/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=skueee/ali"/>
</a>

## Features

- Create aliases
- Make aliases available globally
- Manage aliases

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
