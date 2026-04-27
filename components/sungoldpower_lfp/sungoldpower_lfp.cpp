#include "sungoldpower_lfp.h"
#include "esphome/core/log.h"
#include <cstdio>

namespace esphome {
namespace sungoldpower_lfp {

static const char *const TAG = "sungoldpower_lfp";

void SunGoldPowerLFP::setup() {
  this->rx_buffer_.clear();
}

void SunGoldPowerLFP::update() {
  this->write_str("Q1\r");
}

void SunGoldPowerLFP::loop() {
  while (this->available()) {
    char c = this->read();
    if (c == '\r') {
      if (!this->rx_buffer_.empty()) {
        this->read_line_();
        this->rx_buffer_.clear();
      }
    } else if (c == '\n') {
      // Ignore newlines
    } else {
      this->rx_buffer_ += c;
    }
  }
}

void SunGoldPowerLFP::read_line_() {
  ESP_LOGD(TAG, "RX: %s", this->rx_buffer_.c_str());

  if (this->rx_buffer_.find("(") == 0) {
    float ip_v, ip_f_v, op_v, op_c, op_f, bat_v, temp;
    char bits[9] = {0};

    // Skip initial ' ' if present, or just start at '('
    int parsed = sscanf(this->rx_buffer_.c_str(), "(%f %f %f %f %f %f %f %8s", 
                        &ip_v, &ip_f_v, &op_v, &op_c, &op_f, &bat_v, &temp, bits);
    
    // Some responses have a leading space after '('
    if (parsed != 8) {
        parsed = sscanf(this->rx_buffer_.c_str(), "( %f %f %f %f %f %f %f %8s", 
                            &ip_v, &ip_f_v, &op_v, &op_c, &op_f, &bat_v, &temp, bits);
    }

    if (parsed == 8) {
      if (this->ip_voltage_sensor_) this->ip_voltage_sensor_->publish_state(ip_v);
      if (this->ip_fault_voltage_sensor_) this->ip_fault_voltage_sensor_->publish_state(ip_f_v);
      if (this->op_voltage_sensor_) this->op_voltage_sensor_->publish_state(op_v);
      if (this->op_current_sensor_) this->op_current_sensor_->publish_state(op_c);
      if (this->op_frequency_sensor_) this->op_frequency_sensor_->publish_state(op_f);
      if (this->battery_voltage_sensor_) this->battery_voltage_sensor_->publish_state(bat_v);
      if (this->temperature_sensor_) this->temperature_sensor_->publish_state(temp);
      
      if (this->utility_fail_binary_sensor_) this->utility_fail_binary_sensor_->publish_state(bits[0] == '1');
      if (this->battery_low_binary_sensor_) this->battery_low_binary_sensor_->publish_state(bits[1] == '1');
      if (this->avr_active_binary_sensor_) this->avr_active_binary_sensor_->publish_state(bits[2] == '1');
      if (this->ups_failed_binary_sensor_) this->ups_failed_binary_sensor_->publish_state(bits[3] == '1');
      if (this->line_interactive_binary_sensor_) this->line_interactive_binary_sensor_->publish_state(bits[4] == '1');
      if (this->test_progress_binary_sensor_) this->test_progress_binary_sensor_->publish_state(bits[5] == '1');
      if (this->shutdown_active_binary_sensor_) this->shutdown_active_binary_sensor_->publish_state(bits[6] == '1');
      if (this->beeper_on_binary_sensor_) this->beeper_on_binary_sensor_->publish_state(bits[7] == '1');
    }
  }
}

void SunGoldPowerLFP::dump_config() {
  ESP_LOGCONFIG(TAG, "SunGoldPowerLFP:");
  LOG_UPDATE_INTERVAL(this);
}

}  // namespace sungoldpower_lfp
}  // namespace esphome
