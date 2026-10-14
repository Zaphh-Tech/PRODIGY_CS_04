# My Prodigy Task 4 - Keylogger (practice only)

Small keylogger I made to learn how keyboard listeners work. Only tested on my own laptop.

It saves keys to `keystrokes.log` with timestamps. Press ESC to stop.

## please read

Only use on your own machine. Don't log other people. See `consent_notice.txt`.

No network stuff in here, no autostart, nothing hidden. You have to type YES or it quits.

## how to run

```
pip install pynput
python3 keylogger.py
```

Custom file:
```
python3 keylogger.py --output mylog.txt
```

Type, then press ESC. Delete the log when done:
```
rm keystrokes.log
```

Needs a real desktop (wont work over plain ssh, thats normal).
