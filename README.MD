# Pentax K10D scripting

Things I've found out:

* `MODSET.xxx` and `AUTORUN.xxx` don't necesserally have to be with the same extensions,
for example my camera has `MODSET.TXT` and `AUTORUN.421` with firmware 1.30.0.
* `AUTORUN` does not support escaped strings, for example `PRINT "\n\r"` would just print `\n\r`.
* The interpreter can't handle lines that are longer than 79 characters. (Split your long comments over multiple lines!) Lines longer than the 79 character limit will make the camera unresponsive, in same cases even to the on/off switch.
* The screen is 26 characters wide and 10 lines tall. Lines longer than 28 characters wrap around, displaying over the previously drawn characters. After 10 lines the screen wraps around and starts overwriting the first line.
* All of the ASCII characters can be displayed, except `"` because it ends the string.
* Setting languages seems weird and can cause crashes
* 18 different colors? (Need to check again)
* Use `GOSUB <label>` to call a function, labels can be defined as `<label>:`. Both upper and lower case work.
* Use `ALLCLR` to clear the screen, don't make your own function :)
* `CLS x1 n x2` Clears `n` number of lines starting from line `x1` and sets the cursor to line `x2` afterwards, lines are 0-indexed

## Commands to document
- `FSEARCH`
- `INTERVAL`
- `CYCLE`
- `TIMERON` `TIMEROFF`
- `IFGOSUB`
- `WAIT`
- `LANGUAGE` 
