"""Helpers that can be used for callback."""


class InterruptHandler:
    """Intercept force-quiting of the app.

    To use::

        from he.handlers import InterruptHandler
        INTERRUPT_HANDLER = InterruptHandler()
        signal.signal(signal.SIGINT, INTERRUPT_HANDLER.signal_handler)
        signal.signal(signal.SIGTERM, INTERRUPT_HANDLER.signal_handler)


    Elsewhere::

        while True:
            # task
            if INTERRUPT_HANDLER.interrupted:
                break


    Inspiration: https://stackoverflow.com/a/43787607/4257312
    """

    def __init__(self) -> None:  # pylint: disable=missing-docstring
        self.interrupted = False

    # `frame` could be another parameter here
    def signal_handler(self, signal: int) -> None:  # pylint: disable=missing-docstring
        print(f'Signal {signal} has been caught. Interrupting...')
        self.interrupted = True
