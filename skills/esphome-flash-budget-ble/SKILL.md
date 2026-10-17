---
name: esphome-flash-budget-ble
description: Fit Bluetooth LE presence scanning onto a flash-limited ESP32 ESPHome node (e.g. ESP32-C6 with voice/wake word) by replacing esp32_ble_tracker with a NimBLE observer-only external component. Use when an ESPHome build overflows flash after adding BLE, or when designing lightweight room-presence sensing on ESP32.
---

# ESPHome flash-budget BLE presence

## Why
`esp32_ble_tracker` pulls in Bluedroid (~500–600 KB). Next to on-device wake word on a 4 MB board it can push the app partition past 100%. Presence sensing only needs to *listen* to advertisements, so NimBLE with only the observer role is enough and much smaller (field result: 109% → ~92% flash on a XIAO ESP32-C6 voice node).

## Workflow
1. **Measure first.** Compile the current config and note flash/RAM %. Compile once with stock BLE to confirm the overflow is BLE.
2. **Use an external component** (`external_components: - source: {type: local, path: components}`) that:
   - sets sdkconfig: `CONFIG_BT_ENABLED=y`, `CONFIG_BT_BLUEDROID_ENABLED=n`, `CONFIG_BT_NIMBLE_ENABLED=y`, `ROLE_OBSERVER=y`, central/peripheral/broadcaster/GATT/security/NVS persist/5.0 features **off**, NimBLE log level none, small host task stack (~3 KB);
   - declares `CONFLICTS_WITH` `esp32_ble`, `esp32_ble_tracker`, `bluetooth_proxy`;
   - calls `nimble_port_init()`, sets `ble_hs_cfg.sync_cb`, starts `nimble_port_freertos_init()`, then a **passive** `ble_gap_disc` with `filter_duplicates=0` (repeats carry RSSI change = movement).
3. **Keep the callback cheap.** The GAP callback runs on the NimBLE host task: use a fixed-size table (e.g. 40 entries), a mutex taken with a few-ms timeout (drop the sample rather than block), and recycle the stalest slot when full. No heap allocation per advertisement.
4. **Publish aggregates, not identities:** devices above an RSSI threshold, Apple devices (manufacturer data company ID `0x004C`), strongest RSSI, and a "motion" score (mean |RSSI − EMA| per device). This avoids storing MAC addresses in Home Assistant.
5. **Share the radio.** Pause scanning while the voice assistant is streaming; use a low duty cycle (e.g. 30 ms window / 320 ms interval) and enable software coexistence.
6. **Verify on-device:** OTA flash, then check voice satellite returns to idle, heap free / largest block sensors are healthy, and BLE sensors update. Keep the previous firmware for rollback.
7. **Tune with data, not guesses:** log strongest RSSI per room for a day; set the threshold relative to that baseline or use an adaptive rule (fire when strongest RSSI ≥ rolling median + ~10 dB).

## Common mistakes
- Leaving `esp32_ble_tracker` anywhere in included packages (conflict / both stacks linked).
- Using `filter_duplicates=1` — you lose the RSSI stream that makes motion detection work.
- Blocking in the scan callback (starves NimBLE, drops Wi-Fi/voice).
- Treating a single RSSI reading as distance; RSSI is noisy — smooth it.
- Assuming random-MAC phones are stable identities; count, don't track.
