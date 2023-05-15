from automation_openfast.openfast_helpers import remove_extension, get_file_name


def modify_inflow_wind_binary_bladed_style(file_lines, turbsim_path, time_stamp):
    turbsim_file = remove_extension(get_file_name(turbsim_path))
    file_lines[22] = f"\"Wind/{turbsim_file}-{time_stamp}\"    FilenameRoot   - " \
                     f"Rootname of the full-field wind file to use (.wnd, .sum)"
    return file_lines
