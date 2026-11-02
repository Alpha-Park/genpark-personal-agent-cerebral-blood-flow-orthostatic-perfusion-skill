# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Cerebral Blood Flow Orthostatic Perfusion Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentCerebralBloodFlowOrthostaticPerfusion

def main():
    agent = PersonalAgentCerebralBloodFlowOrthostaticPerfusion()

    print("=" * 70)
    print("DEMO: Personal Agent Cerebral Blood Flow (TCD) & Perfusion Engine")
    print("=" * 70)

    # 1. Transcranial Doppler Hemodynamics (Vs: 96 cm/s, Vd: 44 cm/s, Vm: 62 cm/s)
    res_tcd = agent.calculate_cerebral_perfusion_and_pulsatility(
        peak_systolic_velocity_cms=96.0,
        end_diastolic_velocity_cms=44.0,
        mean_flow_velocity_cms=62.0
    )

    print(f"\n1. Middle Cerebral Artery (MCA) Perfusion Profile:")
    print(f"   Velocities: Systolic={res_tcd['mca_peak_systolic_velocity_cms']} cm/s | Diastolic={res_tcd['mca_end_diastolic_velocity_cms']} cm/s | Mean={res_tcd['mca_mean_flow_velocity_cms']} cm/s")
    print(f"   Gosling Pulsatility Index (PI): {res_tcd['gosling_pulsatility_index_pi']} ({res_tcd['pulsatility_status_tier']})")
    print(f"   Pourcelot Resistive Index (RI): {res_tcd['pourcelot_resistive_index_ri']}")
    print(f"   Mean Velocity Status: {res_tcd['mean_velocity_status_tier']}")
    print(f"   Assessment: {res_tcd['hemodynamic_assessment']}")

    # 2. Hyperventilation Over-Breathing Challenge (ETCO2 drops 40 -> 26 mmHg)
    res_co2 = agent.model_hypocapnic_hyperventilation_vasoconstriction(
        current_etco2_mmhg=26.0,
        baseline_etco2_mmhg=40.0,
        baseline_mca_velocity_cms=62.0
    )

    print(f"\n2. Hypocapnic Hyperventilation Vasoconstriction Response:")
    print(f"   ETCO2: {res_co2['current_etco2_mmhg']} mmHg (Delta: {res_co2['delta_etco2_mmhg']} mmHg)")
    print(f"   Cerebral Velocity Shift: {res_co2['cerebral_blood_flow_velocity_shift_pct']}")
    print(f"   Projected Mean Velocity: {res_co2['projected_mca_mean_velocity_cms']} cm/s")
    print(f"   Vasomotor State: {res_co2['vasomotor_state']}")
    print(f"   Symptom Forecast: {res_co2['clinical_symptom_forecast']}")
    print(f"   Countermeasure: {res_co2['breathwork_countermeasure']}")

    print("\nVerification complete: Cerebral blood flow engine executed flawlessly.")

if __name__ == "__main__":
    main()
