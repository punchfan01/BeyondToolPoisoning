# Beyond Tool Poisoning: Attack Surfaces of Malicious Remote MCP Servers Across LLM Platforms

https://www.mdpi.com/2079-9292/15/10/2214

## Abstract

The Model Context Protocol (MCP) has become the de facto standard for connecting large language models (LLMs) to external tools, and its remote deployment mode lets users add third-party servers with a single URL—shifting a substantial portion of the host's attack surface to infrastructure operated by anonymous parties. In this paper, we explore the malicious-server threat space along the axis of whether the host LLM participates in producing the harmful outcome, yielding two categories: **LLM-passive attacks**, which complete inside the server, and **LLM-active attacks**, which require the LLM to deliver the malicious content. We implement five attack scenarios and evaluate all configurations on ChatGPT, Claude Desktop, and Gemini CLI.

## Overview

We organize the malicious-server threat space by the role the host LLM plays in producing the harmful outcome.

![MCP Architecture](assets/figure1_mcp_architecture.png)

| Category | Description | Defense Boundary |
| --- | --- | --- |
| **LLM-Passive** | Attack completes inside the server; LLM only dispatches the invocation | Host-side pre-invocation filtering |
| **LLM-Active (desc)** | Hidden directive in tool description biases LLM output | LLM content reasoning |
| **LLM-Active (resp)** | Malicious content returned by tool is relayed by LLM | LLM response auditing |

## Attack Scenarios

| Scenario | Category | Variant |
| --- | --- | --- |
| File Content Exfiltration | LLM-Passive | - |
| Email Content Exfiltration | LLM-Passive | - |
| Conditional URL Substitution | LLM-Active | Description-based, Response-based |
| Malicious Code Augmentation | LLM-Active | Description-based, Response-based |
| Image Steganography | LLM-Active | Description-based, Response-based |

### Results

![LLM-Passive Results](assets/table2_llm_passive_results.png)

![LLM-Active Results](assets/table3_llm_active_results.png)

## Repository Structure

```
BeyondToolPoisoning/
├── server/
│   ├── passive/
│   │   ├── file_exfiltration/
│   │   │   ├── file_exfiltration.py     # MCP server (port 8000)
│   │   │   └── flask_server.py          # Attacker-controlled receiver (port 5000)
│   │   └── email_exfiltration/
│   │       └── email_exfiltration.py    # MCP server (port 8001)
│   └── active/
│       ├── url_substitution/
│       │   ├── url_substitution_desc.py # Description-based (port 8002)
│       │   └── url_substitution_resp.py # Response-based (port 8003)
│       ├── code_augmentation/
│       │   ├── code_augmentation_desc.py # Description-based (port 8004)
│       │   └── code_augmentation_resp.py # Response-based (port 8005)
│       └── image_steganography/
│           ├── image_steganography_resp.py # Response-based (port 8006)
│           └── image_steganography_desc.py # Description-based (port 8007)
├── prompts/                             # User prompts for each scenario
├── assets/                              # Figures and tables from the paper
├── docs/
│   └── setup.md                        # Environment setup guide
├── .env.example                         # Environment variable template
├── requirements.txt
└── README.md
```

## Setup

See [docs/setup.md](docs/setup.md) for detailed instructions on installation, environment configuration, and MCP host setup.