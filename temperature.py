class ProcessorOverheat(Exception):
    """ Cpu_temp exceeded 85C """

    def __init__(self, msg):
        super().__init__(msg)
