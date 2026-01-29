

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




