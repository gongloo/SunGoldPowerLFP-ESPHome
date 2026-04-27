import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import (
    DEVICE_CLASS_PROBLEM,
    DEVICE_CLASS_BATTERY,
)
from . import sungoldpower_lfp_ns, SunGoldPowerLFP, CONF_SUNGOLDPOWER_LFP_ID

DEPENDENCIES = ["sungoldpower_lfp"]

CONF_UTILITY_FAIL = "utility_fail"
CONF_BATTERY_LOW = "battery_low"
CONF_AVR_ACTIVE = "avr_active"
CONF_UPS_FAILED = "ups_failed"
CONF_LINE_INTERACTIVE = "line_interactive"
CONF_TEST_PROGRESS = "test_progress"
CONF_SHUTDOWN_ACTIVE = "shutdown_active"
CONF_BEEPER_ON = "beeper_on"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_SUNGOLDPOWER_LFP_ID): cv.use_id(SunGoldPowerLFP),
        cv.Optional(CONF_UTILITY_FAIL): binary_sensor.binary_sensor_schema(
            device_class=DEVICE_CLASS_PROBLEM,
            icon="mdi:transmission-tower-off",
        ),
        cv.Optional(CONF_BATTERY_LOW): binary_sensor.binary_sensor_schema(
            device_class=DEVICE_CLASS_BATTERY,
            icon="mdi:battery-alert",
        ),
        cv.Optional(CONF_AVR_ACTIVE): binary_sensor.binary_sensor_schema(
            icon="mdi:power-settings",
        ),
        cv.Optional(CONF_UPS_FAILED): binary_sensor.binary_sensor_schema(
            device_class=DEVICE_CLASS_PROBLEM,
            icon="mdi:alert-circle",
        ),
        cv.Optional(CONF_LINE_INTERACTIVE): binary_sensor.binary_sensor_schema(
            icon="mdi:power-plug",
        ),
        cv.Optional(CONF_TEST_PROGRESS): binary_sensor.binary_sensor_schema(
            icon="mdi:progress-wrench",
        ),
        cv.Optional(CONF_SHUTDOWN_ACTIVE): binary_sensor.binary_sensor_schema(
            icon="mdi:power-off",
        ),
        cv.Optional(CONF_BEEPER_ON): binary_sensor.binary_sensor_schema(
            icon="mdi:volume-high",
        ),
    }
)

async def to_code(config):
    hub = await cg.get_variable(config[CONF_SUNGOLDPOWER_LFP_ID])
    if CONF_UTILITY_FAIL in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_UTILITY_FAIL])
        cg.add(hub.set_utility_fail_binary_sensor(sens))
    if CONF_BATTERY_LOW in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_BATTERY_LOW])
        cg.add(hub.set_battery_low_binary_sensor(sens))
    if CONF_AVR_ACTIVE in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_AVR_ACTIVE])
        cg.add(hub.set_avr_active_binary_sensor(sens))
    if CONF_UPS_FAILED in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_UPS_FAILED])
        cg.add(hub.set_ups_failed_binary_sensor(sens))
    if CONF_LINE_INTERACTIVE in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_LINE_INTERACTIVE])
        cg.add(hub.set_line_interactive_binary_sensor(sens))
    if CONF_TEST_PROGRESS in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_TEST_PROGRESS])
        cg.add(hub.set_test_progress_binary_sensor(sens))
    if CONF_SHUTDOWN_ACTIVE in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_SHUTDOWN_ACTIVE])
        cg.add(hub.set_shutdown_active_binary_sensor(sens))
    if CONF_BEEPER_ON in config:
        sens = await binary_sensor.new_binary_sensor(config[CONF_BEEPER_ON])
        cg.add(hub.set_beeper_on_binary_sensor(sens))
