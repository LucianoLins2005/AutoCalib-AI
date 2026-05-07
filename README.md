# AutoCalib-AI: Intelligent Framework for Vehicle Dynamics Calibration 🚗🤖

This repository features an advanced framework for optimizing and validating Active Control Systems (ESC/TCS), merging **High-Precision Automotive Engineering** with **Applied Artificial Intelligence**.

The project was designed to automate telemetry analysis and suggest safety calibrations under the rigor of international functional safety and metrology standards.

---

## 📊 Project Outputs

### Technical Dashboard
![Dashboard Preview](docs/dashboard_preview.png)

### Validation Report
The framework automatically generates a professional HTML report for auditing purposes. 
* **File**: `docs/validation_report.html`
* **Purpose**: Detailed visualization of braking pressure corrections and stability metrics.

---

## 🌟 Strategic Differentiators
* **Regulatory Compliance**: Implementation based on **ISO 26262** (Functional Safety) and **ISO 17025** (Data Reliability).
* **AI Reliability Score**: Integrated audit system that evaluates the safety and efficacy of AI suggestions before vehicle application.
* **Time-to-Market Focus**: Reduction in track testing time through data-driven pre-calibration.

## 🛠️ Technical Pillars

### 1. Vehicle Dynamics & Control
The algorithm processes **Yaw Rate** and **Steering Angle** data to identify deviations in limit-handling maneuvers.
* **Tolerance Zone**: Defines ±10% confidence bands over the target dynamic model to prevent nuisance interventions.
* **Safety Limits**: Calibration suggestions respect hardware physical limits (e.g., 80 bar maximum hydraulic pressure).

### 2. AI Evaluation Framework
This framework includes an **AI Audit Layer**:
* **Safety Check**: Ensures compliance with functional safety boundaries.
* **Reliability Metric**: A dynamic score (0-100) displayed on the dashboard to support Senior Engineer decision-making.

## 📁 Project Structure
```text
/
├── data/
│   └── telemetry_data.csv      # Simulated CAN-Bus logs
├── src/
│   └── auto_calib.py           # Core engine and AI logic
├── docs/
│   ├── validation_report.html  # Technical validation report
│   └── dashboard_preview.png   # Dashboard preview image
└── README.md                   # Project documentation

🚀 Usage
Install dependencies:
pip install pandas plotly

Run the assistant:
python src/auto_calib.py