*********************
SBOM Generation Tools
*********************

.. tool-data:: apko
    :id: TOOL1
    :tool: apko
    :generation: yes
    :consumption: no
    :transformation: yes
    :cyclonedx: yes
    :spdx: yes


.. _apko:

apko
####

`apko <https://github.com/chainguard-dev/apko>`_ provides SBOM support by producing SBOM documents for OCI images.


.. tool-data:: CycloneDX Tool Center
    :id: TOOL2
    :tool: CycloneDX Tool Center
    :generation: yes
    :consumption: no
    :transformation: no
    :cyclonedx: yes
    :spdx: no


.. _cdxtc:

CycloneDX Tool Center
#####################

Generates CycloneDX format SBOMs. Full list of tools can be found in the `CycloneDX Tool Center <https://cyclonedx.org/tool-center/>`_.


.. tool-data:: Docker SBOM
    :id: TOOL3
    :tool: Docker SBOM
    :generation: yes
    :consumption: no
    :transformation: no
    :cyclonedx: yes
    :spdx: no


.. _dockersbom:

Docker SBOM
###########

Generates SBOMs for Docker images with the currently experimental :command:`docker sbom` command. Based on :ref:`Syft <syft>`. For more detail, please visit the `Docker SBOM Documentation <https://docs.docker.com/engine/sbom/>`_.


.. tool-data:: FatBOM
    :id: TOOL4
    :tool: FatBOM
    :generation: yes
    :consumption: no
    :transformation: yes
    :cyclonedx: no
    :spdx: yes


.. _fatbom:

FatBOM
######

FatBOM generates SBOMs via :ref:`Syft <syft>`, :ref:`Salus <salus>`, :ref:`SPDX SBOM Generator <spdxsbomgen>` and :ref:`K8s BOM <k8sbom>` and composes them into a single SPDX SBOM in JSON format. Full details can be found in the `FatBOM GitHub repository <https://github.com/sbs2001/fatbom>`_.


.. tool-data:: KubeClarity
    :id: TOOL5
    :tool: KubeClarity
    :generation: yes
    :consumption: yes
    :transformation: no
    :cyclonedx: yes
    :spdx: yes


.. _kubeclarity:

KubeClarity
###########

`KubeClarity <https://github.com/openclarity/kubeclarity>`_ uses :ref:`Syft <syft>` and `Cyclonedx-gomod <https://github.com/CycloneDX/cyclonedx-gomod>`_ (:ref:`CycloneDX Tool Center <cdxtc>`) to generate SBOMs and offers [SBOM scanning](consumption_tools.md#kubeclarity).


.. tool-data:: K8s BOM
    :id: TOOL6
    :tool: K8s BOM
    :generation: yes
    :consumption: yes
    :transformation: no
    :cyclonedx: no
    :spdx: yes


.. _k8sbom:

K8s BOM
#######


`K8s BOM <https://github.com/kubernetes-sigs/bom>`_ generates SBOMs from files, images, and docker archives and supports pulling images from remote registries. The SBоM data can be exported to an `in-toto <https://in-toto.io>`_ provenance attestation. For SBOM scanning details, please see the [K8s BOM consumption tools](consumption_tools.md#k8s-bom) section.


.. tool-data:: OSS Review Toolkit
    :id: TOOL7
    :tool: OSS Review Toolkit
    :generation: yes
    :consumption: yes
    :transformation: no
    :cyclonedx: yes
    :spdx: yes

.. _ort:

OSS Review Toolkit
##################

The `OSS Review Toolkit <https://github.com/oss-review-toolkit/ort>`_'s `Reporter <https://github.com/oss-review-toolkit/ort/blob/main/README.md#reporter>`_ generates SBOMs in [CycloneDX](../specs/cyclonedx.md) or [SPDX](../specs/spdx.md) format.


.. tool-data:: Pkgconf bomtool
    :id: TOOL8
    :tool: Pkgconf bomtool
    :generation: yes
    :consumption: no
    :transformation: no
    :cyclonedx: no
    :spdx: yes

.. _bomtool:

Pkgconf bomtool
###############

Bomtool is a feature of `pkgconf <http://pkgconf.org>`_ and can be used for generating SBOMs for C/C++ packages under Alpine. Usage:
```bash
$ bomtool <package_name>
```
where package name should be linked in `pkgconf`.


.. tool-data:: Salus
    :id: TOOL9
    :tool: Salus
    :generation: yes
    :consumption: no
    :transformation: no
    :cyclonedx: no
    :spdx: yes

.. _salus:

Salus
#####

`Salus <https://github.com/microsoft/sbom-tool>`_ is an Open Source SBOM generation tool implemented by Microsoft. It allows build-time generation from source and packages, as well as `CI/CD pipelines integration <https://github.com/microsoft/sbom-tool#integrating-sbom-tool-to-your-cicd-pipelines>`_ via `GitHub Actions <https://github.com/microsoft/sbom-tool/blob/main/docs/setting-up-github-actions.md>`_ and `Azure DevOps Pipelines <https://github.com/microsoft/sbom-tool/blob/main/docs/setting-up-ado-pipelines.md>`_.


.. tool-data:: SBOM Operator
    :id: TOOL10
    :tool: SBOM Operator
    :generation: yes
    :consumption: no
    :transformation: no
    :cyclonedx: yes
    :spdx: yes

.. _sbomoperator:

SBOM Operator
#############

`SBOM Operator <https://github.com/ckotzbauer/sbom-operator>`_ uses :ref:`Syft <syft>` to generate SBOMs from each image deployed in a Kubernetes cluster. Relies on `go-containeregistry <https://github.com/google/go-containerregistry>`_ for downloading images. Allows [analysis](consumption_tools.md#sbom-operator).


.. tool-data:: ScanCode
    :id: TOOL11
    :tool: ScanCode
    :generation: yes
    :consumption: yes
    :transformation: no
    :cyclonedx: yes
    :spdx: yes

.. _scancode:

ScanCode
########

`ScanCode <https://github.com/nexB/scancode-toolkit>`_ is an OSS tool from `AboutCode <https://www.aboutcode.org/>`_ that generates SBOMs for containers, system packages, and many language packages. Supports both [SPDX](../specs/spdx.md) and [CycloneDX](../specs/cyclonedx.md). It's embedded in :ref:`ORT <ort>`, :ref:`Tern <tern>`, [FOSSology](consumption_tools.md#fossology), Fosslight, Barista, Philips software license-scanner, and others.
It provides a ScanCode.io (CLI, web UI and REST API) to read and write SPDX and CycloneDX.


.. tool-data:: SPDX SBOM Generator
    :id: TOOL12
    :tool: SPDX SBOM Generator
    :generation: yes
    :consumption: no
    :transformation: no
    :cyclonedx: no
    :spdx: yes

.. _spdxsbomgen:

SPDX SBOM Generator
###################

The `SPDX SBOM Generator <https://github.com/opensbom-generator/spdx-sbom-generator>`_ generates SBOMs from source code. The supported package managers can be found the the tool `Overview <https://github.com/opensbom-generator/spdx-sbom-generator#overview>`_.

.. tool-data:: Syft
    :id: TOOL13
    :tool: Syft
    :generation: yes
    :consumption: no
    :transformation: no
    :cyclonedx: yes
    :spdx: yes

.. _syft:

Syft
####

`Syft <https://github.com/anchore/syft>`_ generates SBOMs from container images and file systems. It provides both a CLI tool and a Go library. Supported ecosystems are available in the tool `documentation <https://github.com/anchore/syft#supported-ecosystems>`_.

.. tool-data:: Syft
    :id: TOOL14
    :tool: Syft
    :generation: yes
    :consumption: no
    :transformation: no
    :cyclonedx: yes
    :spdx: yes

.. _tern:

Tern
####

`Tern <https://github.com/tern-tools/tern>`_ is a software package inspection tool that generates SBOMs for container images and Dockerfiles. Supports both [SPDX](../specs/spdx.md) and [CycloneDX](../specs/cyclonedx.md), [SWID](../specs/swid.md).