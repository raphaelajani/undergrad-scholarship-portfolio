# ====================================================================
# GLOBAL CHART PREDICTOR: WEST AFRICAN ANOMALY INDEX (v2.1)
# Objective: Programmatically calculate Virality Efficiency Scores
# ====================================================================

print("🎵 INITIATING COMMERCIAL CHART ANOMALY DETECTION PIPELINE...\n")

music_database = [
    {"track_name": "Ku Lo Sa (Oxlade)",   "bpm": 100, "danceability": 78, "tiktok_trending": True,  "weekly_streams": 620000},
    {"track_name": "Wait For U (Future)",  "bpm": 83,  "danceability": 55, "tiktok_trending": True,  "weekly_streams": 750000},
    {"track_name": "Pray (Wizkid)",        "bpm": 102, "danceability": 64, "tiktok_trending": False, "weekly_streams": 480000}
]

for track in music_database:
    # Calculate custom evaluation metric
    ves_score = round(track["weekly_streams"] / track["danceability"], 2)
    
    print(f"📊 Vector: {track['track_name']} | Streaming Volume: {track['weekly_streams']:,}")
    print(f"   ↳ Computed Virality Efficiency Score (VES): {ves_score}")
    
    if ves_score > 10000:
        print("   🔮 STRATEGIC VALUATION: [MAXIMUM STRUCTURAL RETENTION] Scaling on core audio integrity.")
    elif ves_score >= 7000:
        print("   🔮 STRATEGIC VALUATION: [BALANCED GROWTH INDEX] Standard algorithmic optimization.")
    else:
        print("   🔮 STRATEGIC VALUATION: [TRAJECTORY STABLE] Metrics match standard market baselines.")
        
    print("-" * 80)
