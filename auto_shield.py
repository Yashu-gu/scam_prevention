import xml.etree.ElementTree as ET
import time
import os
import re
import urllib.parse

# Configuration
GUARDIAN_PHONE_NUMBER = "+919876543210"  # Replace with actual guardian number
EMERGENCY_SMS_TEXT = "🚨 EMERGENCY ALERT: Cyber-Fraud Scam Shield detected a 'Digital Arrest/CBI' threat on this phone! Please call me immediately!"

# Regex Pattern Dictionary for Scam Detection
REGEX_CATEGORIES = {
    "AUTHORITY": {
        "weight": 25,
        "patterns": [r"\bc\.?b\.?i\.?\b", r"\bpolice\b", r"\bcustoms\b", r"\btrai\b", r"\bcyber\s*cell\b", r"\bcourt\b", r"\bed\b"]
    },
    "LEGAL_THREAT": {
        "weight": 35,
        "patterns": [r"\barr[3e]st\b", r"\bwarr[a4]nt\b", r"\bdigital\s*arrest\b", r"\bf\.?i\.?r\.?\b", r"\bseized?\b"]
    },
    "URGENCY": {
        "weight": 20,
        "patterns": [r"\bimm[e3]diately\b", r"\b[uü]rgent\b", r"\bnow\b"]
    },
    "PAYMENT": {
        "weight": 20,
        "patterns": [r"\bpay\b", r"\bupi\b", r"\btransf[e3]r\b", r"\bpenal[t7]y\b", r"\bfine\b"]
    }
}

def calculate_threat_score(text_content):
    score = 0
    detected_matches = []
    for cat_name, cat_data in REGEX_CATEGORIES.items():
        cat_matched = False
        for pattern in cat_data["patterns"]:
            if re.search(pattern, text_content, re.IGNORECASE):
                cat_matched = True
                detected_matches.append(pattern)
        if cat_matched:
            score += cat_data["weight"]
    return score, list(set(detected_matches))

def parse_ui_xml():
    os.system("adb shell uiautomator dump /sdcard/window_dump.xml > /dev/null 2>&1")
    os.system("adb pull /sdcard/window_dump.xml . > /dev/null 2>&1")
    try:
        tree = ET.parse("window_dump.xml")
        root = tree.getroot()
        all_text = []
        for node in root.iter('node'):
            text_val = node.get('text')
            if text_val:
                all_text.append(text_val.lower())
            desc_val = node.get('content-desc')
            if desc_val:
                all_text.append(desc_val.lower())
        return " ".join(all_text)
    except Exception:
        return ""

def trigger_emergency_defense(score, matches):
    print(f"\n🚨 CRITICAL SCAM DETECTED! (Score: {score}) AUTONOMOUS DEFENSE ACTIVATED 🚨")
    print(f"Matched Triggers: {matches}")
    
    # 1. Wake up the phone screen automatically
    os.system("adb shell input keyevent KEYCODE_WAKEUP")
    # 2. Dismiss lockscreen/keyguard
    os.system("adb shell wm dismiss-keyguard")
    
    # 3. Automatically trigger SMS app with pre-filled guardian number and warning message
    encoded_message = urllib.parse.quote(EMERGENCY_SMS_TEXT)
    sms_command = f"adb shell am start -a android.intent.action.SENDTO -d smsto:{GUARDIAN_PHONE_NUMBER} --es sms_body \"{EMERGENCY_SMS_TEXT}\""
    os.system(sms_command)
    
    print(f"✅ Emergency SMS app opened automatically with pre-filled alert for: {GUARDIAN_PHONE_NUMBER}\n")

if __name__ == "__main__":
    print("🛡️ Cyber-Fraud Autonomous Shield Running... (Press Ctrl+C to stop)")
    
    while True:
        raw_screen_text = parse_ui_xml()
        
        if raw_screen_text:
            threat_score, matched_triggers = calculate_threat_score(raw_screen_text)
            print(f"Scanning... Current Threat Score: {threat_score}/100")
            
            # Autonomous trigger threshold
            if threat_score >= 60:
                trigger_emergency_defense(threat_score, matched_triggers)
                # Pause for 30 seconds to prevent continuous spam triggers on the same screen
                time.sleep(30)
                
        time.sleep(2)