import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

CODEOWNERS = ["@gongloo"]
DEPENDENCIES = ["uart"]
MULTI_CONF = True

sungoldpower_lfp_ns = cg.esphome_ns.namespace("sungoldpower_lfp")
SunGoldPowerLFP = sungoldpower_lfp_ns.class_("SunGoldPowerLFP", cg.PollingComponent, uart.UARTDevice)

CONF_SUNGOLDPOWER_LFP_ID = "sungoldpower_lfp_id"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(SunGoldPowerLFP),
        }
    )
    .extend(cv.polling_component_schema("10s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
