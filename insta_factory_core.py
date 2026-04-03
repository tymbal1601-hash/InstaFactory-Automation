import flet as ft
import threading
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

class InstaFactoryDemo:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "InstaFactory Pro - Multi-Device Automation"
        self.page.theme_mode = ft.ThemeMode.DARK
        
        # UI Components initialization
        self.log_area = ft.ListView(expand=True, spacing=5, auto_scroll=True)
        self.start_button = ft.ElevatedButton(
            "Start Automation", 
            on_click=self.start_threads,
            style=ft.ButtonStyle(color="white", bgcolor="green")
        )
        
        # Build Main Layout
        self.page.add(
            ft.Text("Device Control Dashboard", size=25, weight="bold"),
            ft.Container(
                content=self.log_area,
                height=300,
                border=ft.border.all(1, "grey"),
                padding=10
            ),
            self.start_button
        )

    def logger(self, message):
        """Thread-safe logging to the Flet UI"""
        current_time = time.strftime("%H:%M:%S")
        self.log_area.controls.append(ft.Text(f"[{current_time}] {message}"))
        self.page.update()

    def run_automation_logic(self, device_id):
        """
        Main automation logic running in a separate thread.
        This prevents the UI from freezing during Appium operations.
        """
        try:
            self.logger(f"Initializing driver for device: {device_id}")
            
            # Appium capabilities setup
            options = UiAutomator2Options()
            options.set_capability('deviceName', device_id)
            options.set_capability('platformName', 'Android')
            # options.set_capability('appPackage', 'com.instagram.android')
            
            self.logger("Connecting to Appium server...")
            # Driver would be initialized here:
            # driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
            
            # Simulated automation steps
            time.sleep(2) 
            self.logger(f"Device {device_id}: Bypassing bot-detection...")
            time.sleep(2)
            self.logger(f"Device {device_id}: Starting content upload process...")
            
        except Exception as e:
            self.logger(f"Error on device {device_id}: {str(e)}")

    def start_threads(self, e):
        """Spawns background threads for parallel device management"""
        devices = ["Emulator_5554", "RealDevice_ADB1"]
        
        self.start_button.disabled = True
        self.page.update()
        
        for device in devices:
            # Creating a daemon thread for each device
            thread = threading.Thread(target=self.run_automation_logic, args=(device,), daemon=True)
            thread.start()
            self.logger(f"Thread started for {device}")

if __name__ == "__main__":
    ft.app(target=InstaFactoryDemo)
