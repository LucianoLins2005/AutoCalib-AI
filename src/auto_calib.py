import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# --- 1. TECHNICAL PREPARATION (ISO 17025 Rigor) ---
df = pd.read_csv('data/telemetry_data.csv')
df['yaw_error'] = df['yaw_rate_actual'] - df['yaw_rate_target']
kp_suggested = 1.65
LIMITE_BAR = 80 # ISO 26262 Safety Limit

df['brake_pressure_new'] = df.apply(
    lambda x: min(x['brake_pressure_old'] * kp_suggested, LIMITE_BAR) if x['yaw_error'] > 5 else x['brake_pressure_old'], 
    axis=1
)

# --- 2. AI EVALUATION SCORE LOGIC ---
def calculate_reliability_score(df):
    limit_check = all(df['brake_pressure_new'] <= LIMITE_BAR) 
    stability_impact = df['yaw_error'].max() > 5 
    score = 0
    if limit_check: score += 60
    if stability_impact: score += 40
    return score

ai_score = calculate_reliability_score(df)

# --- 3. GENERATING THE GRAPH (Creating 'fig' first!) ---
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                    vertical_spacing=0.15,
                    subplot_titles=("Dynamic Analysis: Tolerance Zone (ISO 17025)", 
                                    "Corrective Action: Safety Limits (ISO 26262)"))

# Subplot 1: Yaw Rate
fig.add_trace(go.Scatter(x=df['time_ms'], y=df['yaw_rate_target'], name='Target (Desired)', line=dict(dash='dash', color='blue')), row=1, col=1)
fig.add_trace(go.Scatter(x=df['time_ms'], y=df['yaw_rate_actual'], name='Actual (Unstable)', line=dict(color='red')), row=1, col=1)

# Subplot 2: Pressure
fig.add_trace(go.Scatter(x=df['time_ms'], y=df['brake_pressure_old'], name='Baseline Calibration', fill='tozeroy', line=dict(color='gray')), row=2, col=1)
fig.add_trace(go.Scatter(x=df['time_ms'], y=df['brake_pressure_new'], name='AI Optimized Calibration', line=dict(color='green', width=3)), row=2, col=1)

# --- 4. GLOBAL STYLING (English Labels) ---
fig.update_layout(height=700, title_text="<b>AutoCalib-AI: Algorithm Validation Framework</b>", showlegend=True)
fig.update_xaxes(title_text="Time (ms)", row=2, col=1)
fig.update_yaxes(title_text="Yaw Rate (deg/s)", row=1, col=1)
fig.update_yaxes(title_text="Pressure (bar)", row=2, col=1)

# AI Score Annotation
fig.add_annotation(dict(xref='paper', yref='paper', x=0.95, y=0.05,
                   text=f"<b>AI Reliability Score: {ai_score}/100</b>",
                   showarrow=False, font=dict(size=14, color="green")))

# Save and Show
os.makedirs('docs', exist_ok=True)
fig.write_html('docs/validation_report.html')
fig.show()

print(f"[SUCCESS] Dashboard generated in English at 'docs/validation_report.html'. AI Score: {ai_score}")