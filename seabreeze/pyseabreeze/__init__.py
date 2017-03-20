"""This is a wrapper for the pyusb-implementation of the seabreeze-library

"""

from .wrapper import (SeaBreezeError,
                      SeaBreezeDevice,
                      initialize,
                      shutdown,
                      device_list_devices,
                      device_open,
                      device_is_open,
                      device_close,
                      device_get_model,
                      device_get_serial_number,
                      device_get_spectrometer_feature_id,
                      device_get_shutter_feature_id,
                      device_get_light_source_feature_id,
                      device_get_continuous_strobe_feature_id,
                      device_get_eeprom_feature_id,
                      device_get_irrad_calibration_feature_id,
                      device_get_tec_feature_id,
                      device_get_lamp_feature_id,
                      device_get_nonlinearity_coeffs_feature_id,
                      device_get_stray_light_coeffs_feature_id,
                      spectrometer_set_trigger_mode,
                      spectrometer_set_integration_time_micros,
                      spectrometer_get_minimum_integration_time_micros,
                      spectrometer_get_formatted_spectrum_length,
                      spectrometer_get_formatted_spectrum,
                      spectrometer_get_unformatted_spectrum_length,
                      spectrometer_get_unformatted_spectrum,
                      spectrometer_get_wavelengths,
                      spectrometer_get_electric_dark_pixel_indices,
                      shutter_set_shutter_open,
                      light_source_get_count,
                      light_source_has_enable,
                      light_source_is_enabled,
                      light_source_set_enable,
                      light_source_has_variable_intensity,
                      light_source_get_intensity,
                      light_source_set_intensity,
                      continuous_strobe_set_enable,
                      continuous_strobe_set_period_micros,
                      eeprom_read_slot,
                      irrad_calibration_read,
                      irrad_calibration_write,
                      irrad_calibration_has_collection_area,
                      irrad_calibration_read_collection_area,
                      irrad_calibration_write_collection_area,
                      tec_read_temperature_degrees_C,
                      tec_set_temperature_setpoint_degrees_C,
                      tec_set_enable,
                      lamp_set_lamp_enable,
                      nonlinearity_coeffs_get,
                      stray_light_coeffs_get,
                      device_get_spectrum_processing_feature_id,
                      spectrum_processing_set_boxcar_width,
                      spectrum_processing_set_scans_to_average,
                      spectrum_processing_get_boxcar_width,
                      spectrum_processing_get_scans_to_average)
