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