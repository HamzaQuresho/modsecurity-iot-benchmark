

# Empirical Evaluation of ModSecurity with OWASP CRS in IoT-like Deployments

This repository provides the artifacts required to reproduce an empirical evaluation of ModSecurity with the OWASP Core Rule Set (CRS) in an IoT-like deployment. The evaluation covers conventional HTTP traffic as well as MQTT-originated payloads that are translated into HTTP requests prior to inspection. The goal of this work is to establish a systematic empirical baseline, identify detection blind spots, and derive evidence-based implications for Web Application Firewalls (WAFs) in IoT environments.

The repository accompanies a research manuscript submitted to an international security journal and is intended to support reproducibility, transparency, and further research.

---

## Inspection Boundary

The inspection boundary in this study is explicitly defined at the HTTP layer. HTTP traffic is inspected directly by ModSecurity, while MQTT traffic is first translated into HTTP POST requests using a custom MQTT2HTTP translation module before inspection.

As a result:
- ModSecurity inspects only HTTP request structures, headers, and payloads.
- Native MQTT protocol elements are **outside the inspection boundary** and are not analyzed.

Specifically, the following MQTT components are **not in scope**:
- Control packet types (CONNECT, SUBSCRIBE, PUBLISH, etc.)
- Quality of Service (QoS) levels
- Retain flag etc.

References to “MQTT-related attacks” in this repository denote attacks whose payloads originate from MQTT messages but are evaluated solely through their translated HTTP representations.



---

## Included Artifacts

This repository includes:
- The MQTT2HTTP translation module used to convert MQTT payloads into HTTP POST requests.
- ModSecurity configuration files and OWASP CRS versions evaluated in the study.
- Enabled CRS rule lists for each experimental configuration.
- Curated attack payload lists grouped by attack category.
- Scripts to reproduce experiments and compute evaluation metrics.

---

## Payload Sources and Handling

Attack payloads were curated from established penetration-testing frameworks and publicly available security datasets, as detailed in the accompanying paper. For each attack category, payloads were drawn from one or more sources and deduplicated where overlaps occurred across sources.

Certain attack classes (e.g., Local File Inclusion and Path Traversal) may exhibit inherent payload similarity due to shared exploitation patterns.

Payload insertion points follow realistic attack vectors:
- HTTP GET requests: payloads injected into the request line.
- HTTP POST requests (including translated MQTT messages): payloads injected into the request body.

Where redistribution of certain payloads is restricted, only metadata or sanitized equivalents are provided.

---

## Integration with External Dataset (IEEE DataPort)

This repository integrates an externally published fuzzing dataset generated using the OWASP ZAP proxy. The dataset contains payloads and corresponding response codes obtained from automated fuzzing experiments.

The full dataset is publicly available via IEEE DataPort:
[IEEE DataPort DOI or URL]

Within this repository, the dataset is referenced for:
- Cross-validation of detection behavior
- Comparative analysis of fuzzing-derived payloads versus curated attack payloads
- Supplementary evaluation of resource exhaustion and buffer overflow scenarios

Scripts in the `analysis/` directory demonstrate how the DataPort dataset is incorporated into the evaluation pipeline.

---

## Reproducibility

To reproduce the experiments:
1. Set up the environment as described in `experiments/environment.yml`.
2. Configure ModSecurity and CRS using the files in `modsecurity/`.
3. Run the experiment orchestration scripts in `experiments/`.
4. Compute detection metrics and confidence intervals using scripts in `analysis/`.

Detailed step-by-step instructions are provided in `experiments/reproduce_results.md`.

---

## License and Citation

This repository is released under the specified license in the `LICENSE` file.

If you use this work, please cite it using the metadata provided in `CITATION.cff`.






