from intermediate.robot import Robot, CleaningRobot


class MockBot(Robot):
    """"""
    # """Simulate a real robot by simply recording the tasks"""
    def __init__(self):
        self.tasks = []

    def fetch(self, tool):
        self.tasks.append(f"fetching {tool}.")

    def move_forward(self, tool):
        self.tasks.append(f"forward {tool}.")

    def move_backward(self, tool):
        self.tasks.append(f"backward {tool}.")

    def replace(self, tool):
        self.tasks.append(f"replace {tool}.")


class MockedCleaningRobot(CleaningRobot, MockBot):
    """"""
    """Inject mock bot into the robot dependency"""
    # def __init__(self):
    #     super().__init__()

# help(MockedCleaningRobot)
def test_bot():
    tbot = MockedCleaningRobot()
    tbot.clean('mop')

    tasks = (['fetching mop.'] +
             ['forward mop.', 'backward mop.'] * 10 +
             ['replace mop.'])
    assert tbot.tasks == tasks