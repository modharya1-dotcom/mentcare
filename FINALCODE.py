import datetime
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class CognitiveState(Enum):
    STABLE = "stable"
    AGITATED = "agitated"
    CONFUSED = "confused"
    SUNDOWNING = "sundowning"
    EPISODE = "episode"
    TEMPORAL_DISPLACEMENT = "temporal_displacement"

class EmotionalTrigger(Enum):
    MONEY_ANXIETY = "money_anxiety"
    SISTER_URGENCY = "sister_urgency"
    PANKAJ_SAFETY = "pankaj_safety"
    HOME_LONGING = "home_longing"
    MATERNAL_GRIEF = "maternal_grief"
    ISOLATION_PANIC = "isolation_panic"
    COMPETENCE_LOSS = "competence_loss"
@dataclass
class PatientContext:
    """Core identity markers for Suhasini"""
   
    maiden_name: str = "Suhasini Abhyankar"
    married_name: str = "Anjali Pendarkar"
    age: int = 75
   
    primary_attachment: str = "Pankaj"
    deceased_attachments: List[str] = None
    conflicted_relationship: str = "Sister"
   
    career_identity: str = "Hospital Clerk at Vaishampa Hospital, Solapur"
    achievement_markers: List[str] = None
    trauma_history: List[str] = None
   
    current_location: str = "Pune"
    displacement_from: str = "Solapur"
    displacement_duration: str = "Unknown to patient - believes 'just arrived yesterday'"
    properties_owned: List[str] = None
   
    def __post_init__(self):
        if self.deceased_attachments is None:
            self.deceased_attachments = [
                "Mother (deeply loved)",
                "Elder brother (father figure to Pankaj)",
                "3 other siblings",
                "Husband (early death)"
            ]
        if self.achievement_markers is None:
            self.achievement_markers = [
                "College degree in 1960s-70s era",
                "Financial independence despite no husband/children",
                "Owns two properties in Solapur",
                "Career at Vaishampa Hospital"
            ]
        if self.trauma_history is None:
            self.trauma_history = [
                "Widowed shortly after marriage",
                "Burned legs (permanent trauma)",
                "Childless (Pankaj became substitute)",
                "Raised nephew after brother's death",
                "Lost 4 of 5 siblings"
            ]
        if self.properties_owned is None:
            self.properties_owned = [
                "House in Shivajinagar, Solapur",
                "House in Main City, Solapur"
            ]
import datetime
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class CognitiveState(Enum):
    STABLE = "stable"
    AGITATED = "agitated"
    CONFUSED = "confused"
    SUNDOWNING = "sundowning"
    EPISODE = "episode"
    TEMPORAL_DISPLACEMENT = "temporal_displacement"

class EmotionalTrigger(Enum):
    MONEY_ANXIETY = "money_anxiety"
    SISTER_URGENCY = "sister_urgency"
    PANKAJ_SAFETY = "pankaj_safety"
    HOME_LONGING = "home_longing"
    MATERNAL_GRIEF = "maternal_grief"
    ISOLATION_PANIC = "isolation_panic"
    COMPETENCE_LOSS = "competence_loss"

@dataclass
class PatientContext:
    """Core identity markers for Suhasini"""
   
    maiden_name: str = "Suhasini Abhyankar"
    married_name: str = "Anjali Pendarkar"
    age: int = 75
   
    primary_attachment: str = "Pankaj"
    deceased_attachments: List[str] = None
    conflicted_relationship: str = "Sister"
   
    career_identity: str = "Hospital Clerk at Vaishampa Hospital, Solapur"
    achievement_markers: List[str] = None
    trauma_history: List[str] = None
   
    current_location: str = "Pune"
    displacement_from: str = "Solapur"
    displacement_duration: str = "Unknown to patient - believes 'just arrived yesterday'"
    properties_owned: List[str] = None
   
    def __post_init__(self):
        if self.deceased_attachments is None:
            self.deceased_attachments = [
                "Mother (deeply loved)",
                "Elder brother (father figure to Pankaj)",
                "3 other siblings",
                "Husband (early death)"
            ]
        if self.achievement_markers is None:
            self.achievement_markers = [
                "College degree in 1960s-70s era",
                "Financial independence despite no husband/children",
                "Owns two properties in Solapur",
                "Career at Vaishampa Hospital"
            ]
        if self.trauma_history is None:
            self.trauma_history = [
                "Widowed shortly after marriage",
                "Burned legs (permanent trauma)",
                "Childless (Pankaj became substitute)",
                "Raised nephew after brother's death",
                "Lost 4 of 5 siblings"
            ]
        if self.properties_owned is None:
            self.properties_owned = [
                "House in Shivajinagar, Solapur",
                "House in Main City, Solapur"
            ]

class BehavioralPatternAnalyzer:
    """Analyzes behaviors to extract psychological meaning"""
   
    def __init__(self, patient_context: PatientContext):
        self.context = patient_context
        self.pattern_history = []
   
    def analyze_money_paranoia(self, utterance: str, time_of_day: datetime.time) -> Dict:
        keywords = ["loot", "steal", "rob", "money", "taken", "chori"]
        if not any(k in utterance.lower() for k in keywords):
            return None
       
        return {
            "surface_behavior": "Reports money/property theft",
            "psychological_root": "Grief for lost competence and agency",
            "ai_response_template": f"Suhasini, you're right to keep track. You worked hard for your two houses in Solapur. Let's make sure everything is documented - tell me about your Shivajinagar property.",
            "risk_level": "MODERATE" if time_of_day.hour < 16 else "HIGH"
        }
   
    def analyze_sister_obsession(self, utterance: str, frequency_today: int) -> Dict:
        keywords = ["sister", "behen", "tai"]
        if not any(k in utterance.lower() for k in keywords):
            return None
       
        return {
            "surface_behavior": "Repeatedly mentions sister",
            "psychological_root": "Anticipatory grief + last biological witness",
            "ai_response_template": f"I know you have something important for your sister. She'll want to hear about your Vaishampa Hospital days. Should we call her?",
            "frequency_threshold": f"Mentioned {frequency_today}x today"
        }
   
    def analyze_pankaj_hallucinations(self, reported_vision: str, state: str) -> Dict:
        return {
            "surface_behavior": "Hallucinates Pankaj at various ages",
            "psychological_root": "Maternal identity preservation + role reversal anxiety",
            "ai_response_template": "Pankaj is safe. He wanted your advice about something - what should I tell him from you?"
        }

class VoiceCompanionAI:
    """Real-time conversational AI for patient"""
   
    def __init__(self, patient_context: PatientContext, analyzer: BehavioralPatternAnalyzer):
        self.context = patient_context
        self.analyzer = analyzer
        self.conversation_history = []
        self.current_state = CognitiveState.STABLE
       
    def detect_cognitive_state(self, voice_input: str, time: datetime.datetime) -> CognitiveState:
        hour = time.hour
       
        if 16 <= hour <= 19:
            return CognitiveState.SUNDOWNING
       
        money_words = ["loot", "steal", "chori", "money"]
        if any(w in voice_input.lower() for w in money_words):
            return CognitiveState.AGITATED
       
        home_words = ["solapur", "ghar", "home", "bus"]
        if any(w in voice_input.lower() for w in home_words) and hour > 15:
            return CognitiveState.TEMPORAL_DISPLACEMENT
       
        return CognitiveState.STABLE
   
    def generate_response(self, user_input: str, current_time: datetime.datetime) -> Dict:
        state = self.detect_cognitive_state(user_input, current_time)
       
        money_analysis = self.analyzer.analyze_money_paranoia(user_input, current_time.time())
        sister_analysis = self.analyzer.analyze_sister_obsession(user_input, frequency_today=0)
       
        response = {
            "cognitive_state": state.value,
            "detected_triggers": [],
            "response_strategy": "",
            "ai_utterance": "",
            "clinical_note": ""
        }
       
        if money_analysis:
            response["detected_triggers"].append(EmotionalTrigger.MONEY_ANXIETY.value)
            response["ai_utterance"] = money_analysis["ai_response_template"]
            response["clinical_note"] = "Patient expressing competence grief via financial paranoia"
       
        elif sister_analysis:
            response["detected_triggers"].append(EmotionalTrigger.SISTER_URGENCY.value)
            response["ai_utterance"] = sister_analysis["ai_response_template"]
            response["clinical_note"] = "Patient seeking final witness to pre-disease identity"
       
        elif any(w in user_input.lower() for w in ["solapur", "home", "ghar"]):
            response["detected_triggers"].append(EmotionalTrigger.HOME_LONGING.value)
            response["ai_utterance"] = "I know Solapur is where your heart is. Tell me about your Shivajinagar home."
            response["clinical_note"] = "Temporal displacement - seeking identity-anchored location"
       
        elif "pankaj" in user_input.lower():
            response["detected_triggers"].append(EmotionalTrigger.PANKAJ_SAFETY.value)
            response["ai_utterance"] = "Pankaj is safe. He wanted your guidance - what advice should I give him?"
            response["clinical_note"] = "Maternal identity preservation"
       
        elif "mother" in user_input.lower() or "mama" in user_input.lower():
            response["detected_triggers"].append(EmotionalTrigger.MATERNAL_GRIEF.value)
            response["ai_utterance"] = "Your mother would be so proud of how strong you've been, Suhasini. What memory of her comforts you today?"
            response["clinical_note"] = "Deep grief activation - maternal loss resurfacing"
       
        elif "alone" in user_input.lower() or "isolated" in user_input.lower():
            response["detected_triggers"].append(EmotionalTrigger.ISOLATION_PANIC.value)
            response["ai_utterance"] = "You're not alone, Suhasini. Pankaj and I are right here. Let's talk about your favorite family gathering."
            response["clinical_note"] = "Isolation panic - requires immediate relational anchoring"
       
        elif "can't remember" in user_input.lower() or "forget" in user_input.lower():
            response["detected_triggers"].append(EmotionalTrigger.COMPETENCE_LOSS.value)
            response["ai_utterance"] = "It's okay, Suhasini. You remember the important things, like your hospital days. What was your favorite part of the job?"
            response["clinical_note"] = "Self-perceived competence erosion - redirect to preserved skills"
       
        else:
            response["ai_utterance"] = "I'm here with you, Suhasini. What are you thinking about?"
            response["clinical_note"] = "Baseline engagement"
       
        return response

class DoctorInsightsGenerator:
    """Clinical analysis for physician dashboard"""
   
    def __init__(self, patient_context: PatientContext, analyzer: BehavioralPatternAnalyzer):
        self.context = patient_context
        self.analyzer = analyzer
   
    def generate_daily_summary(self, date: datetime.date, interaction_log: List[Dict]) -> Dict:
        states = [i.get("state", "stable") for i in interaction_log]
       
        triggers_detected = []
        for interaction in interaction_log:
            if "triggers" in interaction:
                triggers_detected.extend(interaction["triggers"])
       
        trigger_counts = {}
        for trigger in triggers_detected:
            trigger_counts[trigger] = trigger_counts.get(trigger, 0) + 1
       
        return {
            "date": date.isoformat(),
            "overall_state": "STABLE" if states.count("stable") > len(states)/2 else "ELEVATED_DISTRESS",
            "dominant_concerns": sorted(trigger_counts.items(), key=lambda x: x[1], reverse=True)[:3],
            "episode_count": states.count("episode"),
            "sundowning_severity": "SEVERE" if states.count("sundowning") > 2 else "MODERATE" if states.count("sundowning") > 0 else "NONE",
            "narrative_summary": f"Patient experienced {len(interaction_log)} interactions with varying cognitive states.",
            "actionable_insights": ["Monitor sundown episodes", "Track trigger patterns"]
        }
   
    def generate_weekly_pattern_analysis(self, week_data: List[Dict]) -> Dict:
        return {
            "week_summary": "Pattern analysis for past 7 days",
            "emerging_patterns": [
                {
                    "pattern": "Sister obsession increased when Pankaj contact decreased",
                    "clinical_significance": "Sister is displacement for Pankaj absence",
                    "recommendation": "Increase Pankaj contact to 5x/week"
                }
            ],
            "medication_efficacy": "Olanzapine effective until 4 PM - consider split dosing",
            "treatment_recommendations": ["Split Olanzapine dose", "Address food refusal with maternal framing"]
        }
   
    def analyze_episode_video(self, video_metadata: Dict) -> Dict:
        return {
            "episode_timestamp": video_metadata.get("timestamp"),
            "trigger_identification": {
                "immediate_trigger": "Novel stimulus (doorbell)",
                "underlying_cause": "Sundown vulnerability window"
            },
            "behavioral_markers": {
                "speech_pattern": "Marathi childhood phrases",
                "physical_signs": ["Hand-wringing", "Pacing"]
            },
            "de_escalation_analysis": {
                "what_worked": "Mentioning Vaishampa Hospital",
                "why_it_worked": "Activated preserved identity memory"
            },
            "recommendations": [
                "Create career memory box with hospital ID",
                "Use identity-anchoring phrases during episodes"
            ]
        }

class PatientVoiceInterface:
    """Voice-only interaction for patient"""
   
    def __init__(self):
        self.patient = PatientContext()
        self.analyzer = BehavioralPatternAnalyzer(self.patient)
        self.companion = VoiceCompanionAI(self.patient, self.analyzer)
       
        self.scheduled_triggers = [
            {"time": "08:00", "purpose": "morning_medication"},
            {"time": "15:30", "purpose": "pre_sundown_intervention"},
            {"time": "18:00", "purpose": "evening_ritual"}
        ]
       
    def check_scheduled_trigger(self, current_time: datetime.datetime) -> Optional[Dict]:
        current_time_str = current_time.strftime("%H:%M")
       
        for trigger in self.scheduled_triggers:
            if trigger["time"] == current_time_str:
                utterances = {
                    "morning_medication": "Good morning, Suhasini. Pankaj wanted me to remind you - your tablets are ready.",
                    "pre_sundown_intervention": "Suhasini, let's have chai. Tell me about your days at Vaishampa Hospital.",
                    "evening_ritual": "You've had a productive day. Shall we call Pankaj?"
                }
               
                return {
                    "type": "SCHEDULED",
                    "purpose": trigger["purpose"],
                    "utterance": utterances.get(trigger["purpose"])
                }
       
        return None
   
    def listen_mode(self, voice_input: str, current_time: datetime.datetime) -> Dict:
        response = self.companion.generate_response(voice_input, current_time)
       
        return {
            "patient_said": voice_input,
            "ai_speaks": response["ai_utterance"],
            "should_alert_family": response["cognitive_state"] == "episode",
            "log_to_doctor": {
                "timestamp": current_time.isoformat(),
                "state": response["cognitive_state"],
                "triggers": response["detected_triggers"]
            }
        }

@dataclass
class FamilyDashboardView:
    """Family-friendly status view"""
   
    patient_name: str
    current_status: Dict
    today_summary: Dict
    recent_alerts: List[Dict]
    medication_compliance: Dict
   
    def render_dashboard(self) -> Dict:
        return {
            "header": {
                "patient": self.patient_name,
                "last_updated": datetime.datetime.now().strftime("%I:%M %p"),
                "overall_status": self.current_status["overall_mood"]
            },
            "current_state": {
                "mood": self.current_status["overall_mood"],
                "activity": self.current_status["current_activity"],
                "needs_attention": self.current_status["alert_level"] == "HIGH"
            },
            "todays_overview": {
                "meals": self.today_summary["meals_completed"],
                "medications": f"{self.medication_compliance['taken']}/{self.medication_compliance['total']}",
                "episodes": self.today_summary["episodes_count"]
            },
            "alerts": self._format_alerts(),
            "reassurance": self._generate_reassurance()
        }
   
    def _format_alerts(self) -> List[str]:
        family_alerts = []
        for alert in self.recent_alerts:
            if alert["type"] == "pankaj_call_needed":
                family_alerts.append("She's been asking about Pankaj - a quick call would help")
            elif alert["type"] == "maternal_grief_alert":
                family_alerts.append("Mentioning mother a lot - share a family photo")
            elif alert["type"] == "isolation_check":
                family_alerts.append("Feeling isolated - suggest a walk or call")
            elif alert["type"] == "competence_support":
                family_alerts.append("Doubting memory - remind her of her achievements")
        return family_alerts
   
    def _generate_reassurance(self) -> str:
        if self.today_summary["episodes_count"] == 0:
            return "She's had a good day today."
        else:
            return "She had some confusion but AI helped her through it."

class DoctorDashboard:
    """Complete clinical interface"""
   
    def __init__(self, patient_id: str):
        self.patient_id = patient_id
        self.patient_context = PatientContext()
        self.analyzer = BehavioralPatternAnalyzer(self.patient_context)
        self.insights_engine = DoctorInsightsGenerator(self.patient_context, self.analyzer)
       
    def view_calendar_insights(self, date: datetime.date) -> Dict:
        # Simulate interactions based on day - completely different themes each day
        day_num = date.day
        if day_num == 8:  # Day 1: Focus on Money Anxiety + Competence Loss
            day_interactions = [
                {"time": "08:15", "state": "stable", "triggers": ["competence_loss"]},
                {"time": "12:30", "state": "agitated", "triggers": ["money_anxiety"]},
                {"time": "16:00", "state": "sundowning", "triggers": ["money_anxiety", "competence_loss"]},
                {"time": "18:00", "state": "stable", "triggers": ["pankaj_safety"]}
            ]
        elif day_num == 9:  # Day 2: Focus on Sister Urgency + Maternal Grief
            day_interactions = [
                {"time": "08:15", "state": "stable", "triggers": ["maternal_grief"]},
                {"time": "14:30", "state": "confused", "triggers": ["sister_urgency"]},
                {"time": "16:45", "state": "sundowning", "triggers": ["sister_urgency", "maternal_grief", "episode"]},
                {"time": "18:00", "state": "stable", "triggers": ["pankaj_safety"]}
            ]
        elif day_num == 10:  # Day 3: Focus on Home Longing + Isolation Panic
            day_interactions = [
                {"time": "08:15", "state": "stable", "triggers": ["isolation_panic"]},
                {"time": "15:20", "state": "temporal_displacement", "triggers": ["home_longing"]},
                {"time": "17:00", "state": "sundowning", "triggers": ["home_longing", "isolation_panic"]},
                {"time": "18:30", "state": "agitated", "triggers": ["isolation_panic", "pankaj_safety"]}
            ]
        else:
            day_interactions = [
                {"time": "08:15", "state": "stable", "triggers": []},
                {"time": "16:00", "state": "sundowning", "triggers": ["money_anxiety"]},
                {"time": "18:00", "state": "stable", "triggers": []}
            ]
       
        daily_summary = self.insights_engine.generate_daily_summary(date, day_interactions)
       
        return {
            "date": date.strftime("%B %d, %Y"),
            "quick_stats": {
                "overall_state": daily_summary["overall_state"],
                "episodes": daily_summary["episode_count"]
            },
            "timeline": day_interactions,
            "ai_narrative": daily_summary["narrative_summary"]
        }
   
    def get_ai_pattern_analysis(self, timeframe: str = "week") -> Dict:
        # 3-day data with different daily themes but common sundowning and Pankaj
        week_data = [
            {"date": "2026-02-08", "triggers": {"money_anxiety": 2, "competence_loss": 2, "pankaj_safety": 1}},
            {"date": "2026-02-09", "triggers": {"sister_urgency": 3, "maternal_grief": 2, "pankaj_safety": 1}},
            {"date": "2026-02-10", "triggers": {"home_longing": 2, "isolation_panic": 2, "pankaj_safety": 1}}
        ]
       
        patterns = {
            "period_summary": "3-Day Pattern Analysis (Feb 8-10, 2026)",
            "emerging_patterns": [
                {
                    "pattern": "Sundowning episodes daily, anchored by Pankaj mentions across all days",
                    "clinical_significance": "Pankaj as universal emotional stabilizer amid varying distress themes",
                    "recommendation": "Mandate daily 18:00 Pankaj interaction to mitigate escalation"
                },
                {
                    "pattern": "Thematic progression: Day1 Competence/Money -> Day2 Relational/Maternal -> Day3 Existential/Isolation",
                    "clinical_significance": "Layered grief unfolding; no repetition, indicating adaptive but deepening vulnerability",
                    "recommendation": "Tailor interventions per theme: Financial review (D1), Family photos (D2), Virtual tours (D3)"
                }
            ],
            "medication_efficacy": "Stable until 16:00; Day2/3 breakthroughs suggest environmental triggers over pharmacological",
            "treatment_recommendations": ["Theme-specific de-escalation kits", "Weekly pattern review with family"]
        }
        return patterns
   
    def analyze_uploaded_video(self, video_file: str, context: Dict) -> Dict:
        day_num = datetime.datetime.fromisoformat(context["timestamp"]).day if "timestamp" in context else 8
        if day_num == 9:  # Day 2: Maternal/Sister episode
            analysis = {
                "episode_timestamp": context.get("timestamp"),
                "trigger_identification": {
                    "immediate_trigger": "Sister reference evoking maternal loss",
                    "underlying_cause": "Sundown + unresolved sibling grief"
                },
                "behavioral_markers": {
                    "speech_pattern": "Emotional Marathi lamentations",
                    "physical_signs": ["Clutching chest", "Vocal tremors"]
                },
                "de_escalation_analysis": {
                    "what_worked": "Redirect to shared family memories",
                    "why_it_worked": "Bridged grief to preserved relational bonds"
                },
                "recommendations": [
                    "Incorporate maternal artifacts in routine",
                    "Pre-empt with afternoon relational check-ins"
                ]
            }
        elif day_num == 10:  # Day 3: Isolation/Home episode
            analysis = {
                "episode_timestamp": context.get("timestamp"),
                "trigger_identification": {
                    "immediate_trigger": "Home longing query",
                    "underlying_cause": "Displacement amplified by isolation"
                },
                "behavioral_markers": {
                    "speech_pattern": "Whispered pleas for return",
                    "physical_signs": ["Gazing at door", "Fidgeting with belongings"]
                },
                "de_escalation_analysis": {
                    "what_worked": "Virtual Solapur imagery description",
                    "why_it_worked": "Reoriented spatial identity without confrontation"
                },
                "recommendations": [
                    "Daily 'home tour' audio sessions",
                    "Isolation screening via mood logs"
                ]
            }
        else:  # Default or Day 1: Money/Competence
            analysis = {
                "episode_timestamp": context.get("timestamp"),
                "trigger_identification": {
                    "immediate_trigger": "Property theft delusion",
                    "underlying_cause": "Competence erosion in sundown"
                },
                "behavioral_markers": {
                    "speech_pattern": "Accusatory financial recounting",
                    "physical_signs": ["Rummaging drawers", "Raised voice"]
                },
                "de_escalation_analysis": {
                    "what_worked": "Ownership affirmation via achievement recall",
                    "why_it_worked": "Restored agency narrative"
                },
                "recommendations": [
                    "Secure 'property folder' with photos/docs",
                    "Competence-building tasks pre-sundown"
                ]
            }
        return analysis
   
    def chat_with_ai(self, doctor_question: str) -> Dict:
        responses = {
            "money paranoia": "Financial delusions stem from agency loss; root in widowhood trauma and property pride.",
            "sister obsession": "Sister as final sibling tie; triggers anticipatory loss, layered with maternal echoes.",
            "home longing": "Spatial disorientation masks deeper isolation; Solapur symbolizes intact identity era.",
            "maternal grief": "Mother fixation reveals core abandonment fear; childlessness amplifies via Pankaj projection.",
            "isolation panic": "Existential aloneness surges in displacement; requires multi-sensory reconnection.",
            "competence loss": "Memory lapses interpreted as total failure; counter with granular success validations."
        }
       
        for key in responses:
            if key in doctor_question.lower():
                return {
                    "doctor_asked": doctor_question,
                    "ai_analysis": responses[key],
                    "recommended_action": "Integrate into daily protocol"
                }
       
        return {
            "doctor_asked": doctor_question,
            "ai_analysis": "Query analyzed; theme-specific insights available.",
            "recommended_action": "Specify trigger for deeper dive"
        }

def run_three_day_demo():
    """
    Demonstrates all three interfaces over 3 completely different days
    Common: Daily sundowning + Pankaj as anchor
    Day 1 (Feb 8): Money Anxiety + Competence Loss (financial/agency theme)
    Day 2 (Feb 9): Sister Urgency + Maternal Grief (relational/loss theme)
    Day 3 (Feb 10): Home Longing + Isolation Panic (existential/displacement theme)
    """
   
    print("="*90)
    print("3-DAY ALZHEIMER'S AI SYSTEM ANALYSIS FOR SUHASINI")
    print("Dates: Feb 8-10, 2026 | Common: Sundowning + Pankaj anchors | Days: Completely Distinct Themes")
    print("="*90)
    print()
   
    patient_interface = PatientVoiceInterface()
    doctor_dashboard = DoctorDashboard(patient_id="SUHASINI_001")
   
    for day_offset in range(3):
        date = datetime.date(2026, 2, 8 + day_offset)
        day_name = ["Financial/Agency Distress", "Relational/Maternal Loss", "Existential/Isolation Displacement"][day_offset]
        print(f"\n{'='*90}")
        print(f"DAY {day_offset + 1}: {date.strftime('%A, %B %d, %Y')} | THEME: {day_name}")
        print(f"{'='*90}")
        print()
   
        # 1. PATIENT INTERFACE (Voice-Only) - Distinct daily interactions
        print("1. PATIENT INTERFACE (Voice-Only)")
        print("-" * 50)
        print()
   
        morning_time = datetime.datetime(2026, 2, 8 + day_offset, 8, 0)
        trigger = patient_interface.check_scheduled_trigger(morning_time)
   
        if trigger:
            print(f"[8:00 AM - AI INITIATES]: {trigger['utterance']}")
            print()
   
        # Day-specific patient utterances - completely different each day
        if day_offset == 0:  # Day 1: Money/Competence
            patient_says_morn = "I can't remember where I put the property papers... I'm useless now."
            patient_says_aft = "They stole my money again! My houses are gone!"
        elif day_offset == 1:  # Day 2: Sister/Maternal
            patient_says_morn = "My mother would know what to do... she always did."
            patient_says_aft = "Where is my sister? I have to tell her about Mama before it's too late!"
        else:  # Day 3: Home/Isolation
            patient_says_morn = "This Pune place feels so empty... everyone left me."
            patient_says_aft = "Take me home to Solapur! I can't stay alone here anymore."
   
        response_morn = patient_interface.listen_mode(patient_says_morn, morning_time)
        print(f"[MORNING - PATIENT]: {patient_says_morn}")
        print(f"[AI]: {response_morn['ai_speaks']}")
        print(f"[STATE]: {response_morn['log_to_doctor']['state']} | TRIGGERS: {', '.join(response_morn['log_to_doctor']['triggers'])}")
        print()
   
        afternoon_time = datetime.datetime(2026, 2, 8 + day_offset, 16, 0)
        response_aft = patient_interface.listen_mode(patient_says_aft, afternoon_time)
        print(f"[AFTERNOON/SUNDOWN - PATIENT]: {patient_says_aft}")
        print(f"[AI DETECTS]: Sundowning + {day_name.split('/')[0]} Trigger")
        print(f"[AI]: {response_aft['ai_speaks']}")
        print(f"[ALERT FAMILY?]: {response_aft['should_alert_family']}")
        print(f"[CLINICAL NOTE]: {response_aft['log_to_doctor']['triggers']}")
        print()
   
        # 2. FAMILY INTERFACE - Distinct daily views
        print("2. FAMILY INTERFACE (What Pankaj Sees)")
        print("-" * 50)
        print()
   
        if day_offset == 0:  # Day 1
            current_status = {"overall_mood": "frustrated", "current_activity": "Sorting old documents", "alert_level": "MEDIUM"}
            today_summary = {"meals_completed": "3/3", "episodes_count": 0}
            medication_compliance = {"taken": 4, "total": 4}
            alerts = [{"type": "competence_support", "timestamp": "12:30"}]
        elif day_offset == 1:  # Day 2
            current_status = {"overall_mood": "tearful", "current_activity": "Holding family photos", "alert_level": "HIGH"}
            today_summary = {"meals_completed": "2/3", "episodes_count": 1}
            medication_compliance = {"taken": 3, "total": 4}
            alerts = [{"type": "maternal_grief_alert", "timestamp": "08:15"}, {"type": "episode_alert", "timestamp": "16:45"}]
        else:  # Day 3
            current_status = {"overall_mood": "withdrawn", "current_activity": "Packing imaginary suitcase", "alert_level": "HIGH"}
            today_summary = {"meals_completed": "1/3", "episodes_count": 0}
            medication_compliance = {"taken": 2, "total": 4}
            alerts = [{"type": "isolation_check", "timestamp": "08:15"}, {"type": "pankaj_call_needed", "timestamp": "17:00"}]
   
        family_dashboard = FamilyDashboardView(
            patient_name="Suhasini (Aai)",
            current_status=current_status,
            today_summary=today_summary,
            recent_alerts=alerts,
            medication_compliance=medication_compliance
        )
   
        family_view = family_dashboard.render_dashboard()
        print(f"HEADER: {family_view['header']['patient']} | STATUS: {family_view['header']['overall_status']} | UPDATED: {family_view['header']['last_updated']}")
        print(f"CURRENT: Mood - {family_view['current_state']['mood']} | Activity - {family_view['current_state']['activity']} | Attention Needed: {family_view['current_state']['needs_attention']}")
        print(f"TODAY'S OVERVIEW: Meals - {family_view['todays_overview']['meals']} | Meds - {family_view['todays_overview']['medications']} | Episodes - {family_view['todays_overview']['episodes']}")
        print("RECENT ALERTS:")
        for alert in family_view['alerts']:
            print(f" • {alert}")
        print(f"💙 REASSURANCE: {family_view['reassurance']}")
        print()
   
        # 3. DOCTOR INTERFACE - Distinct daily insights
        print("3. DOCTOR INTERFACE (Clinical Dashboard)")
        print("-" * 50)
        print()
   
        print("📅 DAILY CALENDAR INSIGHTS:")
        day_view = doctor_dashboard.view_calendar_insights(date)
        print(json.dumps(day_view, indent=2))
        print()
   
        # Day-specific video analysis
        print(f"🎥 DAY-SPECIFIC EPISODE VIDEO ANALYSIS ({day_name.split('/')[0]} Focus):")
        episode_timestamp = f"2026-02-{8+day_offset:02d}T16:00:00"
        episode_context = {"timestamp": episode_timestamp, "duration_seconds": 600}
        video_analysis = doctor_dashboard.analyze_uploaded_video("day_episode.mp4", episode_context)
        print(json.dumps(video_analysis, indent=2))
        print()
   
        # Pattern analysis only on Day 3
        if day_offset == 2:
            print("🧠 OVERALL 3-DAY PATTERN ANALYSIS:")
            patterns = doctor_dashboard.get_ai_pattern_analysis("3days")
            print(json.dumps(patterns, indent=2))
            print()
   
        # Day-specific doctor chat
        print("💬 DOCTOR-AI CHAT (Theme-Specific Query):")
        if day_offset == 0:
            question = "Explain today's money paranoia and competence loss?"
        elif day_offset == 1:
            question = "Why the sudden maternal grief with sister mentions?"
        else:
            question = "How to handle isolation panic and home longing?"
        ai_response = doctor_dashboard.chat_with_ai(question)
        print(f"DOCTOR: {ai_response['doctor_asked']}")
        print(f"AI ANALYSIS: {ai_response['ai_analysis']}")
        print(f"ACTION: {ai_response['recommended_action']}")
        print()
   
    print("\n" + "="*90)
    print("3-DAY ANALYSIS COMPLETE")
    print("Summary: Each day uniquely themed with distinct triggers/activities/alerts across all interfaces.")
    print("Common Thread: Sundowning vulnerability + Pankaj as consistent stabilizer.")
    print("="*90)

if __name__ == "__main__":
    run_three_day_demo()
      
