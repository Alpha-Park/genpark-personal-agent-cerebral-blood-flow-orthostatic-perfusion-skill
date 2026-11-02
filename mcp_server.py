# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Cerebral Blood Flow Orthostatic Perfusion Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentCerebralBloodFlowOrthostaticPerfusion

mcp = FastMCP("PersonalAgentCerebralBloodFlowOrthostaticPerfusion")
client = PersonalAgentCerebralBloodFlowOrthostaticPerfusion()

@mcp.tool()
def calculate_cerebral_perfusion_and_pulsatility(
    peak_systolic_velocity_cms: float = 95.0,
    end_diastolic_velocity_cms: float = 42.0,
    mean_flow_velocity_cms: float = 60.0
) -> str:
    """Calculates Gosling Pulsatility Index (PI), Resistive Index (RI), and microvascular resistance tier."""
    import json
    return json.dumps(client.calculate_cerebral_perfusion_and_pulsatility(
        peak_systolic_velocity_cms, end_diastolic_velocity_cms, mean_flow_velocity_cms
    ), indent=2)

@mcp.tool()
def model_hypocapnic_hyperventilation_vasoconstriction(
    current_etco2_mmhg: float = 28.0,
    baseline_etco2_mmhg: float = 40.0,
    baseline_mca_velocity_cms: float = 62.0
) -> str:
    """Calculates cerebral blood flow velocity drop and vasoconstriction induced by acute hypocapnia."""
    import json
    return json.dumps(client.model_hypocapnic_hyperventilation_vasoconstriction(
        current_etco2_mmhg, baseline_etco2_mmhg, baseline_mca_velocity_cms
    ), indent=2)

if __name__ == "__main__":
    mcp.run()
