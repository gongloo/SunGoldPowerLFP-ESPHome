import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_TEMPERATURE,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLTAGE,
    UNIT_VOLT,
    UNIT_CELSIUS,
    UNIT_HERTZ,
    UNIT_PERCENT,
)
from . import sungoldpower_lfp_ns, SunGoldPowerLFP, CONF_SUNGOLDPOWER_LFP_ID

DEPENDENCIES = ["sungoldpower_lfp"]

CONF_IP_VOLTAGE = "ip_voltage"
CONF_IP_FAULT_VOLTAGE = "ip_fault_voltage"
CONF_OP_VOLTAGE = "op_voltage"
CONF_OP_CURRENT = "op_current"
CONF_OP_FREQUENCY = "op_frequency"
CONF_BATTERY_VOLTAGE = "battery_voltage"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_SUNGOLDPOWER_LFP_ID): cv.use_id(SunGoldPowerLFP),
        cv.Optional(CONF_IP_VOLTAGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:flash",
        ),
        cv.Optional(CONF_IP_FAULT_VOLTAGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:flash-alert",
        ),
        cv.Optional(CONF_OP_VOLTAGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:flash",
        ),
        cv.Optional(CONF_OP_CURRENT): sensor.sensor_schema(
            unit_of_measurement=UNIT_PERCENT,
            accuracy_decimals=0,
            icon="mdi:current-ac",
        ),
        cv.Optional(CONF_OP_FREQUENCY): sensor.sensor_schema(
            unit_of_measurement=UNIT_HERTZ,
            accuracy_decimals=1,
            device_class="frequency",
            icon="mdi:sine-wave",
        ),
        cv.Optional(CONF_BATTERY_VOLTAGE): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=2,
            device_class=DEVICE_CLASS_VOLTAGE,
            icon="mdi:battery",
        ),
        cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
            unit_of_measurement=UNIT_CELSIUS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_TEMPERATURE,
            icon="mdi:thermometer",
        ),
    }
)

async def to_code(config):
    hub = await cg.get_variable(config[CONF_SUNGOLDPOWER_LFP_ID])
    if CONF_IP_VOLTAGE in config:
        sens = await sensor.new_sensor(config[CONF_IP_VOLTAGE])
        cg.add(hub.set_ip_voltage_sensor(sens))
    if CONF_IP_FAULT_VOLTAGE in config:
        sens = await sensor.new_sensor(config[CONF_IP_FAULT_VOLTAGE])
        cg.add(hub.set_ip_fault_voltage_sensor(sens))
    if CONF_OP_VOLTAGE in config:
        sens = await sensor.new_sensor(config[CONF_OP_VOLTAGE])
        cg.add(hub.set_op_voltage_sensor(sens))
    if CONF_OP_CURRENT in config:
        sens = await sensor.new_sensor(config[CONF_OP_CURRENT])
        cg.add(hub.set_op_current_sensor(sens))
    if CONF_OP_FREQUENCY in config:
        sens = await sensor.new_sensor(config[CONF_OP_FREQUENCY])
        cg.add(hub.set_op_frequency_sensor(sens))
    if CONF_BATTERY_VOLTAGE in config:
        sens = await sensor.new_sensor(config[CONF_BATTERY_VOLTAGE])
        cg.add(hub.set_battery_voltage_sensor(sens))
    if CONF_TEMPERATURE in config:
        sens = await sensor.new_sensor(config[CONF_TEMPERATURE])
        cg.add(hub.set_temperature_sensor(sens))
