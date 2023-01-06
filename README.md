# Pico-Ducky-Code-Injector-GUI

Inject any code file into someone's computer and execute using this Python script with a GUI interface. It has different modes of executing code. This can be through one terminal command, through a variety of text editors and through different operating systems such as Windows and Mac. The way it works for these techniques is the same: 

1. It opens  spotlight search or the windows search bar.

2. It writes the file with the extension of their choice and saves this to the same directory.

3. It executes this command using the appropiate scripting language.


### Bugs and Pull requests

Currently it has been tested on MAC only so if a bug occurs, please issue a pull request. Next to that you can add a command which makes an alias of Python 3 and add the delay through the entire script. Next to that you can delete all the comments and white spaces to make your code as compact as possible. 

### Future updates

A major update could be to add a function which saves a file to a hidden directory. Another feature could be to randomize waiting times in a certain range to make the HID seem more like a human actor and not a HID. Next to this there could be updates to make it more versatile.

## 1. Setting up script

Tkinter is the only requirement for this script. This can be downloaded using the following command: "Pip install Tkinter". 

![GUI at startup](https://github.com/Maxbladt/Pico-Ducky-Code-Injector-GUI/blob/a6274ffff272f5c3e3734522e1112b91f96b7794/images/GUI_empty.png)

## 2. Working of Pico-Ducky-Code-Injector

To Begin input your python code (or another programming language code - Not tested) and click convert. In the normal payload you will see comments using the command (REM COMMENTS). Before converting  you can tweak a lot different things such as the waiting time. 100 (ms) has been tested for a mac to work with inputting python script using the terminal.

![Working of Pico-Ducky-Code-Injector](https://github.com/Maxbladt/Pico-Ducky-Code-Injector-GUI/blob/1cb418a260986a14c5c2eed3eb6bb33a637a5580/images/Example_Normal_payload.png)

## 2. Payload shortening

The comments are made to be readable and explained using REM comments. Ofcourse if you want to penetrate something you want these scripts to be as lightweight as possible. A feature called "Delete whitespace and REM comments" has been made in the form of a checkbox. If pressed it will produce the following output.

![Payload shortening](https://github.com/Maxbladt/Pico-Ducky-Code-Injector-GUI/blob/1cb418a260986a14c5c2eed3eb6bb33a637a5580/images/Example_Shortened_Payload.png)

## 2. Saving payload

The GUI has two to save payloads. One via the "Copy payload" button which copies the output, and one via the "Save payload" button which saves it to the same directory as "payload.dd". After having saved this payload you can upload it to your pico ducky or convert it and put it on your USB Rubber ducky. This is how your pico Ducky is supposed to look. If you plug it in it will imediately start injecting, saving and executing the python script.

![Saving payload](https://github.com/Maxbladt/Pico-Ducky-Code-Injector-GUI/blob/1cb418a260986a14c5c2eed3eb6bb33a637a5580/images/Example_Shortened_Payload.png)
![alt text]()
![alt text]()

