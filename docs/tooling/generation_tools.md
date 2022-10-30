
# SBoM Generation Tools

## CycloneDX Tool Center

Generates CycloneDX format SBoMs. Full list of tools can be found in the [CycloneDX Tool Center](https://cyclonedx.org/tool-center/).

## Docker SBOM

Generates SBoMs for Docker images with the currently experimental `docker sbom` command. Based on [Syft](#syft). For more detail, please visit the [Docker SBOM Documentation](https://docs.docker.com/engine/sbom/).

## FatBOM

FatBOM generates SBoMs via [Syft](#syft), [Salus](#salus), [SPDX SBoM Generator](#spdx-sbom-generator) and [K8s BOM](#k8s-bom) and composes them into a single SPDX SBoM in JSON format. Full details can be found in the [FatBOM GitHub repository](https://github.com/sbs2001/fatbom).

## KubeClarity

[KubeClarity](https://github.com/openclarity/kubeclarity) uses [Syft](#syft) and [Cyclonedx-gomod](https://github.com/CycloneDX/cyclonedx-gomod) ([CycloneDX Tool Center](#cyclonedx-tool-center)) to generate SBoMs and offers [SBoM scanning](consumption_tools.md#kubeclarity).

## K8s BOM

[K8s BOM](https://github.com/kubernetes-sigs/bom) generates SBoMs from files, images, and docker archives and supports pulling images from remote registries. The SBоM data can be exported to an [in-toto](https://in-toto.io) provenance attestation. For SBoM scanning details, please see the [K8s BOM consumption tools](consumption_tools.md#k8s-bom) section.

## Pkgconf bomtool

Bomtool is a feature of [pkgconf](http://pkgconf.org) and can be used for generating SBoMs for C/C++ packages under Alpine. Usage:
```bash
$ bomtool <package_name>
```
where package name should be linked in `pkgconf`.

## Salus

[Salus](https://github.com/microsoft/sbom-tool) is an Open Source SBoM generation tool implemented by Micrisoft. It allows build-time generation from source and packages, as well as [CI/CD pipelines integration](https://github.com/microsoft/sbom-tool#integrating-sbom-tool-to-your-cicd-pipelines) via [GitHub Actions](https://github.com/microsoft/sbom-tool/blob/main/docs/setting-up-github-actions.md) and [Azure DevOps Pipelines](https://github.com/microsoft/sbom-tool/blob/main/docs/setting-up-ado-pipelines.md).

## SBoM Operator 

[SBOM Operator](https://github.com/ckotzbauer/sbom-operator) uses [Syft](#syft) to generate SBoMs from each image deployed in a Kubernetes cluster. Relies on [go-containeregistry](https://github.com/google/go-containerregistry) for downloading images. Allows [analysis](consumption_tools.md#sbom-operator).

## SPDX SBoM Generator

The [SPDX SBoM Generator](https://github.com/opensbom-generator/spdx-sbom-generator) generates SBoMs from source code. The supported package managers can be found the the tool [Overview](https://github.com/opensbom-generator/spdx-sbom-generator#overview).

## Syft

[Syft](https://github.com/anchore/syft) generates SBoMs from container images and file systems. It provides both a CLI tool and a Go library. Supported ecosystems are available in the tool [documentation](https://github.com/anchore/syft#supported-ecosystems).

## Tern

[Tern](https://github.com/tern-tools/tern) is a software package inspection tool that generates SBoMs for container images and Dockerfiles. Supports both [SPDX](../specs/spdx.md) and [CycloneDX](../specs/cyclonedx.md), [test](../specs/swid.md).