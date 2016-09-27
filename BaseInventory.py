
class BaseInventory:
    def __init__(self):
        pass

    def getContext(self):
        pass

    def module_switch_in(self, module):
        context = module.getContext()

    def module_switch_out(self, module):
        pass