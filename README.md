# pi-voice
Raspberry Pi Voice

**Python**: 3.5.3

## Run

```bash
$ python3 app.py --log=INFO
```

## Daemon

```bash
$ sudo cp pi-voice /etc/init.d/pi-voice
$ sudo chmod 755 /etc/init.d/pi-voice
$ sudo update-rc.d pi-voice defaults

```

## Install pip3

```bash
sudo apt-get install python3-pip
```

## Install packages

```bash
pip3 install -r requirements.txt
```

## Install player

```bash
sudo apt-get install omxplayer
```
