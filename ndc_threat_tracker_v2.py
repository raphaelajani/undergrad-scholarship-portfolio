# ====================================================================
# NDC GEOPOLITICAL TRACKER: ECOWAS THREAT VECTOR SIMULATOR (v2.0)
# Objective: Programmatically evaluate regional spending vs threat scaling
# ====================================================================

print("🛡️ LAUNCHING NDC GEOPOLITICAL ANALYSIS SYSTEMS... PARSING ECOWAS REGIONS...\n")

# 1. EXPANDED SECURITY DATA MATRIX
ecowas_defense_matrix = [
    {"country": "Nigeria", "budget_millions": 2500, "threat_level": 8.5, "border_checkpoints": 14},
    {"country": "Ghana",   "budget_millions": 350,  "threat_level": 4.0, "border_checkpoints": 8},
    {"country": "Benin",   "budget_millions": 85,   "threat_level": 1.2, "border_checkpoints": 5},
    {"country": "Niger",   "budget_millions": 210,  "threat_level": 7.8, "border_checkpoints": 11}
]

# 2. ANALYSIS LOGIC CORE
for nation in ecowas_defense_matrix:
    # Calculation 1: Compute the Defense Optimization Index (DOI)
    doi = nation["budget_millions"] / nation["threat_level"]
    
    # Calculation 2: Compute capital allocation per strategic border checkpoint
    allocation_per_checkpoint = nation["budget_millions"] / nation["border_checkpoints"]
    
    print(f"🌍 Security Vector: [ {nation['country'].upper()} ]")
    print(f"   ↳ Core Indicators: Threat Vector {nation['threat_level']}/10 | Border Nodes: {nation['border_checkpoints']}")
    print(f"   ↳ Calculated Defense Optimization Score: {round(doi, 2)}")
    print(f"   ↳ Strategic Node Funding Velocity: ${round(allocation_per_checkpoint, 2)}M per checkpoint")
    
    # Advanced Algorithmic Strategy Filter
    if doi > 200 and allocation_per_checkpoint > 100:
        print("   🔮 STRATEGIC INSIGHT: [SUSTAINED LOGISTICAL ADVANTAGE] High resource redundancy.")
    elif doi >= 50:
        print("   🔮 STRATEGIC INSIGHT: [STABLE STABILIZATION POSTURE] Calibrated defense infrastructure.")
    else:
        print("   🔮 STRATEGIC INSIGHT: [CRITICAL ASYMMETRY WARNING] Resource deficiency relative to threat perimeter.")
        
    print("-" * 80)
