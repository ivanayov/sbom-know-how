*********************************
SBOM Artifact Image Specification
*********************************

The `SBOM Artifact Image Spec <https://github.com/dlorenc/sbom-oci>`_ defines how to bundle SBOMs as OCI images. SBOM Artifact Image consist of one or more SBOM files, with annotations to indicate which other OCI artifacts, or parts of OCI artifacts, they are intended to cover.

The spec is not restricted to SBOMs generated from OCI images.

The SBOM OCI Artifact Specification defines a method of storing SBOM files which makes them easy to store and distribute, alongside the OCI artifacts they refer to.

Read about using `cosign` for attaching SBOMs to OCI images in the `Cosign SBOM Spec <https://github.com/sigstore/cosign/blob/main/specs/SBOM_SPEC.md>`_.