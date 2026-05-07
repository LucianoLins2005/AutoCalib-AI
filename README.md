# AutoCalib-AI: Intelligent Framework for Vehicle Dynamics Calibration 🚗🤖

Este repositório apresenta um framework avançado para a otimização e validação de sistemas de controle ativo (ESC/TCS), unindo **Engenharia Automotiva de Precisão** com **Inteligência Artificial Aplicada**.

O projeto foi desenvolvido para automatizar a análise de telemetria e sugerir calibrações de segurança sob o rigor das normas internacionais de segurança funcional e metrologia.

## 🌟 Diferenciais Estratégicos
* **Rigor Normativo**: Implementação baseada na **ISO 26262** (Segurança Funcional) e **ISO 17025** (Confiabilidade de Dados).
* **AI Reliability Score**: Sistema de avaliação integrado que audita a segurança e a eficácia da sugestão da IA antes da aplicação no veículo.
* **Foco em Time-to-Market**: Redução do tempo de pista através de pré-calibração orientada por dados de telemetria.

## 🛠️ Pilares Técnicos

### 1. Dinâmica Veicular e Controle
O algoritmo processa dados de **Yaw Rate** (Taxa de Guinada) e **Steering Angle** (Ângulo de Volante) para identificar desvios em manobras de limite de aderência.
* **Zona de Tolerância**: Define bandas de confiança de ±10% sobre o modelo dinâmico alvo para evitar intervenções desnecessárias.
* **Safety Limits**: A calibração sugerida respeita limites físicos de hardware (80 bar de pressão máxima).

### 2. IA Evaluation Framework (Item C)
Diferente de scripts comuns, este framework possui uma camada de **Auditoria de IA**:
* **Safety Check**: Garante conformidade com limites de segurança funcional.
* **AI Reliability Score**: Métrica dinâmica (0-100) exibida no dashboard para suporte à decisão.

## 📊 Dashboard de Engenharia
O sistema gera um relatório interativo contendo:
- Comparativo Real vs. Alvo com zonas de incerteza.
- Nova curva de pressão hidráulica otimizada.
- Selo de Qualidade *AI Reliability Score*.

## 📂 Estrutura do Projeto
```text
/
├── data/
│   └── telemetry_data.csv      # Logs simulados de rede CAN
├── src/
│   └── auto_calib.py           # Core engine e lógica de IA
├── docs/
│   └── dashboard_report.html   # Relatório de validação técnica
└── README.md                   # Documentação do framework

Como Executar
Instale as dependências: pip install pandas plotly

Execute o assistente: python src/auto_calib.py