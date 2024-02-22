# Google Gemma + Boomi Local Atom
This design lets you call a local copy of the Google Gemma large language model, from a Boomi atom installed on the same device. 

You'll need a local atom setup, the scripts here should automatically downalod google gemma on the first run of the script once you've accepted the T&C's in hugging face and have setup a .env file with your huggingface access ID. 

https://huggingface.co/google/gemma-2b-it

I was working from the 2b instruct model and it runs nicely on my macbook pro. I would imagine the 7b parameter model might strain this laptop a bit, but I would expect a decent gaming computer to handle it.

One you've got the local atom setup the sample boomi process will call into boomi_gemma.py with a data process shape using the terminal command that was 'staged' in the previous message shape. You might need to modify the command based on windows vs unix operating system (as mentioned mine runs on a Mac).
