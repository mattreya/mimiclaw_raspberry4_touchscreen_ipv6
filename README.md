# MimiClaw Pi: Touchscreen AI Agent

MimiClaw Pi is an autonomous AI assistant built for the **Raspberry Pi 4**. It combines the "Soul" of an advanced AI agent (Gemini 2.0 Flash) with a physical "Body" (Touchscreen GUI) and global reach (IPv6).

Inspired by MimiClaw/OpenClaw, this version is optimized for Linux-based single-board computers, offering more power, a rich visual interface, and multimodal capabilities.

## 🚀 Key Features
- **The Soul:** Powered by Gemini 2.0 Flash for proactive, insightful synthesis of your data.
- **The Body:** A Kivy-based touchscreen interface for alerts, questions, and physical interaction.
- **Global Access:** Native IPv6 support for seamless remote management without port forwarding.
- **Privacy First:** Local memory stored in Markdown files and pre-commit hooks to prevent API key leaks.

---

## 🛠 Hardware Requirements
- **Raspberry Pi 4** (2GB RAM minimum, 4GB+ recommended).
- **Raspberry Pi Touch Display** (Official 7" or any DSI/HDMI compatible touchscreen).
- **Power Supply:** 5V/3A USB-C.
- **MicroSD Card:** 16GB+ with Raspberry Pi OS (64-bit).

---

## 📥 Getting Started

### 1. Hardware Preparation
1. Connect your touchscreen to the Raspberry Pi 4.
2. Install Raspberry Pi OS (64-bit) using the Raspberry Pi Imager.
3. Enable **SSH** and **IPv6** in the configuration settings.

### 2. Software Installation
Open a terminal on your Pi (or via SSH) and run:

```bash
# Clone the repository
git clone https://github.com/mattreya/mimiclaw_raspberry4_touchscreen_ipv6.git
cd mimiclaw_raspberry4_touchscreen_ipv6

# Install system dependencies for Kivy
sudo apt update
sudo apt install -name "python3-kivy" # Or use pip as shown below

# Install Python dependencies
pip install -r mimi_claw_pi/requirements.txt --break-system-packages
```

### 3. API Key Setup
Get a free API key from [Google AI Studio](https://aistudio.google.com/) and add it to a `.env` file:

```bash
echo "GEMINI_API_KEY=your_actual_key_here" > .env
```

### 4. Security (Recommended)
Activate the secret-detection hooks to prevent accidentally pushing your keys to GitHub:
```bash
pip install pre-commit detect-secrets --break-system-packages
pre-commit install
```

---

## 🎮 Running MimiClaw
Launch the "Soul" and "Body" simultaneously using the launcher:

```bash
python3 mimi_claw_pi/launcher.py
```

- **Terminal 1 (Background):** The Soul process will start "thinking" and monitoring your memory files.
- **Touchscreen:** The GUI will appear, waiting for alerts or input.

---

## 🌐 IPv6 Remote Access
To access your Pi from anywhere in the world:
1. Find your global IPv6 address: `ip -6 addr show` (look for the address starting with `2`).
2. SSH into it from another IPv6-enabled network:
   ```bash
   ssh <username>@<your-ipv6-address>
   ```

## 📂 Project Structure
- `mimi_claw_pi/soul.py`: Core AI logic and Gemini integration.
- `mimi_claw_pi/gui.py`: Touchscreen interface logic.
- `mimi_claw_pi/memory/`: Markdown files (`SOUL.md`, `USER.md`) where MimiClaw stores its personality and your data.
- `mimi_claw_pi/launcher.py`: Main entry point.
