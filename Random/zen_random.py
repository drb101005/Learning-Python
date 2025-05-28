import speech_recognition as sr
import pyautogui
import webbrowser
import os
import tkinter as tk
from tkinter import ttk
import threading
import time
import datetime
import asyncio
import edge_tts
import subprocess
import platform
from typing import Optional

class VoiceAutomationSystem:
    def __init__(self):
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Configuration
        self.trigger_word = "computer"  # Change to your preferred trigger
        self.active = True  # Start as active by default
        self.listening = False
        self.voice = "en-US-AriaNeural"  # Modern neural voice
        self.browser_path = self.get_chrome_path()  # Get Chrome path automatically
        
        # Command mappings
        self.commands = {
            "open browser": self.open_chrome,
            "open chrome": self.open_chrome,
            "open workplace": self.open_vscode,
            "shutdown": self.system_shutdown,
            "good morning": self.good_morning_response,
            "good evening": self.good_evening_response,
            "good night": self.good_night_response,
            "search": self.web_search,
            "wake up": self.activate_system,
            "sleep": self.deactivate_system,
            "what's the time": self.current_time,
            "open youtube": lambda: self.open_website("youtube.com"),
            "open gmail": lambda: self.open_website("mail.google.com"),
            "open google": lambda: self.open_website("google.com")
        }
        
        # Create GUI
        self.create_gui()
        
        # Start continuous listening in a separate thread
        self.listening_thread = threading.Thread(target=self.run_async_loop, daemon=True)
        self.listening_thread.start()
        
        # Set up auto-start
        self.setup_autostart()
        
        # Initial greeting
        asyncio.run_coroutine_threadsafe(self.speak("Voice control system initialized"), asyncio.get_event_loop())
    
    def get_chrome_path(self):
        """Get the path to Google Chrome based on the operating system"""
        if platform.system() == "Windows":
            # Common Chrome paths on Windows
            paths = [
                os.path.join(os.environ.get("PROGRAMFILES", ""), "Google", "Chrome", "Application", "chrome.exe"),
                os.path.join(os.environ.get("LOCALAPPDATA", ""), "Google", "Chrome", "Application", "chrome.exe")
            ]
            for path in paths:
                if os.path.exists(path):
                    return path
            return None  # Let webbrowser handle it if not found
        elif platform.system() == "Darwin":
            return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        else:  # Linux
            return "/usr/bin/google-chrome"
    
    def run_async_loop(self):
        """Run the asyncio loop in a separate thread"""
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.continuous_listening())
    
    def create_gui(self):
        """Create the system status window with modern styling"""
        self.root = tk.Tk()
        self.root.title("Voice Control System")
        self.root.geometry("320x200")
        self.root.resizable(False, False)
        
        # Use themed widgets
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        bg_color = "#2d2d2d"
        fg_color = "#ffffff"
        accent_color = "#4a90e2"
        
        style.configure('TFrame', background=bg_color)
        style.configure('TLabel', background=bg_color, foreground=fg_color)
        style.configure('TButton', background=bg_color, foreground=fg_color)
        style.configure('Accent.TButton', background=accent_color, foreground=fg_color)
        
        self.root.configure(bg=bg_color)
        
        # Status indicators
        self.status_frame = ttk.Frame(self.root)
        self.status_frame.pack(pady=15)
        
        self.status_label = ttk.Label(
            self.status_frame, 
            text="System Status:", 
            font=('Segoe UI', 10)
        )
        self.status_label.pack(side=tk.LEFT)
        
        self.status_value = ttk.Label(
            self.status_frame, 
            text="Active" if self.active else "Inactive", 
            font=('Segoe UI', 10, 'bold')
        )
        self.status_value.pack(side=tk.LEFT, padx=5)
        
        # Visual indicator
        self.indicator = tk.Canvas(
            self.root, 
            width=30, 
            height=30, 
            highlightthickness=0,
            bg=bg_color
        )
        self.indicator.pack(pady=5)
        self.update_indicator()
        
        # Control buttons
        self.btn_frame = ttk.Frame(self.root)
        self.btn_frame.pack(pady=15)
        
        self.activate_btn = ttk.Button(
            self.btn_frame, 
            text="Activate", 
            command=self.activate_system,
            style="Accent.TButton"
        )
        self.activate_btn.pack(side=tk.LEFT, padx=5)
        
        self.deactivate_btn = ttk.Button(
            self.btn_frame,
            text="Deactivate",
            command=self.deactivate_system
        )
        self.deactivate_btn.pack(side=tk.LEFT, padx=5)
        
        # Make window always on top
        self.root.attributes('-topmost', True)
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def update_indicator(self):
        """Update the status indicator"""
        self.indicator.delete("all")
        color = "#4CAF50" if self.active else "#F44336"  # Green/Red
        self.indicator.create_oval(5, 5, 25, 25, fill=color, outline="")
        status = "Active - Listening" if self.active else "Inactive"
        self.status_value.config(text=status)
    
    async def speak(self, text: str):
        """Convert text to speech using Edge TTS"""
        try:
            communicate = edge_tts.Communicate(text, self.voice)
            await communicate.save("temp.mp3")
            
            # Play audio using platform-appropriate method
            if platform.system() == "Windows":
                os.startfile("temp.mp3")
            elif platform.system() == "Darwin":  # MacOS
                subprocess.run(["afplay", "temp.mp3"])
            else:  # Linux
                subprocess.run(["aplay", "temp.mp3"])
                
            os.remove("temp.mp3")
        except Exception as e:
            print(f"TTS Error: {e}")
    
    def listen_for_command(self) -> Optional[str]:
        """Listen for a voice command"""
        with self.microphone as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                command = self.recognizer.recognize_google(audio).lower()
                print(f"Recognized: {command}")
                return command
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                print("Could not understand audio")
                return None
            except sr.RequestError as e:
                print(f"Recognition error: {e}")
                return None
    
    async def process_command(self, command: str):
        """Process the voice command"""
        if not command:
            return
        
        # Check if command starts with trigger word
        if command.startswith(self.trigger_word):
            command = command[len(self.trigger_word):].strip()
        
        # Check for exact matches
        for cmd, action in self.commands.items():
            if cmd in command:
                if asyncio.iscoroutinefunction(action):
                    await action()
                else:
                    action()
                return
        
        # Check for search queries
        if any(prefix in command for prefix in ["search for", "look up", "find"]):
            query = command.split("for")[-1].strip() if "for" in command else command.split("up")[-1].strip()
            await self.web_search(query)
            return
        
        # Default response
        await self.speak("I didn't understand that command. Please try again.")
    
    async def continuous_listening(self):
        """Continuously listen for commands"""
        while True:
            if self.active:
                command = self.listen_for_command()
                if command and (self.trigger_word in command or not self.trigger_word):
                    await self.process_command(command)
            await asyncio.sleep(0.1)
    
    def activate_system(self):
        """Activate the system"""
        self.active = True
        self.update_indicator()
        asyncio.run_coroutine_threadsafe(self.speak("System activated. How can I help you?"), asyncio.get_event_loop())
    
    def deactivate_system(self):
        """Deactivate the system"""
        self.active = False
        self.update_indicator()
        asyncio.run_coroutine_threadsafe(self.speak("System deactivated."), asyncio.get_event_loop())
    
    # Command implementations
    def open_chrome(self):
        """Open Google Chrome browser"""
        asyncio.run_coroutine_threadsafe(self.speak("Opening Google Chrome"), asyncio.get_event_loop())
        try:
            if self.browser_path:
                if platform.system() == "Windows":
                    os.startfile(self.browser_path)
                elif platform.system() == "Darwin":
                    subprocess.Popen([self.browser_path])
                else:
                    subprocess.Popen([self.browser_path])
            else:
                # Fallback to webbrowser module
                webbrowser.get("chrome").open_new("")
        except Exception as e:
            print(f"Error opening Chrome: {e}")
            asyncio.run_coroutine_threadsafe(self.speak("Could not open Google Chrome"), asyncio.get_event_loop())
    
    def open_website(self, url: str):
        """Open a specific website in Chrome"""
        asyncio.run_coroutine_threadsafe(self.speak(f"Opening {url}"), asyncio.get_event_loop())
        try:
            if self.browser_path:
                if platform.system() == "Windows":
                    os.startfile(f"chrome.exe --new-window https://{url}")
                elif platform.system() == "Darwin":
                    subprocess.Popen([self.browser_path, f"https://{url}"])
                else:
                    subprocess.Popen([self.browser_path, f"https://{url}"])
            else:
                webbrowser.get("chrome").open_new(f"https://{url}")
        except Exception as e:
            print(f"Error opening website: {e}")
            asyncio.run_coroutine_threadsafe(self.speak(f"Could not open {url}"), asyncio.get_event_loop())
    
    def open_vscode(self):
        """Open Visual Studio Code"""
        asyncio.run_coroutine_threadsafe(self.speak("Opening Visual Studio Code"), asyncio.get_event_loop())
        try:
            if platform.system() == "Windows":
                os.startfile("code")
            elif platform.system() == "Darwin":
                subprocess.Popen(["/usr/bin/open", "-a", "Visual Studio Code"])
            else:
                subprocess.Popen(["code"])
        except Exception as e:
            print(f"Error opening VS Code: {e}")
            asyncio.run_coroutine_threadsafe(self.speak("Could not open Visual Studio Code"), asyncio.get_event_loop())
    
    def system_shutdown(self):
        """Shutdown the computer"""
        asyncio.run_coroutine_threadsafe(self.speak("Shutting down the system"), asyncio.get_event_loop())
        try:
            if platform.system() == "Windows":
                os.system("shutdown /s /t 1")
            elif platform.system() == "Darwin":
                os.system("shutdown -h now")
            else:
                os.system("shutdown now")
        except Exception as e:
            print(f"Error shutting down: {e}")
            asyncio.run_coroutine_threadsafe(self.speak("Could not shutdown the system"), asyncio.get_event_loop())
    
    async def good_morning_response(self):
        """Respond to good morning"""
        hour = datetime.datetime.now().hour
        if hour < 12:
            response = "Good morning! Ready for a productive day?"
        else:
            response = "Good morning to you too, though it's actually afternoon!"
        await self.speak(response)
    
    async def good_evening_response(self):
        """Respond to good evening"""
        hour = datetime.datetime.now().hour
        if hour >= 17:
            response = "Good evening! How was your day?"
        else:
            response = "Good evening to you, though it's still daytime!"
        await self.speak(response)
    
    async def good_night_response(self):
        """Respond to good night"""
        hour = datetime.datetime.now().hour
        if hour >= 21 or hour < 4:
            response = "Good night! Sleep well."
        else:
            response = "Good night to you, though it's a bit early for bed!"
        await self.speak(response)
    
    async def current_time(self):
        """Tell the current time"""
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        await self.speak(f"The current time is {time_str}")
    
    async def web_search(self, query: str):
        """Perform a web search"""
        if not query:
            await self.speak("What would you like me to search for?")
            query = self.listen_for_command()
            if not query:
                return
        
        await self.speak(f"Searching for {query}")
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        
        try:
            if self.browser_path:
                if platform.system() == "Windows":
                    os.startfile(f"chrome.exe --new-window {url}")
                elif platform.system() == "Darwin":
                    subprocess.Popen([self.browser_path, url])
                else:
                    subprocess.Popen([self.browser_path, url])
            else:
                webbrowser.get("chrome").open_new(url)
        except Exception as e:
            print(f"Error performing search: {e}")
            await self.speak("I couldn't perform that search")
    
    def setup_autostart(self):
        """Set up the program to start automatically on system startup"""
        try:
            if platform.system() == "Windows":
                import winreg
                key = winreg.OpenKey(
                    winreg.HKEY_CURRENT_USER,
                    r"Software\Microsoft\Windows\CurrentVersion\Run",
                    0, winreg.KEY_SET_VALUE
                )
                winreg.SetValueEx(
                    key, 
                    "VoiceAutomation", 
                    0, 
                    winreg.REG_SZ, 
                    f'"{sys.executable}" "{os.path.abspath(__file__)}"'
                )
                winreg.CloseKey(key)
            elif platform.system() == "Darwin":
                # Create a plist file in ~/Library/LaunchAgents/
                pass
            else:
                # Add to ~/.config/autostart/
                pass
        except Exception as e:
            print(f"Autostart setup failed: {e}")
    
    def on_closing(self):
        """Handle window closing"""
        self.deactivate_system()
        self.root.destroy()
    
    def run(self):
        """Run the application"""
        self.root.mainloop()

if __name__ == "__main__":
    system = VoiceAutomationSystem()
    system.run()