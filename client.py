# -*- coding: utf-8 -*-
"""Personal Agent Cerebral Blood Flow Orthostatic Perfusion Skill.

Zero-dependency Transcranial Doppler (TCD) Middle Cerebral Artery (MCA) velocity modeler,
Gosling Pulsatility Index (PI) calculator, and hypocapnic hyperventilation vasoconstriction evaluator.
"""

import math
from typing import Dict, Any, Optional

class PersonalAgentCerebralBloodFlowOrthostaticPerfusion:
    """Quantitative cerebral hemodynamics and cerebrovascular autoregulation engine
    based on Transcranial Doppler (TCD) ultrasonography and CO2 arterial vasoreactivity models."""

    def calculate_cerebral_perfusion_and_pulsatility(
        self,
        peak_systolic_velocity_cms: float = 95.0,
        end_diastolic_velocity_cms: float = 42.0,
        mean_flow_velocity_cms: float = 60.0
    ) -> Dict[str, Any]:
        """Calculates Gosling Pulsatility Index (PI), Pourcelot Resistive Index (RI),
        and intracranial downstream microvascular resistance tier."""
        vs = max(20.0, float(peak_systolic_velocity_cms))
        vd = max(5.0, float(end_diastolic_velocity_cms))
        vm = max(10.0, float(mean_flow_velocity_cms))

        # Gosling Pulsatility Index: PI = (Vs - Vd) / Vm
        pi = round((vs - vd) / vm, 2)

        # Pourcelot Resistive Index: RI = (Vs - Vd) / Vs
        ri = round((vs - vd) / vs, 2)

        # TCD Clinical Reference Benchmarks (MCA mean velocity normal: 50 - 75 cm/s, PI: 0.70 - 1.10)
        if 0.70 <= pi <= 1.10:
            pi_tier = "Normal Intracranial Pulsatility / Healthy Microvascular Resistance"
            clinical_status = "Intact downstream cerebral arteriolar compliance"
        elif pi > 1.25:
            pi_tier = "Elevated Cerebral Pulsatility Index"
            clinical_status = "Increased distal cerebrovascular resistance or elevated intracranial pressure (ICP)"
        else:
            pi_tier = "Low Pulsatility / Distal Vasodilation"
            clinical_status = "Reduced distal resistance; possible arteriovenous shunting or proximal flow restriction"

        if 50.0 <= vm <= 75.0:
            vm_tier = "Normative Baseline Perfusion Velocity"
        elif vm > 85.0:
            vm_tier = "Hyperdynamic Cerebral Perfusion or Focal Vasospasm"
        else:
            vm_tier = "Sub-Optimal Cerebral Hypoperfusion Velocity"

        return {
            "mca_peak_systolic_velocity_cms": vs,
            "mca_end_diastolic_velocity_cms": vd,
            "mca_mean_flow_velocity_cms": vm,
            "gosling_pulsatility_index_pi": pi,
            "pourcelot_resistive_index_ri": ri,
            "pulsatility_status_tier": pi_tier,
            "mean_velocity_status_tier": vm_tier,
            "hemodynamic_assessment": clinical_status
        }

    def model_hypocapnic_hyperventilation_vasoconstriction(
        self,
        current_etco2_mmhg: float = 28.0,
        baseline_etco2_mmhg: float = 40.0,
        baseline_mca_velocity_cms: float = 62.0
    ) -> Dict[str, Any]:
        """Calculates cerebral arteriolar vasoconstriction and blood flow velocity drop
        induced by acute hypocapnia (hyperventilation / shallow chest over-breathing)."""
        etco2_cur = max(15.0, min(65.0, float(current_etco2_mmhg)))
        etco2_base = max(30.0, min(50.0, float(baseline_etco2_mmhg)))
        vm_base = max(20.0, float(baseline_mca_velocity_cms))

        # Cerebrovascular CO2 Reactivity:
        # Cerebral blood flow changes ~3.0% per 1 mmHg delta in ETCO2
        delta_etco2 = etco2_cur - etco2_base
        percent_velocity_change = round(delta_etco2 * 3.0, 1)

        # Projected new mean velocity
        projected_vm = round(max(15.0, vm_base * (1.0 + (percent_velocity_change / 100.0))), 1)

        if delta_etco2 <= -8.0:
            vaso_status = "Severe Hypocapnic Vasoconstriction / Cerebral Oligemia"
            symptoms = "Prefrontal hypoperfusion, lightheadedness, tunnel vision, cognitive fragmentation, and panic triggers"
        elif delta_etco2 < 0.0:
            vaso_status = "Mild Hypocapnic Arterial Constriction"
            symptoms = "Sub-clinical reduction in cerebral oxygen delivery; mild attention fatigue"
        elif delta_etco2 <= 5.0:
            vaso_status = "Eucapnic Normative Vasomotor Tone"
            symptoms = "Optimal cerebral tissue oxygenation and physiological Bohr effect"
        else:
            vaso_status = "Hypercapnic Cerebral Vasodilation"
            symptoms = "Intracranial vasodilation; potential throbbing headache if ETCO2 > 48 mmHg"

        return {
            "current_etco2_mmhg": etco2_cur,
            "baseline_etco2_mmhg": etco2_base,
            "delta_etco2_mmhg": round(delta_etco2, 1),
            "cerebral_blood_flow_velocity_shift_pct": f"{'+' if percent_velocity_change > 0 else ''}{percent_velocity_change}%",
            "projected_mca_mean_velocity_cms": projected_vm,
            "vasomotor_state": vaso_status,
            "clinical_symptom_forecast": symptoms,
            "breathwork_countermeasure": (
                "IMMEDIATE PROTOCOL: Execute slow nasal breathing with extended exhalations (4s in, 8s out) "
                "or brief 5-second breath holds to elevate alveolar CO2 back to 40 mmHg."
                if delta_etco2 <= -6.0 else
                "Maintain natural rhythmic diaphragmatic respiration."
            )
        }
