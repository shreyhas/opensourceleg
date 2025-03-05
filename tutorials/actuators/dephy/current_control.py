import time

from opensourceleg.actuators.dephy import DephyActuator
from opensourceleg.actuators.base import CONTROL_MODES
from opensourceleg.logging.logger import Logger
from opensourceleg.time import SoftRealtimeLoop

TIME_TO_STEP = 1.0
FREQUENCY = 1000
DT = 1 / FREQUENCY

def current_control():
    current_logger = Logger(
        log_path="./logs",
        file_name="current_control",
    )
    actpack = DephyActuator(
        port="/dev/ttyACM0",
        gear_ratio=9.0,
        frequency=FREQUENCY,
        debug_level=0,
        dephy_log=False

    )
    clock = SoftRealtimeLoop(dt=DT)

    with actpack:
        actpack.set_control_mode(mode=CONTROL_MODES.CURRENT)
        actpack.set_current_gains()

        command_current = 0

        current_logger.track_variable(lambda: actpack.motor_current, "Motor Current")
        current_logger.track_variable(lambda: command_current, "Command Current")

        for t in clock:
            if t > TIME_TO_STEP:
                command_current = 500
                actpack.set_motor_current(value=command_current)  # in mA

            actpack.update()

            current_logger.info(f"Time: {t}; \
                                Command Current: {command_current}; \
                                Motor Current: {actpack.motor_current}")
            current_logger.update()


if __name__ == "__main__":
    current_control()
