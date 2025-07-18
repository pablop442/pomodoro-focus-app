# LoFi Focus App ✨

A modern, desktop-based **Pomodoro Timer with LoFi music** for focused work sessions. Built with Python, `customtkinter`, and powered by `mpv` for streaming.

---

## 🌟 Features

* Pomodoro-style timer (25/5 min cycles)
* Stream curated LoFi music channels
* Dark & Light mode switch
* Neon-themed modern UI

---

## 🔧 Requirements

* Python 3.8+
* [mpv player](https://mpv.io/installation/) (installed & in your system PATH)

---

## 📁 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/YOUR_USERNAME/lofi-focus-app.git
cd lofi-focus-app
```

2. **Create virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Make sure `mpv` is installed and accessible**:

* On macOS: `brew install mpv`
* On Linux: `sudo apt install mpv`
* On Windows:

  * Download `mpv.exe` from [https://mpv.io/installation/](https://mpv.io/installation/)
  * Place it in a folder like `C:\mpv`
  * Add that folder to your Windows PATH

5. **Run the app:**

```bash
python app.py
```

---

## 🔊 LoFi Channels Included

* LoFi Girl
* Chillhop Radio
* Jazz Hop

---

## 🌈 Light & Dark Mode

Toggle theme from the dropdown in the top-right corner of the app.

---

## 🚪 Exit Cleanly

To stop music when exiting:

* Use the `Stop Music` button **before** closing the app, or
* Close the app using the window close button (music stops automatically)

---

## 📅 Upcoming Features

* System tray support
* Custom session length
* User-defined LoFi URLs

---

## 🎓 Learn More

* [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique)
* [LoFi music](https://en.wikipedia.org/wiki/Lo-fi_music)

---

## 🎓 License

[MIT License](LICENSE)

---

## 🚀 Author

Made by pablop442

---

## 📣 Share

Want to share with friends/family?

* Create `.exe` with PyInstaller (see instructions below)
* Or just zip the folder with a README and share the source!
