# SCITT Architecture

"[An Architecture for Trustworthy and Transparent Digital Supply Chains](https://datatracker.ietf.org/doc/draft-birkholz-scitt-architecture/)" publiation from 24 Oct 2022 defines a generic and scalable architecture to enable transparency across any supply chain with minimum adoption barriers for producers and enough flexibility to allow different implementations of Transparency Services with various auditing and compliance requirements.


##  Architecture Overview
                       .----------.
                      |  Artifact  |
                       '----+-----'
                            v
                       .----+----.  .----------.
   Issuer       -->   | Statement ||  Envelope  |
                       '----+----'  '-----+----'
                            |             |       +------------------+
                             '----. .----'        | DID Key Manifest |
                                   |              | (decentralized)  |
                                   v              +---+----------+---+
                                .--+--.   Sign Claim  |          |
                               | Claim +<------------'           |
                                '--+--'                          |
                                   |            +--------------+ |
                                .-' '---------->+ Transparency | |
                               |   .-------.    |              | |
   Transparency -->            |  | Receipt |<--+   Registry   | |
        Service                |   '---+---'    +-------+------+ |
                                '-. .-'                 |        |
                                   |                    |        |
                                   v                    |        |
                             .-+-------+-.              |        |
                            | Transparent |             |        |
                            |    Claim    |             |        |
                             '-----+-----'              |        |
                                   |                    |        |
                                   |'------.     .------)-------'
                                   |        |   |       |
                                   |        v   v       |
                                   |   .----+---+-----. |
   Verifier      -->               |  / Verify Claim /  |
                                   | '--------------'   |
                                   v                    v
                          .--------+---------.  .-------+---------.
   Auditor       -->     / Collect Receipts /  / Replay Registry /
                        '------------------'  '-----------------'

## GitHub and Community efforts

For more details on the SCITT Architecture approach, community efforts and progress, please visit the [SCITT GitHub organisation](https://github.com/ietf-scitt).

[SCITT Draft](https://github.com/ietf-scitt/draft-birkholz-scitt-architecture) is were updates and modifications are being proposed.

## Implementations

[DID EQT](https://github.com/transmute-industries/did-eqt) is a project for exploring SCITT Architecture Components and is NOT a reference implementation for SCITT.