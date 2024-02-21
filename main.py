from pathlib import Path

from energyplus.api import EnergyPlusAPI


def progress_update(percent):
    filled_length = int(80 * (percent / 100.0))
    bar = "*" * filled_length + '-' * (80 - filled_length)
    print(f'\rProgress: |{bar}| {percent}%', end="")


this_file = Path(__file__).resolve()
api = EnergyPlusAPI()
state = api.state_manager.new_state()
api.runtime.set_console_output_status(state, False)
api.runtime.callback_progress(state, progress_update)
result = api.runtime.run_energyplus(
    state,
    [
        '-d',
        str(this_file.parent / 'energyplus_outputs'),
        '-w',
        str(this_file.parent / 'resources' / 'chicago.epw'),
        "-a",
        str(this_file.parent / 'resources' / '5ZoneAirCooled.idf')
    ]
)
