def turbsim_binary_bladed_style_full_field(file_lines, random_seed1, random_seed2, wind_speed):
    file_lines[4] = f"{random_seed1}   RandSeed1       - First random seed  (-2147483648 to 2147483647)"
    file_lines[5] = f"{random_seed2}   RandSeed2       - Second random seed (-2147483648 to 2147483647) for " \
                    f"intrinsic pRNG, or an alternative pRNG: \"RanLux\" or \"RNSNLW\""
    file_lines[22] = f"        600   UsableTime      - Usable length of output time series [seconds] " \
                     f"(program will add GridWidth/MeanHHWS seconds unless UsableTime is \"ALL\")"
    file_lines[
        39] = f"      {wind_speed}   URef            - Mean (total) velocity at the reference height [m/s] " \
              f"(or \"default\" for JET velocity profile) [must be 1-hr mean for API model; otherwise is " \
              f"the mean over AnalysisTime seconds]"

    return file_lines
