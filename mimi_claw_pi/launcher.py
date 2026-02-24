import threading
import time
import sys
import os
from mimi_claw_pi.soul import MimiSoul

def run_soul():
    print("[Soul] Starting AI Agent logic...")
    soul = MimiSoul()
    # In a real scenario, this would be a loop listening to Telegram/Sensors
    while True:
        # For now, let's just simulate a "Heartbeat" every 30 seconds
        time.sleep(30)
        # soul.think("What's on my schedule?")

def run_gui():
    print("[Body] Starting Touchscreen Interface...")
    # Import inside function to avoid Kivy window popping up for the Soul thread
    os.environ['KIVY_NO_ARGS'] = '1'
    from mimi_claw_pi.gui import MimiClawApp
    MimiClawApp().run()

if __name__ == "__main__":
    # Start the Soul in a background thread
    soul_thread = threading.Thread(target=run_soul, daemon=True)
    soul_thread.start()

    # Start the GUI in the main thread
    run_gui()
