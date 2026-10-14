# PRODIGY_CS_04

A simple keylogger written in Python, built for Task 4 of the Prodigy InfoTech
Cyber Security internship. For learning only, on your own machine.

It records key presses to a local file with timestamps so you can see how keyboard
listeners work.

## What it does

- Logs keystrokes to `keystrokes.log` with a timestamp on each line
- Shows a consent screen first — you have to type YES or it quits
- Press ESC to stop
- No network code, no autostart, nothing hidden

## Ethics

Only run this on a computer you own. Logging other people's keystrokes without consent
is illegal. See `consent_notice.txt`. Delete the log when you're done.

## Setup

```bash
pip install pynput
```

Needs a real desktop session (won't work over plain SSH — that's normal).

## How to run

```bash
python3 keylogger.py

# custom output file
python3 keylogger.py --output mylog.txt
```

Type a bit, press ESC, then clean up:

```bash
rm keystrokes.log
```

## Example output

```
$ python3 keylogger.py
KEYLOGGER - Prodigy Task 4 (school exercise, local only)
...
type YES to continue: YES
logging... press ESC to stop
saving to: /home/user/.../keystrokes.log
```

## Files

- `keylogger.py` — the tool
- `consent_notice.txt` — the usage/ethics notice
