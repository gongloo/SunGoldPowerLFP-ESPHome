# TTL Communication Protocol for Inverter

## 1. General Overview

This document outlines the TTL communications protocol utilized in SunGoldPower LFP and AIMS PICO series Inverter/Chargers. It is also likely compatible with Sigineer low frequency Inverter/Chargers as well, though this has not been tested. The protocol enables a computer to control information exchange by sending a query followed by a carriage return (`<cr>`). The inverter subsequently responds with the requested information or performs an action, also followed by a `<cr>`.

The protocol provides the following core capabilities:

- Monitor charger status.
- Monitor battery status and condition.
- Monitor the utility status.

## 2. Hardware Specifications

The communication interface utilizes the following serial port settings:

- **Baud Rate:** 2400 bps
- **Data Length:** 8 bits
- **Stop Bit:** 1 bit
- **Parity:** NONE

**Pinout Configuration:**
| Computer | Inverter |
| :--- | :--- |
| RX | TX (pin 6) |
| TX | RX (pin 8) |
| GND | GND (pin 2) |
| +5V | +5V (pin 4) |

## 3. Communications Protocol Commands

### 3.1 Status Inquiry

This command queries the real-time status telemetry of the inverter.

- **Computer sends:** `Q1<cr>`
- **Inverter responds:** `(MMM.M NNN.N PPP.P QQQ RR.R S.SS TT.T b7b6b5b4b3b2b1b0<cr>`

**Data Stream Field Definitions:**
_(Note: A space character separates every field.)_

- **Start byte:** `(`
- **I/P voltage:** `MMM.M` (Integer 0-9; Unit: Volt)
- **I/P fault voltage:** `NNN.N` (Integer 0-9; Unit: Volt)
- **O/P voltage:** `PPP.P` (Integer 0-9; Unit: Volt)
- **O/P current:** `QQQ` (Percentage of maximum current, not absolute)
- **O/P frequency:** `RR.R` (Integer 0-9; Unit: Hz)
- **Battery voltage:** `SS.S` or `S.SS` (Integer 0-9). On-line units provide voltage/cell as `S.SS`. Standby units provide actual voltage as `SS.S`. The inverter status type dictates this format.
- **Temperature:** `TT.T` (Integer 0-9; Unit: Degrees Celsius)
- **Inverter Status (`<U>`):** A single byte of binary information formatted as `b7b6b5b4b3b2b1b0` where each bit is an ASCII `0` or `1`.
- **Stop Byte:** `<cr>`

**Status Byte Bitmask Breakdown (`<U>`):**
| Bit | Description (When set to '1') |
| :--- | :--- |
| **7** | Utility Fail (Immediate) |
| **6** | Battery Low |
| **5** | AVR (0 means NORMAL) |
| **4** | Inverter Failed |
| **3** | Inverter Type is Line-Interactive (0 means On-line) |
| **2** | Test in Progress |
| **1** | Shutdown Active |
| **0** | Beeper On

> **Example Query & Response:**
>
> - **Computer:** `Q1<cr>`
> - **Inverter:** `(208.4 140.0 208.4 034 59.9 2.05 35.0 00110000<cr>`
> - **Interpretation:** I/P voltage is 208.4V , I/P fault voltage is 140.0V , O/P voltage is 208.4V , O/P current is 34% , I/P frequency is 59.9 HZ , Battery voltage is 2.05V , Temperature is 35.0 degrees of centigrade , Status: Inverter type is on-line, Inverter failed, AVR active, and shutdown not active.

### 3.2 Turn On/Off Beep (Toggle Beeper)

Toggles the warning beep generated when AC power fails, allowing the manager to silence the alarm.

- **Computer sends:** `Q<cr>`

### 3.3 Inverter Rating Information

Queries the hardware rating values of the unit.

- **Computer sends:** `F<cr>`
- **Inverter responds:** `#MMM.M QQQ SS.SS RR.R<cr>`

_(Fields are separated by spaces.)_

- **Rating Voltage:** `MMM.M`
- **Rating Current:** `QQQ`
- **Battery Voltage:** `SS.SS` or `SSS.S`
- **Frequency:** `RR.R`

### 3.4 Additional System Queries

- **Inverter Password:** \* **Computer:** `M<cr>`

* **Inverter:** `C<cr>` / RUN formula

- **Inverter Fault State Query:** \* **Computer:** `G? <cr>`

* **Inverter Responses:** `"Normal 04<cr>Fa"<cr>` (if normal) or `"Over Load"<cr>` (if overloaded)

- **Inverter Charger Action Query:** \* **Computer:** `D<cr>`

* **Inverter Responses:** `"ACK"<cr>` (if charging) or `"NAK"<cr>` (if not charging)
