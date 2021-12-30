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

# Firmware reverse engineering
## Different functions
- 0x10469138 - Firmware update related stuff
- 0x10472894 - EEPROM related stuff
- 0x1048846E - Debug menu page 1
- 0x10488AE4 - Debug menu page 2
- 0x1048911E - Debug menu page 3
- 0x1051F24E - Debug menu page 4
- 0x104B57EE - Loads the script
- 0x104B5EAA - Some script interpreter code
- 0x104B640A - Interpreter printing code, atleast for variables

Look for 0x9F8(reg)(32-bit address of ascii string)!

## Gameplan to run custom code on the camera
1) Identify file loading functions in the firmware
2) Inject a custom function, that loads code from the SD-card to RAM and jumps to it.
3) ???
4) Profit!

More fun but not possible (yet) ways of executing custom code
- Find a exploit in the script interpreter and make it run code from the firmware

