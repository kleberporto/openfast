import random
import shutil
import subprocess
import calendar
import time

from automation_openfast.file_modification import modify_simulation_file
from automation_openfast.inflow_wind_types import modify_inflow_wind_binary_bladed_style
from automation_openfast.openfast_helpers import remove_extension
from automation_openfast.turbsim_wind_types import turbsim_binary_bladed_style_full_field
from automation_openfast.openfast_helpers import delete_files


class Openfast_Simulation:
    """
    """

    def __init__(self,
                 openfast_model_file_path,
                 turbsim_model_file_path,
                 inflow_wind_file_path,
                 wind_type,
                 wind_speed_range):
        self.openfast_model_file_path = openfast_model_file_path
        self.turbsim_model_file_path = turbsim_model_file_path
        self.inflow_wind_model_file_path = inflow_wind_file_path
        self.wind_type = wind_type
        self.wind_speed_range = wind_speed_range
        self.simulation_input_file = None
        self.turbsim_simulation_file = None
        self.simulation_time_stamp = calendar.timegm(time.gmtime())
        self.simulation_input_file_no_extension = None

    def define_simulation_file_name(self, model_file, extension):
        """

        :return: The unique ID for the simulation
        """
        model_file_no_extension = remove_extension(model_file)
        return f"{model_file_no_extension}-{self.simulation_time_stamp}.{extension}"

    def modify_turbsim_file(self):
        """

        :return:
        """
        shutil.copyfile(self.turbsim_model_file_path, self.turbsim_simulation_file)

        wind_speed = round(random.uniform(self.wind_speed_range[0], self.wind_speed_range[1]), 2)
        random_seed1 = random.randint(-2147483648, 2147483648)
        random_seed2 = random.randint(-2147483648, 2147483648)
        if self.wind_type == 4:
            with open(self.turbsim_simulation_file, 'r') as reading_file:
                lines = reading_file.read().splitlines()
                modified_lines = turbsim_binary_bladed_style_full_field(lines, random_seed1, random_seed2, wind_speed)
                with open(self.turbsim_simulation_file, 'w') as writing_lines:
                    writing_lines.write('\n'.join(modified_lines))

    def openfast_input(self):
        """

        :return:
        """
        shutil.copyfile(self.openfast_model_file_path, self.simulation_input_file)
        with open(self.simulation_input_file, "r") as reading_file:
            lines = reading_file.read().splitlines()
            modified_lines = modify_simulation_file(lines)
            with open(self.simulation_input_file, "w") as writing_file:
                writing_file.write('\n'.join(modified_lines))

    def inflow_wind(self):
        """

        :return:
        """
        with open(self.inflow_wind_model_file_path, 'r') as reading_file:
            lines = reading_file.read().splitlines()
            if self.wind_type == 4:
                modified_lines = modify_inflow_wind_binary_bladed_style(lines,
                                                                        self.turbsim_model_file_path,
                                                                        self.simulation_time_stamp)
            with open(self.inflow_wind_model_file_path, 'w') as writing_file:
                writing_file.write('\n'.join(modified_lines))

    def __enter__(self):
        fst_extension = "fst"
        self.turbsim_simulation_file = self.define_simulation_file_name(self.turbsim_model_file_path, "inp")
        self.simulation_input_file = f"{remove_extension(self.openfast_model_file_path)}/" \
                                     f"{self.define_simulation_file_name(self.openfast_model_file_path, fst_extension)}"
        self.modify_turbsim_file()
        self.openfast_input()
        self.inflow_wind()
        return self

    def __exit__(self, type, value, traceback):
        self.simulation_input_file_no_extension = remove_extension(self.simulation_input_file)
        delete_files(self.simulation_input_file)
        delete_files(f"{self.simulation_input_file_no_extension}.AD.sum")
        delete_files(f"{self.simulation_input_file_no_extension}.ED.sum")
        delete_files(f"{self.simulation_input_file_no_extension}.sum")
        delete_files(f"{self.simulation_input_file_no_extension}.UA.sum")
        delete_files(f"{self.simulation_input_file_no_extension}.SrvD.sum")
        delete_files(self.turbsim_simulation_file)
        delete_files(f"{remove_extension(self.turbsim_simulation_file)}.wnd")
        delete_files(f"{remove_extension(self.turbsim_simulation_file)}.sum")

    def run(self):
        self.__enter__()
        subprocess.run(["turbsim", self.turbsim_simulation_file])
        subprocess.run(["openfast", self.simulation_input_file])
        self.__exit__(None, None, None)
