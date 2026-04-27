#pragma once

#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/binary_sensor/binary_sensor.h"
#include <string>

namespace esphome {
namespace sungoldpower_lfp {

class SunGoldPowerLFP : public PollingComponent, public uart::UARTDevice {
 public:
  void set_ip_voltage_sensor(sensor::Sensor *sensor) { this->ip_voltage_sensor_ = sensor; }
  void set_ip_fault_voltage_sensor(sensor::Sensor *sensor) { this->ip_fault_voltage_sensor_ = sensor; }
  void set_op_voltage_sensor(sensor::Sensor *sensor) { this->op_voltage_sensor_ = sensor; }
  void set_op_current_sensor(sensor::Sensor *sensor) { this->op_current_sensor_ = sensor; }
  void set_op_frequency_sensor(sensor::Sensor *sensor) { this->op_frequency_sensor_ = sensor; }
  void set_battery_voltage_sensor(sensor::Sensor *sensor) { this->battery_voltage_sensor_ = sensor; }
  void set_temperature_sensor(sensor::Sensor *sensor) { this->temperature_sensor_ = sensor; }

  void set_utility_fail_binary_sensor(binary_sensor::BinarySensor *sensor) { this->utility_fail_binary_sensor_ = sensor; }
  void set_battery_low_binary_sensor(binary_sensor::BinarySensor *sensor) { this->battery_low_binary_sensor_ = sensor; }
  void set_avr_active_binary_sensor(binary_sensor::BinarySensor *sensor) { this->avr_active_binary_sensor_ = sensor; }
  void set_ups_failed_binary_sensor(binary_sensor::BinarySensor *sensor) { this->ups_failed_binary_sensor_ = sensor; }
  void set_line_interactive_binary_sensor(binary_sensor::BinarySensor *sensor) { this->line_interactive_binary_sensor_ = sensor; }
  void set_test_progress_binary_sensor(binary_sensor::BinarySensor *sensor) { this->test_progress_binary_sensor_ = sensor; }
  void set_shutdown_active_binary_sensor(binary_sensor::BinarySensor *sensor) { this->shutdown_active_binary_sensor_ = sensor; }
  void set_beeper_on_binary_sensor(binary_sensor::BinarySensor *sensor) { this->beeper_on_binary_sensor_ = sensor; }

  void setup() override;
  void loop() override;
  void update() override;
  void dump_config() override;

 protected:
  void read_line_();
  sensor::Sensor *ip_voltage_sensor_{nullptr};
  sensor::Sensor *ip_fault_voltage_sensor_{nullptr};
  sensor::Sensor *op_voltage_sensor_{nullptr};
  sensor::Sensor *op_current_sensor_{nullptr};
  sensor::Sensor *op_frequency_sensor_{nullptr};
  sensor::Sensor *battery_voltage_sensor_{nullptr};
  sensor::Sensor *temperature_sensor_{nullptr};

  binary_sensor::BinarySensor *utility_fail_binary_sensor_{nullptr};
  binary_sensor::BinarySensor *battery_low_binary_sensor_{nullptr};
  binary_sensor::BinarySensor *avr_active_binary_sensor_{nullptr};
  binary_sensor::BinarySensor *ups_failed_binary_sensor_{nullptr};
  binary_sensor::BinarySensor *line_interactive_binary_sensor_{nullptr};
  binary_sensor::BinarySensor *test_progress_binary_sensor_{nullptr};
  binary_sensor::BinarySensor *shutdown_active_binary_sensor_{nullptr};
  binary_sensor::BinarySensor *beeper_on_binary_sensor_{nullptr};

  std::string rx_buffer_;
};

}  // namespace sungoldpower_lfp
}  // namespace esphome
