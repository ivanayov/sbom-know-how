*************************
SBOM Transformation Tools
*************************


.. _apkot:

apko
####

`apko <https://github.com/chainguard-dev/apko>`_ produces SBOM documents and provides an `SBOM composition <https://github.com/chainguard-dev/apko/blob/main/docs/sbom-composition.md>`_ functionality

.. tool-data:: CDX2SPDX
    :id: TOOL27
    :tool: CDX2SPDX
    :generation: no
    :consumption: no
    :transformation: yes
    :cyclonedx: yes
    :spdx: yes


CDX2SPDX
########

`CDX2SPDX <https://github.com/spdx/cdx2spdx>`_ is a Java tool that converts :doc:`../specs/cyclonedx.rst` SBOMs to :doc:`../specs/spdx.rst`.

.. tool-data:: DaggerBoard
    :id: TOOL28
    :tool: DaggerBoard
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes
    :vulnerabilty_scanning: yes


SBOM Composer
#############

`SBOM Composer <https://github.com/vmware-samples/sbom-composer>`_ is a tool that serves for composing :doc:`../specs/spdx.rst` SBOM files into a single SPDX document. Not restricted by the contents of the composable SBOMs, as long as they are valid SPDX. The version of the final document is the latest amongst all composed.

.. tool-data:: DaggerBoard
    :id: TOOL29
    :tool: DaggerBoard
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes
    :vulnerabilty_scanning: yes


Tejolote
########

`Tejolote <https://github.com/puerco/tejolote>`_ is a tool that consumes SBOMs and generates `SLSA <https://slsa.dev/>`_ provenance attestations about build runs.