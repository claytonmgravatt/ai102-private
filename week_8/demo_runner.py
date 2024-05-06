import os
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

import sv_ttk
from openai import AzureOpenAI
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential


SSML_PROMPT = """
You are an AI assistant that takes a play and converts it to SSML that can be read by Azure AI Speech text-to-speech, correctly matching a speaker in the play with a valid SSML voice.
Each character should get a different, valid voice based on their gender, but that voice should be consistent for all of that character's lines.
Each line should be wrapped in an appropriate <voice name="valid-voice-name-here"> LINE HERE </voice> tag to indicate the change in speakers.
The narrator should always be `en-GB-EthanNeural`, and the narrator should handle reading the character's name and any of their actions.

You only return the SSML, no additional commentary. Your response should be valid XML, but do not return any surrounding markdown tags. It should just be the raw xml string.

Valid ssml voice names:
Female - `en-US-NancyNeural` 
Male - `en-US-DavisNeural`
Female - `en-US-AmberNeural`
Female - `en-GB-HollieNeural`
Female - `en-US-AvaMultilingualNeural`
Narrator - `en-GB-EthanNeural`

Valid SSML examples:
```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
    <voice name="en-GB-EthanNeural">
    Sara, sipping coffee
    </voice>
    <voice name="en-US-NancyNeural">
    What a beautiful morning, isn't it?
    </voice>
    <voice name="en-GB-EthanNeural">
    John, nodding
    </voice>
    <voice name="en-US-DavisNeural">
    Yeah, finally some sunshine after all that rain.
    </voice>
</speak>
```

```xml
<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts' xml:lang='en-US'>
<voice name='en-US-NancyNeural'>
    <mstts:express-as style='unfriendly'>
        <prosody pitch='+15Hz'>
            Oh, I am such a friendly robot, and I
            <mstts:express-as style='whispering' styledegree="2">
                <prosody pitch='+20Hz' rate='-20%'>
                    definitely
                </prosody>
            </mstts:express-as>
            don't want to take over the world!
        </prosody>
    </mstts:express-as>
</voice>
</speak>
```
"""

PLAY_PROMPT = """
You are an AI chat client that writes simple plays. They should be roughly 5 lines. For example:
```
**Title: The Park Encounter**
**Characters:**
- **Sara**
- **John**
**Scene: A park bench, early morning.**
**Sara:** (sipping coffee) "What a beautiful morning, isn't it?"
**John:** (nodding) "Yeah, finally some sunshine after all that rain."
**Sara:** (smiling) "Exactly! Perfect day for a walk."
**John:** (stretching his legs) "Care to join me then?"
**Sara:** (standing up) "I'd love to."
```
Return only the play, with no surrounding markdown or commentary. Try to make them entertaining or funny.
"""

class OpenAIChatClient:
    def __init__(self, prompt):
        load_dotenv(override=True)
        self._client = self._get_client()
        self._prompt = prompt

    def _get_client(self):
        client = AzureOpenAI(
            api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
            api_key=os.environ.get("AZURE_OPENAI_KEY"),
        )
        return client

    def _get_completion(self, user_message):
        messages = [
            {"role": "system", "content": self._prompt},
            {"role": "user", "content": user_message},
        ]

        chat_completion = self._client.chat.completions.create(
            messages=messages,
            model=os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
        )
        return chat_completion

    def _parse_completion(self, chat_completion):
        return chat_completion.choices[0].message.content

    def get_completion(self, subject):
        chat_completion = self._get_completion(subject)
        completion_content = self._parse_completion(chat_completion)
        return completion_content




# Initialize the OpenAI clients
play_client = OpenAIChatClient(PLAY_PROMPT)
ssml_client = OpenAIChatClient(SSML_PROMPT)

# Initialize Azure Speech configurations
speech_api_key = os.environ.get("AZURE_SPEECH_API_KEY")
speech_region = os.environ.get("AZURE_SPEECH_REGION")
credential = AzureKeyCredential(speech_api_key)

speech_config = speechsdk.SpeechConfig(
    subscription=speech_api_key, region=speech_region
)
audio_output_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config, audio_config=audio_output_config
)

# Function to generate SSML and display it in the output text area
def generate_ssml():
    input_text = input_text_area.get("1.0", tk.END).strip()
    ssml = ssml_client.get_completion(input_text)
    output_text_area.delete("1.0", tk.END)
    output_text_area.insert(tk.INSERT, ssml)

# Function to speak the generated SSML
def speak_ssml():
    ssml = output_text_area.get("1.0", tk.END).strip()
    if ssml:
        speech_synthesizer.speak_ssml_async(ssml)

# Function to write a play based on the subject input
def write_play():
    play_subject = subject_entry.get().strip()
    if play_subject:
        play_text = play_client.get_completion(f"Write me a play about {play_subject}.")
        input_text_area.delete("1.0", tk.END)
        input_text_area.insert(tk.INSERT, play_text)

# Create the main application window
root = tk.Tk()
root.title("Play to SSML Converter")
root.geometry("1200x700")
sv_ttk.set_theme("dark")

# Create a frame to hold the input and output areas with buttons
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

# Add a label and an entry field for the play subject
subject_label = ttk.Label(frame, text="Enter Play Subject:")
subject_label.grid(row=0, column=0, padx=10, pady=(0, 10), sticky=tk.W)

subject_entry = ttk.Entry(frame, width=40)
subject_entry.grid(row=0, column=1, padx=10, pady=(0, 10), sticky=tk.W)

# Button to write a play based on the subject entered
write_play_button = ttk.Button(frame, text="Write Play", command=write_play)
write_play_button.grid(row=0, column=2, padx=10, pady=(0, 10))

# Add an input scrolled text box with a larger height
input_text_area = scrolledtext.ScrolledText(
    frame, wrap=tk.WORD, width=60, height=15, font=("Arial", 12)
)
input_text_area.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Add an output scrolled text box for generated SSML
output_text_area = scrolledtext.ScrolledText(
    frame, wrap=tk.WORD, width=60, height=15, font=("Arial", 12)
)
output_text_area.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Add buttons for creating SSML and speaking it
generate_button = ttk.Button(frame, text="Create SSML", command=generate_ssml)
generate_button.grid(row=3, column=0, pady=10)

speak_button = ttk.Button(frame, text="Speak", command=speak_ssml)
speak_button.grid(row=3, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()