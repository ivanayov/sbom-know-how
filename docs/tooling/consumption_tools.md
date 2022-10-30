# SBoM Consumption Tools
## FOSSology

FOSSology is a compliance scanner tool for license, copyright and export control. Documentation can be found on [the official web site](https://www.fossology.org).

## Grype

[Grype](https://github.com/anchore/grype) is a vulnerability scanner for container images and file systems. If scans for vulnerabilities for both operating system and language-specific packages. Supports Docker, OCI and Singularity image formats, as well as consumes SBoM attestations.

## Hoppr Cop

[Hoppr Cop](https://github.com/lmco/hoppr-cop) generates vulnerability information from CycloneDX SBoMs. It's available both as a CLI and a python library.

## KubeClarity

KubeClarity detects and manages SBoMs and vulnerabilities of container images and filesystems. It can also scan K8s runtime to detect vulnerabilities discovered post-deployment. It uses [Grype](https://github.com/anchore/grype) and [Dependency-Track](https://github.com/DependencyTrack/dependency-track) for vulnerability scanning. More detail can be found in the [KubeClarity documentation](https://github.com/openclarity/kubeclarity).

## K8s BOM

[K8s BOM](https://github.com/kubernetes-sigs/bom) offers drawing a structure of an SPDX document and serves for verification.

## OSS Review Toolkit

The [OSS Review Toolkit](https://github.com/oss-review-toolkit/ort) provides a list of tools, including [Analyzer](https://github.com/oss-review-toolkit/ort#analyzer) for dependencies of projects and their metadata, [Downloader](https://github.com/oss-review-toolkit/ort#downloader) for fetching source code and dependencies, [Scanner](https://github.com/oss-review-toolkit/ort#scanner) for detecting license / copyright findings from source code, [Advisor](https://github.com/oss-review-toolkit/ort#advisor) for retrieving security advisories for used dependencies, and others.

## SBOM Diff Action

[SBOM Diff Action](https://github.com/ckotzbauer/sbom-diff-action) is a GitHub integration tool that creates diffs for SBoMs from PR changes.

## SBoM Operator

The SBoM Operator allows checks for changed images and pods within a cluster. Provides vulnerability scans via the [Vulnerability Operator](#vulnerability-operator). For more detail, please refer to the SBoM Operators [Analysis-Trigger section](https://github.com/ckotzbauer/sbom-operator#analysis-trigger).

## SBoM Utility

[SBoM Utility](https://github.com/mrutkows/sbom-utility) is a CycloneDX and SPDX SBoM validation tool.

## Vulnerability Operator

The [vulnerability-operator](https://github.com/ckotzbauer/vulnerability-operator) uses [Grype](https://github.com/anchore/grype) for scanning SBoMs and exports all found vulnerabilities into a JSON format.