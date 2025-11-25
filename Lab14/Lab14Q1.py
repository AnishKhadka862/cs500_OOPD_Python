from __future__ import annotations
from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


# Light class
class Light:
    def on(self) -> None:
        print("Light is ON")

    def off(self) -> None:
        print("Light is OFF")


# Fan class
class Fan:
    def start(self) -> None:
        print("Fan started")

    def stop(self) -> None:
        print("Fan stopped")


# LightOnCommand
class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.on()


# LightOffCommand
class LightOffCommand(Command):
    def __init__(self, light: Light) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.off()


# FanStartCommand
class FanStartCommand(Command):
    def __init__(self, fan: Fan) -> None:
        self._fan = fan

    def execute(self) -> None:
        self._fan.start()


# FanStopCommand
class FanStopCommand(Command):
    def __init__(self, fan: Fan) -> None:
        self._fan = fan

    def execute(self) -> None:
        self._fan.stop()


# RemoteControl class
class RemoteControl:
    def __init__(self) -> None:
        self.lightOnCommand: Command | None = None
        self.lightOffCommand: Command | None = None
        self.fanStartCommand: Command | None = None
        self.fanStopCommand: Command | None = None

    def setCommand(
        self,
        light_on: Command,
        light_off: Command,
        fan_start: Command,
        fan_stop: Command,
    ) -> None:
        self.lightOnCommand = light_on
        self.lightOffCommand = light_off
        self.fanStartCommand = fan_start
        self.fanStopCommand = fan_stop

    def lightOnButtonPressed(self) -> None:
        if self.lightOnCommand:
            self.lightOnCommand.execute()

    def lightOffButtonPressed(self) -> None:
        if self.lightOffCommand:
            self.lightOffCommand.execute()

    def fanStartButtonPressed(self) -> None:
        if self.fanStartCommand:
            self.fanStartCommand.execute()

    def fanStopButtonPressed(self) -> None:
        if self.fanStopCommand:
            self.fanStopCommand.execute()


# Demo / main
def main():
    # Receivers
    light = Light()
    fan = Fan()

    # Commands
    light_on_cmd = LightOnCommand(light)
    light_off_cmd = LightOffCommand(light)
    fan_start_cmd = FanStartCommand(fan)
    fan_stop_cmd = FanStopCommand(fan)

    # Invoker
    remote = RemoteControl()
    remote.setCommand(light_on_cmd, light_off_cmd, fan_start_cmd, fan_stop_cmd)

    # Simulate button presses
    remote.lightOnButtonPressed()      # Light is ON
    remote.lightOffButtonPressed()     # Light is OFF
    remote.fanStartButtonPressed()     # Fan started
    remote.fanStopButtonPressed()      # Fan stopped


if __name__ == "__main__":
    main()
