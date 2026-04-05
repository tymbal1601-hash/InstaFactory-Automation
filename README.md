# 📱 InstaFactory-Automation
### *Multi-Device Mobile Automation System*

---

## 🚀 Overview
**InstaFactory Pro** is a high-performance automation solution designed for scalable Instagram content management. Built with **Python**, **Appium**, and **Flet**, it enables seamless, parallel execution of complex tasks across multiple Android devices or emulators simultaneously.

<img width="1280" height="855" alt="image" src="https://github.com/user-attachments/assets/ae39f55e-64d1-4838-ad1d-acf6e861b483" />

---

## ✨ Key Features

* **🌐 Multi-Instance Management**
    Independent execution threads for each device, allowing simultaneous management of dozens of accounts without UI freezes.
* **🤖 Intelligent UI Interaction**
    Leverages **Appium (UiAutomator2)** with advanced `WebDriverWait` strategies to handle dynamic elements and network latency.
* **🔌 Hybrid ADB Integration**
    Combines high-level UI automation with low-level **ADB** commands for lightning-fast file transfers and media scanning.
* **🛡️ Smart VPN Controller**
    Native support for **VPN**, ensuring unique IP addresses for every session to minimize ban risks.
* **🔐 Security & Licensing**
    Custom **NTP-based verification** system that validates license integrity against global network time (bypassing local clock manipulation).
* **📊 Real-time Logging**
    A sleek, responsive dashboard providing per-device live logs for instant status monitoring.

---

## 🛠 Technology Stack

| Category | Tools & Technologies |
| :--- | :--- |
| **Language** | `Python 3.10+` |
| **Automation** | `Appium`, `Selenium`, `ADB` |
| **Frontend** | `Flet` (Flutter-based UI) |
| **Architecture** | `Multithreading`, `OOP`, `POM` |

---

## 📂 Repository Structure

> **insta_factory_core** — File with basic logic of software, note **this is a demonstration snippet highlighting the architecture.**

---

## ⚙️ How It Works

1.  **License Check:** System queries **NTP servers** (e.g., `time.google.com`) to verify subscription.
2.  **Thread Allocation:** Spawns a dedicated `threading.Thread` for each Device ID (UDID).
3.  **Environment Sync:** Files are pushed via **ADB**, followed by a media scan.
4.  **Automation Loop:** `ProfileInstance` handles human-like interactions with randomized delays.

---

## 📽 Demonstration

> [!TIP]
> **[Watch the automation in action here →](ТВОЯ_ССЫЛКА_НА_ВИДЕО)**
> *Video showcases simultaneous uploading on multiple devices.*

---

## ⚠️ Disclaimer
> [!IMPORTANT]
> This repository contains the **core architecture** and **UI demonstration**. The main code of fully functional software was hidden
