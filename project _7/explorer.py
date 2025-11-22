def explore_module(module_name):
    """Returns attributes of a module."""
    try:
        module = __import__(module_name)
        return [attr for attr in dir(module) if not attr.startswith("_")]
    except ModuleNotFoundError:
        return None
