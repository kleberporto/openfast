def modify_simulation_file(file_lines):
    file_lines[5] = "        60   TMax            - Total run time (s)"
    return file_lines
