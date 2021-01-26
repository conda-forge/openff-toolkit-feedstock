from openff.toolkit.utils.toolkits import AmberToolsToolkitWrapper, RDKitToolkitWrapper

assert RDKitToolkitWrapper().is_available()
assert AmberToolsToolkitWrapper().is_available()
