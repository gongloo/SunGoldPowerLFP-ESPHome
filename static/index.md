# SunGoldPower LFP Inverter ESPHome Firmware

This project provides ESPHome-based firmware for monitoring and controlling SunGoldPower LFP series inverter/chargers using an ESP32. It communicates with the inverter via its TTL serial port (typically an RJ45 jack).

## Features

- **Real-time Monitoring**: Track input/output voltage, frequency, current, battery voltage, and temperature.
- **Status Indicators**: Receive binary status for utility failure, battery low, AVR status, UPS failure, and more.
- **Remote Control**: Integrated relay control for inverter power state (optional).
- **Web Installer**: Flash directly from your browser via USB.

## Bill of Materials

To build this controller, you will need:

- **ESP32 Board**: **ESP32 Single Relay Board** (commonly found on AliExpress or similar).
- **Inverter**: SunGoldPower LFP Series Inverter/Charger.
- **Wiring**:
  - RJ45 cable.
  - RJ45 female to female adapter breakout board.
  - Jumper wires for connecting the breakout board and relay board.

## Wiring Guide

To enable communication, you must connect the ESP32 to the inverter's RJ45 communication port. The following table shows the required connections:

| Inverter RJ45 | Purpose                                      | Relay Board   |
| :------------ | :------------------------------------------- | :------------ |
| Pin 2         | GND                                          | GND           |
| Pin 3         | Inverter On Switch                           | Relay COM     |
| Pin 5         | +12V (Power)                                 | VCC, Relay NO |
| Pin 6         | TX (Inverter Out)                            | GPIO21        |
| Pin 8         | (Optional, not recommended) RX (Inverter In) | GPIO16        |

> [!WARNING]
> Make sure that your board supports 12V on VCC. Some boards only support 5V, which is available from Inverter RJ45 Pin 4.

> [!IMPORTANT]
> **RJ45 Pinout**: Pin 1 is the leftmost pin when looking into the socket with the clip/tab facing down.

> [!WARNING]
> When operating in read-only mode, the remote LCD must be connected to the inverter in parallel with the ESP32. Optionally, the remote LCD can be omitted if the write pin is connected to the inverter. Note this may interfere with remote LCD function and is not recommended.

## Installation

You can use the button below to install the pre-built firmware directly to your device via USB from the browser.

<esp-web-install-button manifest="firmware/sungoldpower-lfp.manifest.json"></esp-web-install-button>

<script type="module" src="https://unpkg.com/esp-web-tools@10/dist/web/install-button.js?module"></script>

## Post-Installation

Once flashed:

1. **Initial WiFi Setup**:
   - **Option A: Improv Wi-Fi**: If your browser/system supports it, you can configure Wi-Fi credentials directly from the installer page using the **Improv** protocol.
   - **Option B: Captive Portal (Fallback Hotspot)**: If the device cannot connect to a known network, it will create its own Wi-Fi hotspot named `sungoldpower-lfp Fallback`.
     1. Connect to this network on your phone or computer.
     2. A portal should open automatically (or visit `192.168.4.1` in your browser).
     3. Select your local Wi-Fi network and enter the password.
2. **Dashboard**: Once connected to your network, the device will appear in your ESPHome dashboard and Home Assistant automatically.
3. **Telemetry**: In Home Assistant, you will find sensors for all telemetry (voltages, current, frequency, etc.) and a switch for the **Inverter Power Relay**.
4. **Customization**: If you need to customize the configuration (e.g., change pins or device name), you can edit the `sungoldpower-lfp.yaml` file and reflash via OTA.
