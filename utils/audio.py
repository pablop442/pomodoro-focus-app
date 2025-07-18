import subprocess
import sys

# --- Internal state ---
_mpv_process = None
LOFI_STREAMS = {
    "LoFi Girl": "https://www.youtube.com/watch?v=jfKfPfyJRdk",
    "Chillhop Radio": "https://www.youtube.com/watch?v=5yx6BWlEVcY",
    "Jazz Hop": "https://www.youtube.com/watch?v=Dx5qFachd3A",
}
_current_stream = None

def get_lofi_streams():
    return list(LOFI_STREAMS.keys())

def get_current_track():
    return _current_stream or ""

def _stop_mpv():
    global _mpv_process
    if _mpv_process:
        print(f"[INFO] Stopping MPV (PID {_mpv_process.pid})")
        try:
            _mpv_process.terminate()
            _mpv_process.wait(timeout=3)  # Wait for it to exit
        except Exception as e:
            print(f"[ERROR] While stopping MPV: {e}")
        finally:
            _mpv_process = None


def play_stream(name):
    global _mpv_process, _current_stream
    if name not in LOFI_STREAMS:
        raise ValueError(f"Unknown stream: {name}")
    _stop_mpv()
    url = LOFI_STREAMS[name]
    ipc_socket = r"\\.\pipe\mpv-pipe"
    cmd = [
        "mpv", "--no-video", "--loop", f"--volume=70", "--msg-level=all=debug",
        "--log-file=mpv_debug.log", f"--input-ipc-server={ipc_socket}", url
    ]
    try:
        print(f"[INFO] Running: {' '.join(cmd)}")
        
        # Added to prevent console window on Windows
        creationflags = 0
        if  sys.platform == "win32":
            creationflags = subprocess.CREATE_NO_WINDOW

        _mpv_process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=creationflags)
        print(f"[INFO] MPV launched with PID {_mpv_process.pid}")
        _current_stream = name
    except Exception as e:
        print(f"[ERROR] Failed to start MPV: {e}")

def stop_stream():
    _stop_mpv()

def cleanup():
    _stop_mpv()
