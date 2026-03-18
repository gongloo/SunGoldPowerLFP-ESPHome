# SunGoldPower LFP ESPHome Firmware

ESPHome firmware for SunGoldPower LFP series inverter/chargers. This project allows you to monitor your inverter's telemetry and control output power using an ESP32.

## Quick Documentation

For a full rundown on how to use this project, including wiring diagrams and a browser-based installer, please visit the documentation page:

**[SunGoldPower LFP ESPHome Documentation](https://gongloo.github.io/SunGoldPowerLFP-ESPHome/)**

Technical details regarding the communication protocol can be found in the [Serial Protocol Documentation](protocol.md).

## Features

- **Real-time Monitoring**: Input/output voltage, current, frequency, battery voltage, and temperature.
- **Status Indicators**: Monitoring for utility status, battery levels, and fault states.
- **Relay Control**: Inverter power control via GPIO.
- **Web Installer**: Flash your ESP32 directly from your browser.

## Acknowledgements

- Special thanks to the contributors at [SecondLifeStorage](https://secondlifestorage.com/index.php?threads/aims-lf-inverter-rj45-protocol-information.10348/) for providing the initial protocol documentation that made this project possible.
- Developed with the assistance of **Antigravity**, an AI coding assistant from Google Deepmind.
