# ====================================================================
# ICT LITERACY CLUB: ENLIGHTENMENT LOG & ENGAGEMENT METRICS (v1.1)
# Objective: Track peer presentation metrics and topic performance
# ====================================================================

print("🖥️ INITIATING ICT CLUB ENLIGHTENMENT PORTAL TERMINAL...\n")

# 1. ACTUAL PRESENTATION LOG (List of Dictionaries)
enlightenment_sessions = [
    {"topic": "How AI Music Generation Works", "engagement_rating": 9.2, "attendance": 28},
    {"topic": "Cybersecurity & Spotting Online Scams", "engagement_rating": 8.5, "attendance": 35},
    {"topic": "Data Centers & How the Global Internet Moves", "engagement_rating": 6.1, "attendance": 14},
    {"topic": "Mobile Wallet Architecture (OPay/PalmPay)", "engagement_rating": 9.5, "attendance": 42},
    {"topic": "The Data Science of Basketball Statistics", "engagement_rating": 9.8, "attendance": 39}
]


high_impact_sessions_count = 0
aggregate_attendance = 0

# 2. LOGIC PIPELINE: Filtering high-impact presentation data
for session in enlightenment_sessions:
    print(f"🎤 Topic Shared: '{session['topic']}'")
    print(f"   ↳ Metrics: {session['attendance']} Students Attended | Engagement: {session['engagement_rating']}/10")
    
    # Track overall student attendance footprint
    aggregate_attendance = aggregate_attendance + session["attendance"]
    
    # Algorithmic Rule: If engagement is above 8.0, mark it as a high-impact topic
    if session["engagement_rating"] >= 8.0:
        high_impact_sessions_count = high_impact_sessions_count + 1
        print("   🔮 ANALYTICS: [HIGH PROFILE IMPACT] Topic holds peak peer interest. Expand on this vector.")
    else:
        print("   🔮 ANALYTICS: [LOW ATTENTION RETENTION] Abstract concept. Pivot format to interactive models.")
        
    print("-" * 75)

print("\n📊 TERM IMPACT ANALYSIS REPORT:")
print(f"   ▪️ Total High-Engagement Frameworks Delivered: {high_impact_sessions_count} sessions")
print(f"   ▪️ Combined Student Attendance Touchpoints: {aggregate_attendance} peers reached")
