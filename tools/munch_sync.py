import json
import os
import datetime


def process_munch_signal(signal_json_path):
    with open(signal_json_path, "r") as f:
        signal = json.load(f)

    target_path = signal["target"]

    # Logic: Append insight to 'Architectural Whys' and par~mi to 'Side Effects'
    with open(target_path, "r") as f:
        content = f.read()

    new_entry = f"\n- **Insight ({datetime.date.today()}):** {signal['insight']}"
    # Use string manipulation to find sections and inject
    content = content.replace(
        '## 🧠 Architectural "Whys" (savwiki)', f'## 🧠 Architectural "Whys" (savwiki){new_entry}'
    )

    with open(target_path, "w") as f:
        f.write(content)

    print(f"Synthesis Receipt: {target_path} updated.")


# Example Trigger:
# process_munch_signal('temp_signal.json')
