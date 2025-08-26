from flask import Flask, request, jsonify
import pyautogui
import webbrowser
import time

app = Flask(__name__)

def run_step(step):
    tool = step["tool"]
    action_data = step["action"].split("|")

    if tool == "webbrowser":
        action = action_data[0]
        if action == "open":
            url = action_data[1]
            webbrowser.open(url)
    elif tool == "pyautogui":
        action = action_data[0]
        if action == "click":
            x, y = int(action_data[1]), int(action_data[2])
            pyautogui.click(x, y)
        elif action == "type":
            text = action_data[1]
            pyautogui.typewrite(text)
        elif action == "press":
            key = action_data[1]
            pyautogui.press(key)
        elif action == "hotkey":
            key1, key2 = action_data[1], action_data[2]
            pyautogui.hotkey(key1, key2)
        elif action == "delay":
            ms = int(action_data[1])
            time.sleep(ms / 1000.0)

@app.route('/execute', methods=['POST'])
def execute_steps():
    data = request.json
    steps = data.get("steps", [])

    for step in steps:
        run_step(step)

    return jsonify({"status": "success", "message": "Steps executed."})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
