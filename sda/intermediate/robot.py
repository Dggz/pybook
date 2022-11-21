class Robot:
    '''Class that moves a real robot'''
    """Don't wear out the real robot by running tests!"""
    def fetch(self, tool):
        print("Robot moving! Fetching tool.")
    def move_forward(self, tool):
        print("Robot moving! Moving forward.")
    def move_backward(self, tool):
        print("Robot moving! Moving backward.")
    def replace(self, tool):
        print("Robot moving! Returning tool.")


class CleaningRobot(Robot):
    """"""
    """Custom robot that has a cleaning routine"""
    def clean(self, tool, times=10):
        super().fetch(tool)
        for i in range(times):
            super().move_forward(tool)
            super().move_backward(tool)
        super().replace(tool)

if __name__ == '__main__':
    roomba = CleaningRobot()
    roomba.clean('broom')