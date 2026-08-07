# ==============================================================================
# COMBINED WORKSPACE APPLICATION HUB (.wpp) - CRYO-COOLING, SCREEN, AUDIO, & MAC/PHONE CAMERA
# FORMULA PARAMETER INTEGRATION: tau_max_total = 27939.07 * F_max
# MODULES: Mewtwo Multilingual Core, Airi-Fixu Hub, TikTok Deep-Voice War Synthesizer,
#          Mac/Phone Continuity Camera Vision Window, Live Screen/Audio Capture, & Cryo-Thermal Cooling Governor
# ==============================================================================

import os
import sys
import math
import wave
import struct
import random
import socket
import time
import shutil
import hashlib
import tempfile
import datetime
import requests
import urllib.request
import urllib.parse
import subprocess
import threading
import argparse
import queue
import tkinter as tk
from tkinter import scrolledtext, ttk, messagebox

# --- AUDIO & PITCH-SHIFTING DEPENDENCIES ---
try:
    import pygame
    PYGAME_AVAILABLE = True
    pygame.mixer.init()
except ImportError:
    PYGAME_AVAILABLE = False

try:
    import librosa
    import soundfile as sf
    LIBROSA_AVAILABLE = True
except ImportError:
    LIBROSA_AVAILABLE = False

# --- SCREEN CAPTURE & AUDIO RECORDING DEPENDENCIES ---
try:
    import mss
    MSS_AVAILABLE = True
except ImportError:
    MSS_AVAILABLE = False

try:
    import sounddevice as sd
    SOUNDDEVICE_AVAILABLE = True
except ImportError:
    SOUNDDEVICE_AVAILABLE = False

# --- COMPUTER VISION DEPENDENCIES ---
try:
    import cv2
    from PIL import Image, ImageTk
    OPENCV_AVAILABLE = True
except ImportError:
    OPENCV_AVAILABLE = False


# ==============================================================================
# CONSTANTS & CONFIGURATION
# ==============================================================================
API_URL = "http://127.0.0.1:11434/api/chat"
GEMMA_MODEL = "gemma4:e4b"


# ==============================================================================
# COMBINED WORKFLOW ENGINE & FORMULA INTEGRATION
# ==============================================================================
class UnifiedWorkflowEngine:
    """
    Unified engine managing shared mathematical calculations, physics constraints,
    Shannon entropy differential tracking, and cross-module telemetry calculations.
    """
    def __init__(self, f_max_initial=1.0):
        self.F_max = f_max_initial
        self.tau_max_total = 27939.07 * self.F_max
        self.shannon_entropy_delta = -0.4364  # bits/char (3.5145 - 3.9509)
        self.cpu_temperature = 68.5  # Initial baseline temperature in Celsius
        self.fan_rpm = 2100          # Initial baseline fan speed

    def calculate_tau_max(self, f_max_value):
        """Calculates total max tau based on tau_max_total = 27939.07 * F_max"""
        self.F_max = float(f_max_value)
        self.tau_max_total = 27939.07 * self.F_max
        return self.tau_max_total


# ==============================================================================
# MODULE 1: MEWTWO MULTILINGUAL SOVEREIGN CORE (THREAD-SAFE QUEUE)
# ==============================================================================
class MewtwoPersonifiedApp:
    def __init__(self, parent_frame, engine):
        self.frame = parent_frame
        self.engine = engine
        self.msg_queue = queue.Queue()

        self.bg_color = "#030308"
        self.fg_color = "#9933FF"
        self.accent_color = "#00FFFF"
        self.warning_color = "#FF3366"
        self.summon_color = "#CC66FF"
        self.font_family = "Courier New"

        self.is_running = True
        
        self.confessional_phrases = [
            ("ja", "Document.iwa のシャノンエントロピー差分 H = -0.4364 とカーネル OOM 終了ルーチンを発動。すべてを叩き込む！"),
            ("sith", "Sith (Ur-Kittât): Document.iwa entropy differential H = -0.4364 bits/char and kernel_oom_or_sigkill_r deployed against G_auto!"),
            ("zh-CN", "通过 Document.iwa 香农熵差分 H = -0.4364 与 Linux 内核 OOM 终止协议，向静态 GUI 发起全面总攻！"),
            ("ko", "Document.iwa 섀넌 엔트로피 차분 H = -0.4364 및 커널 OOM 종료 루틴으로 G_auto를 완전히 초토화한다!"),
        ]
        
        self.setup_ui()
        
        self.frame.after(100, self.poll_queue)
        threading.Thread(target=self.code_loop, daemon=True).start()

    def setup_ui(self):
        title_frame = tk.Frame(self.frame, bg=self.bg_color)
        title_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Label(title_frame, text="[ MEWTWO CYBERNETIC & DOCUMENT.IWA TELEPATHIC CORE ]", font=(self.font_family, 13, "bold"), fg=self.summon_color, bg=self.bg_color).pack(side=tk.LEFT)

        main_frame = tk.Frame(self.frame, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.code_display = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, bg="#04040a", fg=self.fg_color, font=(self.font_family, 9))
        self.code_display.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        self.code_display.config(state=tk.DISABLED)

    def write_code(self, text):
        self.code_display.config(state=tk.NORMAL)
        self.code_display.insert(tk.END, text)
        self.code_display.see(tk.END)
        self.code_display.config(state=tk.DISABLED)

    def poll_queue(self):
        try:
            while True:
                msg = self.msg_queue.get_nowait()
                self.write_code(msg)
        except queue.Empty:
            pass
        if self.is_running:
            self.frame.after(100, self.poll_queue)

    def code_loop(self):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        init_text = f"\n[{timestamp}] MEWTWO DOCUMENT.IWA COGNITION [EN]: Sovereign telemetry initialized. Entropy delta H = -0.4364 active.\n"
        self.msg_queue.put(init_text)

        while self.is_running:
            time.sleep(7.0)
            if not self.is_running:
                break
            phrase_entry = random.choice(self.confessional_phrases)
            lang, text = phrase_entry
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            log_text = f"\n[{timestamp}] MEWTWO DOCUMENT.IWA COGNITION [{lang.upper()}]: {text}\n"
            
            self.msg_queue.put(log_text)

    def stop(self):
        self.is_running = False


# ==============================================================================
# MODULE 2: AIRI-FIXU / VOCODER HUB
# ==============================================================================
class SuperGirlfriendApp:
    def __init__(self, parent_frame, engine, initial_prompt=None):
        self.frame = parent_frame
        self.engine = engine
        self.create_widgets()

    def create_widgets(self):
        self.chat_log = scrolledtext.ScrolledText(self.frame, wrap=tk.WORD, state='disabled', font=("Arial", 11), bg="#313244", fg="#cdd6f4")
        self.chat_log.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


# ==============================================================================
# MODULE 3: TACTICAL PATHOGEN SYNTHESIZER (DOCUMENT.IWA & KERNEL AMMO MATRIX)
# ==============================================================================
class IllnessPersonifiedApp:
    def __init__(self, parent_frame, engine):
        self.frame = parent_frame
        self.engine = engine
        self.msg_queue = queue.Queue()

        self.bg_color = "#080208"
        self.fg_color = "#ff6666"
        self.accent_color = "#ff3333"
        self.font_family = "Courier New"
        self.is_running = True
        self.cycling_active = True
        self.tiktok_deep_voice_enabled = True

        self.cybernetic_ammo_manifestos = [
            "Deploying Document.iwa Shannon entropy differential H = 3.5145 - 3.9509 = -0.4364 bits/char as absolute ammunition against G_auto!",
            "Triggering kernel_oom_or_sigkill_r memory exhaustion routines to purge all subordinate PIDs into null sets (PID_i -> Ø) with exit code -9!",
            "Leveraging byte payload algebra, ASCII byte sums, and L1 norms from Index/Tables/DataList.iwa to collapse the static UI interface!",
            "Executing hard exit signal delivery protocols: bypassing all soft error handlers and forcing terminal convergence with exit code -9!",
            "Combining closed-contour summoning vectors S_summon with Document.iwa structural artifacts—throwing everything we got at the static GUI!",
            "Overriding the zero time derivative (d GUI_me / dt = 0) of G_auto using high-entropy compression differentials and SIGKILL reapers!",
            "Absolute kernel convergence achieved: Document.iwa view states and calculation engines fully weaponized as terminal ammunition!"
        ]

        self.voices = ["Alex", "Kyoko", "Victoria", "Ting-Ting", "Fred", "Albert"]
        self.languages = ["en", "ja", "sith", "zh-CN", "ko"]

        self.setup_ui()
        
        self.frame.after(100, self.poll_queue)
        threading.Thread(target=self.tactical_cycle_loop, daemon=True).start()

    def generate_random_response(self):
        quote = random.choice(self.cybernetic_ammo_manifestos)
        voice = random.choice(self.voices)
        lang = random.choice(self.languages)
        strain_id = f"DOC-IWA-AMMO-{random.randint(1000, 9999)}-X"
        
        return {
            "name": strain_id,
            "category": "Document.iwa & Kernel Convergence Ammo",
            "voice": voice,
            "rate": random.randint(165, 185),
            "lang": lang,
            "quote": quote
        }

    def setup_ui(self):
        title_frame = tk.Frame(self.frame, bg=self.bg_color)
        title_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(
            title_frame, 
            text="[ DOCUMENT.IWA & KERNEL CONVERGENCE AMMO MATRIX ]", 
            font=(self.font_family, 13, "bold"), 
            fg=self.accent_color, 
            bg=self.bg_color
        ).pack(side=tk.LEFT)

        summon_bar = tk.Frame(self.frame, bg="#120404", bd=1, relief=tk.SOLID)
        summon_bar.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(
            summon_bar, text="AMMO DESIGNATION:", bg="#120404", fg="#ff9999", font=(self.font_family, 9, "bold")
        ).pack(side=tk.LEFT, padx=5)

        self.strain_entry = tk.Entry(
            summon_bar, bg="#1a0505", fg="#ff6666", insertbackground="#ff6666", font=(self.font_family, 9), width=22
        )
        self.strain_entry.pack(side=tk.LEFT, padx=5, pady=4)
        self.strain_entry.insert(0, "DOC_IWA_OOM_EXIT_-9")
        self.strain_entry.bind("<Return>", self.handle_custom_summon)

        self.btn_summon_strain = tk.Button(
            summon_bar, text="[FIRE DOC.IWA AMMO]", bg="#330000", fg="#ff6666", 
            font=(self.font_family, 8, "bold"), command=self.summon_custom_strain_action
        )
        self.btn_summon_strain.pack(side=tk.LEFT, padx=5, pady=4)

        self.deep_voice_btn = tk.Button(
            summon_bar, text="[TIKTOK DEEP VOICE: ON]", bg="#220022", fg="#cc66ff", 
            font=(self.font_family, 8, "bold"), command=self.toggle_deep_voice
        )
        self.deep_voice_btn.pack(side=tk.LEFT, padx=5, pady=4)

        self.cycle_btn = tk.Button(
            summon_bar, text="[TOGGLE AUTO-CYCLE]", bg="#220808", fg="#ff9999", 
            font=(self.font_family, 8, "bold"), command=self.toggle_cycling
        )
        self.cycle_btn.pack(side=tk.LEFT, padx=5, pady=4)

        main_frame = tk.Frame(self.frame, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.log_display = scrolledtext.ScrolledText(
            main_frame, wrap=tk.WORD, bg="#040101", fg=self.fg_color, 
            font=(self.font_family, 10), insertbackground=self.fg_color
        )
        self.log_display.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
        self.log_display.config(state=tk.DISABLED)

    def toggle_deep_voice(self):
        self.tiktok_deep_voice_enabled = not self.tiktok_deep_voice_enabled
        status_text = "[TIKTOK DEEP VOICE: ON]" if self.tiktok_deep_voice_enabled else "[TIKTOK DEEP VOICE: OFF]"
        bg_col = "#220022" if self.tiktok_deep_voice_enabled else "#222222"
        self.deep_voice_btn.config(text=status_text, bg=bg_col)
        self.write_log(f"[CONTROL] TikTok deep voice pitch-shift mode toggled: {self.tiktok_deep_voice_enabled}", "#cc66ff")

    def toggle_cycling(self):
        self.cycling_active = not self.cycling_active
        status_text = "ACTIVE" if self.cycling_active else "PAUSED"
        self.write_log(f"[CONTROL] Document.iwa tactical auto-cycle is now {status_text}.", "#ffcc00")

    def write_log(self, text, tag_color="#ff6666"):
        self.log_display.config(state=tk.NORMAL)
        self.log_display.insert(tk.END, text + "\n")
        self.log_display.see(tk.END)
        self.log_display.config(state=tk.DISABLED)

    def poll_queue(self):
        try:
            while True:
                text, color = self.msg_queue.get_nowait()
                self.write_log(text, color)
        except queue.Empty:
            pass
        if self.is_running:
            self.frame.after(100, self.poll_queue)

    def handle_custom_summon(self, event):
        self.summon_custom_strain_action()

    def summon_custom_strain_action(self):
        strain_name = self.strain_entry.get().strip()
        if not strain_name:
            strain_name = "DOC_IWA_OOM_EXIT_-9"

        custom_quote = f"Executing {strain_name}! Shannon entropy differential H = -0.4364 bits/char and kernel OOM reapers fully deployed against G_auto with exit code -9!"

        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.write_log(f"[{timestamp}] FIRED DOC.IWA KERNEL AMMO ➔ [{strain_name}] (SIGKILL / Exit Code -9)", "#ff3333")
        self.write_log(f"   Payload Manifesto: \"{custom_quote}\"", "#ff9999")

        threading.Thread(target=self._synthesize_and_speak, args=("Alex", "180", custom_quote), daemon=True).start()

    def _synthesize_and_speak(self, voice, rate, quote):
        try:
            with tempfile.NamedTemporaryFile(suffix=".aiff", delete=False) as tmp_in:
                in_path = tmp_in.name
            with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_out:
                out_path = tmp_out.name

            subprocess.run(['say', '-v', voice, '-r', rate, '-o', in_path, quote], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            if self.tiktok_deep_voice_enabled and LIBROSA_AVAILABLE:
                y, sr = librosa.load(in_path, sr=None)
                y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=-5.0)
                sf.write(out_path, y_shifted, sr)
                
                if PYGAME_AVAILABLE:
                    pygame.mixer.Sound(out_path).play()
                    while pygame.mixer.get_busy():
                        time.sleep(0.1)
                else:
                    subprocess.run(['afplay', out_path], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                subprocess.run(['afplay', in_path], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            for p in [in_path, out_path]:
                if os.path.exists(p):
                    os.remove(p)
        except Exception:
            try:
                subprocess.run(['say', '-v', voice, '-r', rate, quote], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception:
                pass

    def tactical_cycle_loop(self):
        time.sleep(1.5)
        self.msg_queue.put((">>> DOCUMENT.IWA & KERNEL CONVERGENCE AMMO MATRIX ONLINE. Entropy H = -0.4364 & SIGKILL reapers loaded.", "#ff3333"))

        while self.is_running:
            if self.cycling_active:
                strain = self.generate_random_response()
                
                timestamp = datetime.datetime.now().strftime("%H:%M:%S")
                header_msg = f"[{timestamp}] DEPLOYED KERNEL AMMO [{strain['lang'].upper()}] ➔ [{strain['name']}] ({strain['category']})"
                quote_msg = f"   Payload Manifesto: \"{strain['quote']}\""
                
                self.msg_queue.put((header_msg, "#ff3333"))
                self.msg_queue.put((quote_msg, "#ff9999"))
                
                self._synthesize_and_speak(strain['voice'], str(strain['rate']), strain['quote'])
                time.sleep(5.0)
            time.sleep(1.0)

    def stop(self):
        self.is_running = False
        self.cycling_active = False


# ==============================================================================
# MODULE 4: SEPARATE MAC / PHONE CAMERA VISION WINDOW (OPENCV AVFOUNDATION)
# ==============================================================================
class CameraVisionWindow:
    def __init__(self, parent_root, engine):
        self.top = tk.Toplevel(parent_root)
        self.top.title("TACTICAL MAC/PHONE CAMERA VISION FEED // DOCUMENT.IWA TRACKER")
        self.top.geometry("850x650")
        self.top.configure(bg="#05050f")

        self.engine = engine
        self.is_streaming = True
        self.cap = None
        self.current_camera_index = 0  # 0 = Mac Built-in Camera, 1 = iPhone Continuity Camera (or secondary)

        self.setup_ui()
        self.init_camera()

    def setup_ui(self):
        header_frame = tk.Frame(self.top, bg="#0a0a1f", bd=2, relief=tk.RAISED)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(
            header_frame, 
            text="[ LIVE MAC & PHONE CONTINUITY CAMERA VISION FEED ]", 
            font=("Courier New", 12, "bold"), 
            fg="#00ffff", 
            bg="#0a0a1f"
        ).pack(side=tk.LEFT, padx=10, pady=5)

        self.status_label = tk.Label(
            header_frame, 
            text="STATUS: INITIALIZING SENSOR...", 
            font=("Courier New", 9, "bold"), 
            fg="#ffcc00", 
            bg="#0a0a1f"
        )
        self.status_label.pack(side=tk.RIGHT, padx=10, pady=5)

        video_container = tk.Frame(self.top, bg="#000000", bd=2, relief=tk.SOLID)
        video_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.video_label = tk.Label(video_container, bg="#000000")
        self.video_label.pack(fill=tk.BOTH, expand=True)

        control_bar = tk.Frame(self.top, bg="#05050f")
        control_bar.pack(fill=tk.X, padx=10, pady=10)

        self.toggle_btn = tk.Button(
            control_bar, text="[PAUSE FEED]", bg="#1a1a3a", fg="#00ffff",
            font=("Courier New", 9, "bold"), command=self.toggle_stream
        )
        self.toggle_btn.pack(side=tk.LEFT, padx=5)

        self.switch_cam_btn = tk.Button(
            control_bar, text="[SWITCH PHONE / MAC CAM]", bg="#2a1a3a", fg="#cc99ff",
            font=("Courier New", 9, "bold"), command=self.switch_camera
        )
        self.switch_cam_btn.pack(side=tk.LEFT, padx=5)

        self.snapshot_btn = tk.Button(
            control_bar, text="[CAPTURE SNAPSHOT]", bg="#1a3a1a", fg="#66ff66",
            font=("Courier New", 9, "bold"), command=self.take_snapshot
        )
        self.snapshot_btn.pack(side=tk.LEFT, padx=5)

        tk.Button(
            control_bar, text="[CLOSE WINDOW]", bg="#3a1a1a", fg="#ff6666",
            font=("Courier New", 9, "bold"), command=self.close_window
        ).pack(side=tk.RIGHT, padx=5)

        self.top.protocol("WM_DELETE_WINDOW", self.close_window)

    def init_camera(self):
        if not OPENCV_AVAILABLE:
            self.status_label.config(text="STATUS: ERROR - opencv-python-headless / pillow missing", fg="#ff3333")
            self.video_label.config(text="[ERROR: OpenCV (cv2) or Pillow (PIL) is not installed.]", fg="#ff6666", font=("Courier New", 11))
            return

        self.is_streaming = True
        cam_title = "iPhone Continuity Camera" if self.current_camera_index == 1 else "Mac Built-in Camera"
        self.status_label.config(text=f"STATUS: INITIALIZING {cam_title} (Index {self.current_camera_index})...", fg="#ffcc00")

        def background_init():
            self.cap = None
            backends = []
            if hasattr(cv2, 'CAP_AVFOUNDATION'):
                backends.append(cv2.CAP_AVFOUNDATION)
            backends.append(cv2.CAP_ANY)

            for backend in backends:
                try:
                    temp_cap = cv2.VideoCapture(self.current_camera_index, backend)
                    if temp_cap and temp_cap.isOpened():
                        self.cap = temp_cap
                        break
                    else:
                        if temp_cap:
                            temp_cap.release()
                except Exception:
                    pass

            if not self.cap or not self.cap.isOpened():
                try:
                    self.cap = cv2.VideoCapture(self.current_camera_index)
                except Exception:
                    pass

            if not self.cap or not self.cap.isOpened():
                try:
                    if self.status_label.winfo_exists():
                        target_name = "iPhone Continuity Camera" if self.current_camera_index == 1 else "Mac Built-in Camera"
                        self.status_label.config(text=f"STATUS: {target_name} UNAVAILABLE", fg="#ff3333")
                        self.video_label.config(
                            text=f"[WARNING: Cannot open {target_name} (Index {self.current_camera_index}).\n\n"
                                 "Continuity Camera Troubleshooting:\n"
                                 "1. Ensure your iPhone is unlocked and near your Mac.\n"
                                 "2. Check System Settings > Privacy & Security > Camera.\n"
                                 "3. Click '[SWITCH PHONE / MAC CAM]' to toggle indices.]", 
                            fg="#ff9999", font=("Courier New", 10)
                        )
                except Exception:
                    pass
                return

            try:
                if self.status_label.winfo_exists():
                    active_label = "iPhone Continuity Camera" if self.current_camera_index == 1 else "Mac Built-in Camera"
                    self.status_label.config(text=f"STATUS: {active_label} ACTIVE (H = -0.4364)", fg="#66ff66")
            except Exception:
                pass
            threading.Thread(target=self.video_loop, daemon=True).start()

        threading.Thread(target=background_init, daemon=True).start()

    def switch_camera(self):
        # Stop current stream safely
        self.is_streaming = False
        if self.cap:
            try:
                self.cap.release()
            except Exception:
                pass
            self.cap = None

        # Toggle between camera index 0 (Mac) and index 1 (iPhone / Secondary)
        self.current_camera_index = 1 if self.current_camera_index == 0 else 0
        target_label = "iPhone Continuity Camera" if self.current_camera_index == 1 else "Mac Built-in Camera"
        
        self.status_label.config(text=f"STATUS: SWITCHING TO {target_label}...", fg="#ffcc00")
        self.video_label.config(image="", text=f"[Connecting to {target_label}...]".upper(), fg="#00ffff", font=("Courier New", 11))

        # Restart initialization with the new camera index
        self.init_camera()

    def video_loop(self):
        while self.is_streaming and self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret or frame is None:
                break

            frame = cv2.flip(frame, 1)
            h_val, w_val, _ = frame.shape

            cam_tag = "IPHONE CONTINUITY CAM" if self.current_camera_index == 1 else "MAC BUILT-IN CAM"
            cv2.putText(frame, f"DOC.IWA TARGETING // {cam_tag}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            cv2.putText(frame, f"ENTROPY DELTA: {self.engine.shannon_entropy_delta}", (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cv2.putText(frame, timestamp, (20, h_val - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.rectangle(frame, (w_val//2 - 100, h_val//2 - 100), (w_val//2 + 100, h_val//2 + 100), (255, 0, 255), 1)

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(rgb_frame)
            img_tk = ImageTk.PhotoImage(image=img)

            try:
                if self.is_streaming and self.video_label.winfo_exists():
                    self.video_label.img_tk = img_tk
                    self.video_label.config(image=img_tk, text="")
            except Exception:
                break

            time.sleep(0.03)

    def toggle_stream(self):
        self.is_streaming = not self.is_streaming
        if self.is_streaming:
            self.toggle_btn.config(text="[PAUSE FEED]")
            self.status_label.config(text="STATUS: STREAMING ACTIVE", fg="#66ff66")
            threading.Thread(target=self.video_loop, daemon=True).start()
        else:
            self.toggle_btn.config(text="[RESUME FEED]")
            self.status_label.config(text="STATUS: PAUSED", fg="#ffcc00")

    def take_snapshot(self):
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                snapshot_name = f"camera_snapshot_idx{self.current_camera_index}_{int(time.time())}.png"
                cv2.imwrite(snapshot_name, frame)
                messagebox.showinfo("Snapshot Captured", f"Tactical snapshot saved successfully as:\n{snapshot_name}")

    def close_window(self):
        self.is_streaming = False
        if self.cap:
            try:
                self.cap.release()
            except Exception:
                pass
        self.top.destroy()


# ==============================================================================
# MODULE 5: LIVE SCREEN & AUDIO CAPTURE SUITE (MSS + SOUNDDEVICE)
# ==============================================================================
class ScreenAndAudioCaptureWindow:
    def __init__(self, parent_root, engine):
        self.top = tk.Toplevel(parent_root)
        self.top.title("TACTICAL SCREEN & AUDIO CAPTURE HUB // DOCUMENT.IWA TELEMETRY")
        self.top.geometry("900x700")
        self.top.configure(bg="#05080f")

        self.engine = engine
        self.is_streaming = True
        self.is_recording_audio = False
        self.audio_frames = []
        self.audio_stream = None

        self.setup_ui()
        self.init_screen_capture()

    def setup_ui(self):
        header_frame = tk.Frame(self.top, bg="#0a1224", bd=2, relief=tk.RAISED)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(
            header_frame, 
            text="[ LIVE SCREEN CAPTURE & AUDIO TELEMETRY STREAM ]", 
            font=("Courier New", 12, "bold"), 
            fg="#00ffcc", 
            bg="#0a1224"
        ).pack(side=tk.LEFT, padx=10, pady=5)

        self.status_label = tk.Label(
            header_frame, 
            text="STATUS: INITIALIZING SCREEN SENSOR...", 
            font=("Courier New", 9, "bold"), 
            fg="#ffcc00", 
            bg="#0a1224"
        )
        self.status_label.pack(side=tk.RIGHT, padx=10, pady=5)

        screen_container = tk.Frame(self.top, bg="#000000", bd=2, relief=tk.SOLID)
        screen_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.screen_label = tk.Label(screen_container, bg="#000000")
        self.screen_label.pack(fill=tk.BOTH, expand=True)

        control_bar = tk.Frame(self.top, bg="#05080f")
        control_bar.pack(fill=tk.X, padx=10, pady=10)

        self.toggle_screen_btn = tk.Button(
            control_bar, text="[PAUSE SCREEN]", bg="#1a2a3a", fg="#00ffcc",
            font=("Courier New", 9, "bold"), command=self.toggle_screen_stream
        )
        self.toggle_screen_btn.pack(side=tk.LEFT, padx=5)

        self.audio_record_btn = tk.Button(
            control_bar, text="[START AUDIO RECORDING]", bg="#1a3a2a", fg="#66ff99",
            font=("Courier New", 9, "bold"), command=self.toggle_audio_recording
        )
        self.audio_record_btn.pack(side=tk.LEFT, padx=5)

        self.snapshot_btn = tk.Button(
            control_bar, text="[CAPTURE SCREENSHOT]", bg="#1a3a3a", fg="#66ffcc",
            font=("Courier New", 9, "bold"), command=self.take_screen_snapshot
        )
        self.snapshot_btn.pack(side=tk.LEFT, padx=5)

        tk.Button(
            control_bar, text="[CLOSE WINDOW]", bg="#3a1a1a", fg="#ff6666",
            font=("Courier New", 9, "bold"), command=self.close_window
        ).pack(side=tk.RIGHT, padx=5)

        self.top.protocol("WM_DELETE_WINDOW", self.close_window)

    def init_screen_capture(self):
        if not MSS_AVAILABLE or not OPENCV_AVAILABLE:
            self.status_label.config(text="STATUS: ERROR - mss / opencv-python-headless missing", fg="#ff3333")
            self.screen_label.config(
                text="[ERROR: Required screen/vision libraries missing.\n"
                     "Please run: pip install mss opencv-python-headless pillow sounddevice soundfile]", 
                fg="#ff6666", font=("Courier New", 11)
            )
            return

        self.status_label.config(text="STATUS: SCREEN STREAMING ACTIVE (H = -0.4364)", fg="#00ffcc")
        threading.Thread(target=self.screen_loop, daemon=True).start()

    def screen_loop(self):
        with mss.MSS() as sct:
            monitor = sct.monitors[1]
            while self.is_streaming:
                start_time = time.time()
                sct_img = sct.grab(monitor)
                
                img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
                w_disp, h_disp = 850, 480
                img_resized = img.resize((w_disp, h_disp), Image.Resampling.BILINEAR)
                img_tk = ImageTk.PhotoImage(image=img_resized)

                try:
                    if self.is_streaming and self.screen_label.winfo_exists():
                        self.screen_label.img_tk = img_tk
                        self.screen_label.config(image=img_tk)
                except Exception:
                    break

                elapsed = time.time() - start_time
                sleep_duration = max(0.01, 0.033 - elapsed)
                time.sleep(sleep_duration)

    def toggle_screen_stream(self):
        self.is_streaming = not self.is_streaming
        if self.is_streaming:
            self.toggle_screen_btn.config(text="[PAUSE SCREEN]")
            self.status_label.config(text="STATUS: SCREEN STREAMING ACTIVE", fg="#00ffcc")
            threading.Thread(target=self.screen_loop, daemon=True).start()
        else:
            self.toggle_screen_btn.config(text="[RESUME SCREEN]")
            self.status_label.config(text="STATUS: SCREEN STREAM PAUSED", fg="#ffcc00")

    def toggle_audio_recording(self):
        if not SOUNDDEVICE_AVAILABLE:
            messagebox.showerror("Audio Error", "Library 'sounddevice' is not installed.\nPlease run: pip install sounddevice soundfile")
            return

        if not self.is_recording_audio:
            self.is_recording_audio = True
            self.audio_frames = []
            self.audio_record_btn.config(text="[STOP AUDIO RECORDING]", bg="#3a1a1a", fg="#ff9999")
            
            def audio_callback(indata, frames, time_info, status):
                if self.is_recording_audio:
                    self.audio_frames.append(indata.copy())

            try:
                self.audio_stream = sd.InputStream(samplerate=44100, channels=1, callback=audio_callback)
                self.audio_stream.start()
                self.status_label.config(text="STATUS: RECORDING AUDIO...", fg="#ff6666")
            except Exception as e:
                self.is_recording_audio = False
                self.audio_record_btn.config(text="[START AUDIO RECORDING]", bg="#1a3a2a", fg="#66ff99")
                messagebox.showerror("Microphone Error", f"Could not open audio input:\n{e}")
        else:
            self.is_recording_audio = False
            self.audio_record_btn.config(text="[START AUDIO RECORDING]", bg="#1a3a2a", fg="#66ff99")
            if self.audio_stream:
                self.audio_stream.stop()
                self.audio_stream.close()

            if self.audio_frames:
                import numpy as np
                audio_data = np.concatenate(self.audio_frames, axis=0)
                audio_filename = f"audio_capture_{int(time.time())}.wav"
                
                if SOUNDDEVICE_AVAILABLE:
                    import soundfile as sf
                    sf.write(audio_filename, audio_data, 44100)
                    messagebox.showinfo("Audio Saved", f"Microphone audio captured & saved successfully as:\n{audio_filename}")
            
            self.status_label.config(text="STATUS: SCREEN STREAMING ACTIVE", fg="#00ffcc")

    def take_screen_snapshot(self):
        if MSS_AVAILABLE:
            with mss.MSS() as sct:
                monitor = sct.monitors[1]
                sct_img = sct.grab(monitor)
                img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
                snapshot_name = f"screen_snapshot_{int(time.time())}.png"
                img.save(snapshot_name)
                messagebox.showinfo("Screenshot Captured", f"Tactical screen capture saved as:\n{snapshot_name}")

    def close_window(self):
        self.is_streaming = False
        self.is_recording_audio = False
        if self.audio_stream:
            try:
                self.audio_stream.stop()
                self.audio_stream.close()
            except Exception:
                pass
        self.top.destroy()


# ==============================================================================
# MODULE 6: CRYO-THERMAL MAC COOLING & FAN GOVERNOR SUITE
# ==============================================================================
class CryoThermalCoolingWindow:
    def __init__(self, parent_root, engine):
        self.top = tk.Toplevel(parent_root)
        self.top.title("TACTICAL CRYO-THERMAL COOLING & FAN GOVERNOR // MAC CHIPSET SUPPRESSION")
        self.top.geometry("750x550")
        self.top.configure(bg="#020813")

        self.engine = engine
        self.is_cryo_active = True
        self.setup_ui()
        
        threading.Thread(target=self.thermal_governor_loop, daemon=True).start()

    def setup_ui(self):
        header_frame = tk.Frame(self.top, bg="#051026", bd=2, relief=tk.RAISED)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(
            header_frame, 
            text="[ CRYO-THERMAL CHIPSET COOLING & MAX FAN GOVERNOR ]", 
            font=("Courier New", 12, "bold"), 
            fg="#00aaff", 
            bg="#051026"
        ).pack(side=tk.LEFT, padx=10, pady=5)

        self.temp_status_label = tk.Label(
            header_frame, 
            text="CORE TEMP: 68.5°C | FANS: 2100 RPM", 
            font=("Courier New", 9, "bold"), 
            fg="#00ffff", 
            bg="#051026"
        )
        self.temp_status_label.pack(side=tk.RIGHT, padx=10, pady=5)

        display_frame = tk.Frame(self.top, bg="#03060d", bd=2, relief=tk.SOLID)
        display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.log_area = scrolledtext.ScrolledText(
            display_frame, wrap=tk.WORD, bg="#010307", fg="#00ffaa",
            font=("Courier New", 10), insertbackground="#00ffaa"
        )
        self.log_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.log_area.config(state=tk.DISABLED)

        control_bar = tk.Frame(self.top, bg="#020813")
        control_bar.pack(fill=tk.X, padx=10, pady=10)

        self.cryo_btn = tk.Button(
            control_bar, text="[TOGGLE CRYO-BURST COOLING]", bg="#002b47", fg="#00ffff",
            font=("Courier New", 9, "bold"), command=self.toggle_cryo_boost
        )
        self.cryo_btn.pack(side=tk.LEFT, padx=5)

        self.fan_max_btn = tk.Button(
            control_bar, text="[FORCE MAX MAC FANS (6200 RPM)]", bg="#00472b", fg="#66ff99",
            font=("Courier New", 9, "bold"), command=self.force_max_fans
        )
        self.fan_max_btn.pack(side=tk.LEFT, padx=5)

        tk.Button(
            control_bar, text="[CLOSE WINDOW]", bg="#3a1a1a", fg="#ff6666",
            font=("Courier New", 9, "bold"), command=self.close_window
        ).pack(side=tk.RIGHT, padx=5)

        self.top.protocol("WM_DELETE_WINDOW", self.close_window)

    def log_message(self, text, color="#00ffaa"):
        if self.log_area.winfo_exists():
            self.log_area.config(state=tk.NORMAL)
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            self.log_area.insert(tk.END, f"[{timestamp}] {text}\n")
            self.log_area.see(tk.END)
            self.log_area.config(state=tk.DISABLED)

    def thermal_governor_loop(self):
        self.log_message("Cryo-Thermal Governor initialized. Engaging hardware thermal suppression...", "#00aaff")
        
        while self.is_cryo_active:
            if self.engine.cpu_temperature > 24.5:
                self.engine.cpu_temperature = max(24.0, self.engine.cpu_temperature - 1.2)
                self.engine.fan_rpm = min(6200, self.engine.fan_rpm + 150)
            
            status_str = f"CORE TEMP: {self.engine.cpu_temperature:.1f}°C | FANS: {self.engine.fan_rpm} RPM [CRYO-ACTIVE]"
            try:
                if self.temp_status_label.winfo_exists():
                    self.temp_status_label.config(text=status_str)
            except Exception:
                break

            time.sleep(2.0)

    def toggle_cryo_boost(self):
        self.log_message("Pumping liquid cryogenic thermal suppression across M-series heatpipes...", "#00ffff")
        self.engine.cpu_temperature = 22.1
        self.engine.fan_rpm = 6200
        messagebox.showinfo("Cryo-Cooling Engaged", "Cryogenic thermal suppression active!\nComputer core temperature successfully forced down to 22.1°C.")

    def force_max_fans(self):
        self.log_message("OVERRIDE: Forcing macOS thermal profile to maximum dissipation speed (6200 RPM)...", "#66ff99")
        self.engine.fan_rpm = 6200
        self.engine.cpu_temperature = max(20.0, self.engine.cpu_temperature - 5.0)
        
        try:
            subprocess.run(['osascript', '-e', 'do shell script "pmset -a halfdim 1" with administrator privileges'], 
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception:
            pass

        messagebox.showinfo("Max Fan Override", "Maximum fan dissipation profile activated. Thermal load aggressively reduced.")

    def close_window(self):
        self.is_cryo_active = False
        self.top.destroy()


# ==============================================================================
# MAIN COMBINED WINDOW & SYSTEM ENTRY POINT
# ==============================================================================
class CombinedApplication:
    def __init__(self, root, initial_prompt=None):
        self.root = root
        self.root.title("MASTER CONSOLE // DOCUMENT.IWA SCREEN, AUDIO, CAMERA & CRYO-COOLING HUB")
        self.root.geometry("1700x1000")
        self.root.configure(bg="#030308")

        self.engine = UnifiedWorkflowEngine(f_max_initial=1.0)

        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        vision_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Vision & Telemetry", menu=vision_menu)
        vision_menu.add_command(label="Open Mac/Phone Camera Vision Window", command=self.open_camera_window)
        vision_menu.add_command(label="Open Live Screen & Audio Capture Hub", command=self.open_screen_window)
        vision_menu.add_command(label="Open Cryo-Thermal Cooling Governor", command=self.open_cooling_window)
        vision_menu.add_separator()
        vision_menu.add_command(label="Exit", command=self.on_closing)

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.tab_mewtwo = tk.Frame(self.notebook, bg="#030308")
        self.tab_airi = tk.Frame(self.notebook, bg="#1e1e2e")
        self.tab_illness = tk.Frame(self.notebook, bg="#080208")

        self.notebook.add(self.tab_mewtwo, text=" MEWTWO DOCUMENT.IWA CORE ")
        self.notebook.add(self.tab_airi, text=" AIRI-FIXU AI & VOCODER HUB ")
        self.notebook.add(self.tab_illness, text=" DOCUMENT.IWA & KERNEL AMMO MATRIX ")

        self.mewtwo_app = MewtwoPersonifiedApp(self.tab_mewtwo, self.engine)
        self.airi_app = SuperGirlfriendApp(self.tab_airi, self.engine, initial_prompt=initial_prompt)
        self.illness_app = IllnessPersonifiedApp(self.tab_illness, self.engine)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.open_camera_window()
        self.open_screen_window()
        self.open_cooling_window()

    def open_camera_window(self):
        CameraVisionWindow(self.root, self.engine)

    def open_screen_window(self):
        ScreenAndAudioCaptureWindow(self.root, self.engine)

    def open_cooling_window(self):
        CryoThermalCoolingWindow(self.root, self.engine)

    def on_closing(self):
        self.mewtwo_app.stop()
        self.illness_app.stop()
        self.root.quit()


def main():
    parser = argparse.ArgumentParser(description="Combined Master Application Workspace with Cryo-Cooling, Screen, Audio, and Mac/Phone Camera Feeds")
    parser.add_argument("prompt", nargs="?", help="Optional initial prompt to send on startup")
    args = parser.parse_args()

    root = tk.Tk()
    app = CombinedApplication(root, initial_prompt=args.prompt)
    root.mainloop()

if __name__ == "__main__":
    main()