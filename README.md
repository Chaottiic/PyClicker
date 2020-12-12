
# PyClicker
Python Auto Clicker

### Coming Soon
- GUI coming soon.
- setup.py coming soon.


## How to install for Development:
- Run the following commands in your terminal.
- - `git clone https://github.com/Chaottiic/PyClicker`
- - `cd PyClicker`
- - `virtualenv venv`
- - `source venv/bin/activate`
- - `pip install -r requirements.txt`
- - `python main.py`
- Before running `python main.py`, make sure to edit the following variables below in the top of `main.py`.

### Variables:
- `DELAY` = `0.005`
- - Delay is in seconds.
- `TOGGLE_KEY` = `Key.shift_r`
- `END_KEY` = `Key.end`
- - You can find the supported keyboard keys <a href="https://pynput.readthedocs.io/en/latest/_modules/pynput/keyboard/_base.html#Key">here!</a>
- `MOUSE_BUTTON` = `Button.right` 
- - Supported Mouse Buttons are `Right`, and `Left`.

## License
- MIT