# HungerCore exceptions
class HungerCoreError(Exception): pass

class InvalidLevelError(HungerCoreError): pass
class InvalidModeError(HungerCoreError): pass


# Method exceptions
class InvalidMethodError(Exception): pass

class RenamedMethodError(InvalidMethodError): pass
class RemovedMethodError(InvalidMethodError): pass
