from openff.toolkit.utils.toolkits import (
    GLOBAL_TOOLKIT_REGISTRY,
    AmberToolsToolkitWrapper,
    RDKitToolkitWrapper,
)

assert RDKitToolkitWrapper().is_available()
assert AmberToolsToolkitWrapper().is_available()


print(GLOBAL_TOOLKIT_REGISTRY.registered_toolkit_versions)

from openff.toolkit import Molecule, Topology, ForceField
offmol = Molecule.from_smiles('CCO')
Molecule.from_rdkit(offmol.to_rdkit())
ff = ForceField('openff-1.0.0.offxml')
# Un-comment once Interchange builds are accessible at test time
# ff.create_openmm_system(offmol.to_topology())
