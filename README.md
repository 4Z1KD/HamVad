# HamVad 🌺
Voice Activity Detector for ham radio 📻

# prerequisite 🖐️
1. python (https://www.python.org/downloads/)

# Installation 🛠
1. create virtual environment (python -m venv hamvad) ☁️
2. activate the venv (Scripts\activate.bat) 🌬️
3. copy this project's files to the venv directory 📑
4. install the requirements (pip install -r requirements.txt) 🧰
5. upload the arduino code to your board of choice 📂

## com ports ✏️
make sure to set the correct COM ports in vad.py<br/> 
```
ser = serial.Serial('COM5', 9600)
```

# usage 🚀
launch run.bat (this will activate the venv and run the script)

# what to expect 🤷‍♀️
VAD algorithms are somewhat sensitive to the input volume so you may want to adjust that for best results.</br>

73,<br/>
Gil 4Z1KD
