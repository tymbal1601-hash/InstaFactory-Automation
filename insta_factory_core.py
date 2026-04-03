import flet as ft
import threading
import ntplib
import time
import os
from datetime import datetime, timezone
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DateChecker:
    """
    Security module to prevent unauthorized use by checking 
    system time against reliable NTP servers.
    """
    def get_time_from_ntp(self):
        ntp_servers = ['pool.ntp.org', 'time.google.com', 'time.windows.com']
        client = ntplib.NTPClient()
        for server in ntp_servers:
            try:
                # Fetching network time to bypass local system time manipulation
                response = client.request(server, version=3)
                return datetime.fromtimestamp(response.tx_time, timezone.utc)
            except Exception as e:
                print(f"NTP Error ({server}): {e}")
        return None

class ProfileInstance:
    """
    Handles independent automation logic for a specific mobile device.
    """
    def __init__(self, device_name, app_context):
        self.device_name = device_name
        self.app = app_context # Reference to the main Flet app for UI updates
        self.driver = None

    def logger(self, message):
        """Thread-safe logging to the specific device tab in UI"""
        print(f"[{self.device_name}] {message}")
        # In real app: self.app.ui.update_log(self.device_name, message)

    def init_driver(self):
        """Initializes Appium driver with specific Android options"""
        options = UiAutomator2Options()
        options.set_capability('deviceName', self.device_name)
        options.set_capability('platformName', 'Android')
        options.set_capability('automationName', 'UiAutomator2')
        options.set_capability('noReset', True)
        
        # Example of dynamic driver connection
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

    def upload_content(self):
        """
        Core automation logic: uses Appium to interact with Instagram UI.
        Runs in a background thread to keep the GUI responsive.
        """
        try:
            self.init_driver()
            self.logger("Step 1: Pushing media via ADB...")
            # ADB command execution example
            os.system(f"adb -s {self.device_name} push video.mp4 /sdcard/Download/")

            self.logger("Step 2: Navigating to Upload section...")
            wait = WebDriverWait(self.driver, 20)
            
            # Professional way to find elements using Explicit Waits
            add_btn = wait.until(EC.presence_of_element_located(
                (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Camera']")
            ))
            add_btn.click()
            
            self.logger("Automation successful.")
        except Exception as e:
            self.logger(f"Critical Automation Error: {str(e)}")
        finally:
            if self.driver:
                self.driver.quit()

class InstaFactoryApp:
    """
    Main Application class using Flet (Flutter for Python).
    Manages UI and orchestrates multiple automation threads.
    """
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "InstaFactory Pro"
        self.checker = DateChecker()
        self.setup_ui()

    def setup_ui(self):
        """Initializes the main Dashboard layout"""
        self.status_text = ft.Text("Checking License...", color="orange")
        self.start_btn = ft.ElevatedButton(
            "Launch Multi-Thread Upload", 
            on_click=self.on_start_click,
            disabled=True
        )
        
        self.page.add(
            ft.Row([ft.Text("InstaFactory Control Panel", size=30, weight="bold")]),
            self.status_text,
            self.start_btn
        )
        self.check_access()

    def check_access(self):
        """Validation logic using NTP time"""
        current_time = self.checker.get_time_from_ntp()
        if current_time and current_time < datetime(2025, 1, 1, tzinfo=timezone.utc):
            self.status_text.value = "License Active"
            self.status_text.color = "green"
            self.start_btn.disabled = False
        else:
            self.status_text.value = "License Expired or Network Error"
            self.status_text.color = "red"
        self.page.update()

    def on_start_click(self, e):
        """Spawns background threads for each profile to prevent UI freezing"""
        active_profiles = ["Pixel_6_Emulator", "Samsung_S21_Real"]
        
        for profile_name in active_profiles:
            instance = ProfileInstance(profile_name, self)
            # Multithreading is crucial for handling multiple devices
            threading.Thread(target=instance.upload_content, daemon=True).start()
            print(f"Started thread for {profile_name}")

if __name__ == "__main__":
    ft.app(target=InstaFactoryApp)
