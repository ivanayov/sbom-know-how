**********************
SBOM Consumption Tools
**********************

.. tool-data:: Bomber
    :id: TOOL15
    :tool: Bomber
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes
    :vulnerabilty_scanning: yes


.. _bomber:

Bomber
######

`Bomber <https://github.com/devops-kung-fu/bomber>`_ is an application that scans SBOMs for security vulnerabilities. Works with :doc:`../specs/cyclonedx.rst` JSON and XML, as well as :doc:`../specs/spdx.rst` and :ref:`Syft <syft>` JSON. 


.. tool-data:: DaggerBoard
    :id: TOOL16
    :tool: DaggerBoard
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes
    :vulnerabilty_scanning: yes


.. _daggerboard:

DaggerBoard
###########

`DaggerBoard <https://github.com/nyph-infosec/daggerboard>`_ is a vulnerability scanning tool, based on ingesting SBOM files (CycloneDX,SPDX), that outputs results in a human-readable format.


.. tool-data:: Dependency-Track
    :id: TOOL17
    :tool: Dependency-Track
    :consumption: yes
    :cyclonedx: yes
    :vulnerabilty_scanning: yes
    :licensing: yes


.. _dependencytrack:

Dependency-Track
################

`Dependency-Track <https://github.com/DependencyTrack/dependency-track> `_ uses :doc:`../specs/cyclonedx.rst` SBOMs to monitor component usage across all versions of the application in its portfolio, in order to identify and reduce risk in the software supply chain.


.. tool-data:: SBOM Scorecard
    :id: TOOL18
    :tool: SBOM Scorecard
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes
    :sbom_quality: yes


.. _sbomscorecard:

SBOM Scorecard
##############

`SBOM Scorecard <https://github.com/eBay/sbom-scorecard>`_ is a tool for providing metrics for SBOM quality, including spec compliance, generation information and package ids, licensed and version.

.. tool-data:: FOSSology
    :id: TOOL19
    :tool: FOSSology
    :consumption: yes
    :spdx: yes
    :licensing: yes


.. _fossology:

FOSSology
#########

FOSSology is a compliance scanner tool for license, copyright and export control. Documentation can be found on the `official web site <https://www.fossology.org>`_.


.. tool-data:: Grype
    :id: TOOL20
    :tool: Grype
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes
    :vulnerabilty_scanning: yes


.. _grype:

Grype
#####

`Grype <https://github.com/anchore/grype>`_ is a vulnerability scanner for container images and file systems. If scans for vulnerabilities for both operating system and language-specific packages. Supports Docker, OCI and Singularity image formats, as well as consumes SBOM attestations.


.. tool-data:: Hoppr Cop
    :id: TOOL21
    :tool: Hoppr Cop
    :consumption: yes
    :cyclonedx: yes
    :vulnerabilty_scanning: yes


.. _hopprcop:

Hoppr Cop
#########

`Hoppr Cop <https://github.com/lmco/hoppr-cop>`_ generates vulnerability information from CycloneDX SBOMs. It's available both as a CLI and a python library.


.. _kubeclarityc:

KubeClarity
###########

KubeClarity detects and manages SBOMs and vulnerabilities of container images and file systems. It can also scan K8s runtime to detect vulnerabilities discovered post-deployment. It uses `Grype <https://github.com/anchore/grype>`_ and `Dependency-Track <https://github.com/DependencyTrack/dependency-track>`_ for vulnerability scanning. More detail can be found in the `KubeClarity documentation <https://github.com/openclarity/kubeclarity>`_.


.. _k8sbomc:

K8s BOM
#######

`K8s BOM <https://github.com/kubernetes-sigs/bom>`_ offers drawing a structure of an SPDX document and serves for verification.


.. _ortc:

OSS Review Toolkit
##################

The `OSS Review Toolkit <https://github.com/oss-review-toolkit/ort>`_ provides a list of tools, including `Analyzer <https://github.com/oss-review-toolkit/ort#analyzer>`_ for dependencies of projects and their metadata, `Downloader <https://github.com/oss-review-toolkit/ort#downloader>`_ for fetching source code and dependencies, `Scanner <https://github.com/oss-review-toolkit/ort#scanner>`_ for detecting license / copyright findings from source code, `Advisor <https://github.com/oss-review-toolkit/ort#advisor>`_ for retrieving security advisories for used dependencies, and others.



.. tool-data:: SBOM Diff Action
    :id: TOOL22
    :tool: SBOM Diff Action
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes


.. _sbomdiffaction:

SBOM Diff Action
################

`SBOM Diff Action <https://github.com/ckotzbauer/sbom-diff-action>`_ is a GitHub integration tool that creates diffs for SBOMs from PR changes.


.. _sbomoperatorc:

SBOM Operator
#############

The SBOM Operator allows checks for changed images and pods within a cluster. Provides vulnerability scans via the :ref:`Vulnerability Operator <vulnop>`. For more detail, please refer to the SBOM Operators `Analysis-Trigger section <https://github.com/ckotzbauer/sbom-operator#analysis-trigger>`_.


.. tool-data:: SBOM Utility
    :id: TOOL23
    :tool: SBOM Utility
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes
    :sbom_quality: yes


.. _sbomutility:

SBOM Utility
############

`SBOM Utility <https://github.com/mrutkows/sbom-utility>`_ is a CycloneDX and SPDX SBOM validation tool.


.. tool-data:: ScanCode.io
    :id: TOOL24
    :tool: ScanCode.io
    :generation: yes
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes
    :vulnerabilty_scanning: yes
    :licensing: yes


.. _scancodeio:

ScanCode.io
###########

`ScanCode.io <https://nexb.github.io/scancode.io-homepage/>`_ is a CLI, web UI and REST API that can read and write :doc:`../specs/spdx.rst` and :doc:`../specs/cyclonedx.rst`. It embeds `scancode-toolkit <https://github.com/nexB/scancode-toolkit>`_ and can scan for origin, vulnerabilities and license a large range of codebase including first class support for Linux containers and docker images, VM Images, Windows containers, Windows VM images as well as packages and codebase with pre-defined configurable pipelines. It detects all archives, installed and embedded formats for packages from Maven, Pypi, Ruby, Rust cargo, Go, NuGet, Alpine, Debian and derivative, RPM distributions, Windows, npm and yarn, Bower, Chef, Cocoapods, conda, cran, haxe, MSI, opam, pubspec.
Both ScanCode toolkit and ScanCode.io are extensively based on and use :doc:`../specs/purl.rst`.


.. tool-data:: Trivy
    :id: TOOL25
    :tool: Trivy
    :generation: yes
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes
    :vulnerabilty_scanning: yes
    :licensing: yes


.. _trivy:

Trivy
#####

`Trivy <https://github.com/aquasecurity/trivy>`_ scans container images, file systems, Git repositories, and Kubernetes clusters or resources for open source packages and dependencies, CVEs, IaC misconfigurations, and sensitive information. It generates SBOMs in the scanning process.
Trivy also allows signing and verifying `SBOM attestations <https://aquasecurity.github.io/trivy/v0.34/docs/attestation/sbom/>`_.


.. tool-data:: Vulnerability Operator
    :id: TOOL26
    :tool: Vulnerability Operator
    :consumption: yes
    :cyclonedx: yes
    :spdx: yes
    :vulnerabilty_scanning: yes


.. _vulnop:

Vulnerability Operator
######################

The `vulnerability-operator <https://github.com/ckotzbauer/vulnerability-operator>`_ uses `Grype <https://github.com/anchore/grype>`_ for scanning SBOMs and exports all found vulnerabilities into a JSON format.