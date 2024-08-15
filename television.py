class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """

        Initialize the Television with default settings.

        """
        self.__muted = False
        self.__status = False

        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL


    def power(self) -> None:
        """

        Toggle the power status of the television.
        :return: Power status

        """
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def mute(self) -> None:
        """

        Toggle the mute status of the television if it is powered on.
        :return: Mute status

        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """

        Increase the channel by 1, wrapping around if at the maximum channel.
        :return: Channel number up by 1

        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            elif self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def channel_down(self) -> None:
        """

        Decrease the channel by 1, wrapping around if at the minimum channel.
        :return: Channel number down by 1

        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            elif self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """

        Increase the volume by 1 if the television is powered on, and unmute if muted.
        :return: Volume number up by 1

        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """

        Decrease the volume by 1 if the television is powered on, and unmute if muted.
        :return: Volume number down by 1

        """

        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """

        Return a string representation of the television's current status.
        :return: String of the power, channel, and volume status

        """

        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
