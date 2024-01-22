"""Adapters for Waveshare boards."""
from typing import ClassVar, Optional

from app.adapters.gpio_devices import Relay


class WaveshareRpiRelayBoardAdapter:
    """Adapter for RPi Relay Board from Waveshare.

    The Board carries three relays which are connected to GPIO pins.
    https://www.waveshare.com/rpi-relay-board.htm
    https://www.waveshare.com/wiki/RPi_Relay_Board
    """

    relay_position_mapping: ClassVar[dict] = {
        1: 0,
        2: 1,
        3: 2,
    }

    def __init__(self, relays: Optional[list[Relay]] = None):
        """Initializer.

        :param list[Relay] relays:
        """
        if relays is None:
            relays = [Relay(26), Relay(20), Relay(21)]

        self.relays: list[Relay] = relays

    def on(self, relay_position: int):
        """Turns relay at relay_position on.

        :param int relay_position:
        :return:
        """
        if relay_position not in self.relay_position_mapping.keys():
            raise ValueError("Invalid relay position")

        relay: Relay = self.relays[self.relay_position_mapping[relay_position]]
        relay.on()

    def off(self, relay_position: int):
        """Turns relay at relay_position off.

        :param int relay_position:
        :return:
        """
        if relay_position not in self.relay_position_mapping.keys():
            raise ValueError("Invalid relay position")

        relay: Relay = self.relays[self.relay_position_mapping[relay_position]]
        relay.off()
