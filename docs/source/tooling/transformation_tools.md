# SBoM Transofmation Tools
## CDX2SPDX

[CDX2SPDX](https://github.com/spdx/cdx2spdx) is a Java tool that converts [CycloneDX](../specs/cyclonedx.md) SBoMs to [SPDX](../specs/spdx.md).

## SBoM Composer

[SBoM Composer](https://github.com/vmware-samples/sbom-composer) is a tool that serves for composing [SPDX](../specs/spdx.md) SBoM files into a single SPDX document. Not restricted by the contents of the composable SBoMs, as long as they are valid SPDX. The version of the final document is the latest amongst all composed.

## Tejelote

[Tejelote](https://github.com/puerco/tejolote) is a tool that consumes SBoMs and generates [SLSA](https://slsa.dev/) provenance attestations about build runs.