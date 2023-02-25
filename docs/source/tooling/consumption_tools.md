# SBOM Consumption Tools

## Bomber

[Bomber](https://github.com/devops-kung-fu/bomber) is an application that scans SBOMs for security vulnerabilities. Works with [CycloneDX](../specs/cyclonedx.md) JSON and XML, as well as [SPDX](../specs/spdx.md) and [Syft](generation_tools.md#syft) JSON. 

## DaggerBoard

[DaggerBoard](https://github.com/nyph-infosec/daggerboard) is a vulnerability scanning tool, based on ingesting SBOM files (CycloneDX,SPDX), that outputs results in a human-readable format.

## Dependency-Track

[Dependency-Track](https://github.com/DependencyTrack/dependency-track) uses [CycloneDX](../specs/cyclonedx.md) SBOMs to monitor component usage across all versions of the application in its portfolio, in order to identify and reduce risk in the software supply chain.

## SBOM Scorecard

[SBOM Scorecard](https://github.com/eBay/sbom-scorecard) is a tool for providing metrics for SBOM quality, including spec compliance, generation information and package ids, licensed and version.

## FOSSology

FOSSology is a compliance scanner tool for license, copyright and export control. Documentation can be found on [the official web site](https://www.fossology.org).

## Grype

[Grype](https://github.com/anchore/grype) is a vulnerability scanner for container images and file systems. If scans for vulnerabilities for both operating system and language-specific packages. Supports Docker, OCI and Singularity image formats, as well as consumes SBOM attestations.

## Hoppr Cop

[Hoppr Cop](https://github.com/lmco/hoppr-cop) generates vulnerability information from CycloneDX SBOMs. It's available both as a CLI and a python library.

## KubeClarity

KubeClarity detects and manages SBOMs and vulnerabilities of container images and file systems. It can also scan K8s runtime to detect vulnerabilities discovered post-deployment. It uses [Grype](https://github.com/anchore/grype) and [Dependency-Track](https://github.com/DependencyTrack/dependency-track) for vulnerability scanning. More detail can be found in the [KubeClarity documentation](https://github.com/openclarity/kubeclarity).

## K8s BOM

[K8s BOM](https://github.com/kubernetes-sigs/bom) offers drawing a structure of an SPDX document and serves for verification.

## OSS Review Toolkit

The [OSS Review Toolkit](https://github.com/oss-review-toolkit/ort) provides a list of tools, including [Analyzer](https://github.com/oss-review-toolkit/ort#analyzer) for dependencies of projects and their metadata, [Downloader](https://github.com/oss-review-toolkit/ort#downloader) for fetching source code and dependencies, [Scanner](https://github.com/oss-review-toolkit/ort#scanner) for detecting license / copyright findings from source code, [Advisor](https://github.com/oss-review-toolkit/ort#advisor) for retrieving security advisories for used dependencies, and others.

## SBOM Diff Action

[SBOM Diff Action](https://github.com/ckotzbauer/sbom-diff-action) is a GitHub integration tool that creates diffs for SBOMs from PR changes.

## SBOM Operator

The SBOM Operator allows checks for changed images and pods within a cluster. Provides vulnerability scans via the [Vulnerability Operator](#vulnerability-operator). For more detail, please refer to the SBOM Operators [Analysis-Trigger section](https://github.com/ckotzbauer/sbom-operator#analysis-trigger).

## SBOM Utility

[SBOM Utility](https://github.com/mrutkows/sbom-utility) is a CycloneDX and SPDX SBOM validation tool.

## ScanCode.io

[ScanCode.io](https://nexb.github.io/scancode.io-homepage/) is a CLI, web UI and REST API that can read and write [SPDX](../specs/spdx.md) and [CycloneDX](../specs/cyclonedx.md). It embeds [scancode-toolkit](https://github.com/nexB/scancode-toolkit) and can scan for origin, vulnerabilities and license a large range of codebase including first class support for Linux containers and docker images, VM Images, Windows containers, Windows VM images as well as packages and codebase with pre-defined configurable pipelines. It detects all archives, installed and embedded formats for packages from Maven, Pypi, Ruby, Rust cargo, Go, NuGet, Alpine, Debian and derivative, RPM distributions, Windows, npm and yarn, Bower, Chef, Cocoapods, conda, cran, haxe, MSI, opam, pubspec.
Both ScanCode toolkit and ScanCode.io are extensively based on and use [Package URL](../specs/purl.md).

## Trivy

[Trivy](https://github.com/aquasecurity/trivy) scans container images, file systems, Git repositories, and Kubernetes clusters or resources for open source packages and dependencies, CVEs, IaC misconfigurations, and sensitive information. It generates SBOMs in the scanning process.
Trivy also allows signing and verifying [SBOM attestations](https://aquasecurity.github.io/trivy/v0.34/docs/attestation/sbom/).

## Vulnerability Operator

The [vulnerability-operator](https://github.com/ckotzbauer/vulnerability-operator) uses [Grype](https://github.com/anchore/grype) for scanning SBOMs and exports all found vulnerabilities into a JSON format.


## SBOM Quality Scoring 
[sbomqs](https://github.com/interlynk-io/sbomqs) provides comprehensive quality scoring for your sboms. It provide a quick compliance check of your sboms with NTIA minimum elements. It uses license, spec compliance,
data quality to help generate an accurate score for your sbom generator.  
