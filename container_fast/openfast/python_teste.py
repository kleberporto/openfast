from automation_openfast.simulation import Openfast_Simulation


def main():
    wind_turbine_input_file = "1.5MW.fst"
    turbsim_input_file = "1.5_MW_Modules/Wind/wind_model.inp"
    inflow_wind_file = "1.5_MW_Modules/WP_Baseline_InflowWind_12mps.dat"
    turbsim_wind_type = 4
    wind_speed_range = (5, 15)

    for simulations in range(5):
        with Openfast_Simulation(wind_turbine_input_file,
                                 turbsim_input_file,
                                 inflow_wind_file,
                                 turbsim_wind_type,
                                 wind_speed_range) as simulation:
            simulation.run()


if __name__ == '__main__':
    main()
