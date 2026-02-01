<h1 align="center">ScreenTime Crack ⚙️🔐</h1>

<p align="center">
  Recover lost iOS Restrictions/ScreenTime PINs <b>from backups in seconds.</b><br>
  Suppors <b>iOS 4 - 11</b> using Brute-Force attack.
</p>


## Inspiration
When i was younger I had ScreenTime setup on my iPhone and sometimes it was very annoying. Years later after gaining some exprerience in computers and programming I decided to find a way how to extract the PIN from a phone. I was inspired by [this blog post](https://nbalkota.wordpress.com/2014/04/05/recover-your-forgotten-ios-7-restrictions-pin-code/) which undercovers how iOS was saving Salt + Target Key (the ingredients to the PIN) in the iPhone backup files and [PinFinder](https://github.com/gwatts/pinfinder) program.

If you want to know more about how this script works, [scroll down to: How It Works](#how-it-works)

## Installation
> [!IMPORTANT]
> **Windows executable coming soon** - no need to install Python and setup anything. 🙏

- Download and install [Python 3](https://www.python.org/downloads/)
- Download [this program](https://github.com/asisamko/ScreenTime-Crack/archive/refs/heads/main.zip) from GitHub
- Locate the downloaded folder in CMD/Terminal
  - Install requirements:
    - MacOS: ```pip3 install -r requirements.txt```
    - Windows: ```pip install -r requirements.txt```
  - Run the program
    - **MacOS:** ```python3 main.py```
    - **Windows:** ```python main.py```

## Features
- **Easy to use** - run the program, select the backup, wait a few seconds, done!
- **Auto-detect backups** - automatically detects and lists all backups from deafult system paths
- **Quick backups overview** - iOS version, device name, device type, backup date, backup location
- **Windows/MacOS supported** - Multi-platform support

### Updates
- [ ] Add **Custom Backup Location** option

## How It Works
*soon.* [-bibby](https://i.redd.it/1d0q5sasni091.jpg)

## Support
Found a bug or issue? Open a new issue in the [Issues tab](https://github.com/asisamko/ScreenTime-Crack/issues) or [create a fork](https://github.com/asisamko/ScreenTime-Crack/pulls) of this repo.

## Credits
Huge thanks to [PinFinder](https://github.com/gwatts/pinfinder) for inspiring me to create this program in first place and [this blog post](https://nbalkota.wordpress.com/2014/04/05/recover-your-forgotten-ios-7-restrictions-pin-code/) for detailed explanation how this method works and how to recreate PIN extraction.
#
**Made with 💖 by [asisamko](https://github.com/asisamko)**
