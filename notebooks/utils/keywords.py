side_effect_keywords = [
    # General symptoms
    'headache', 'migraine', 'dizzy', 'dizziness', 'lightheaded', 'faint', 'nausea', 'nauseous',
    'vomit', 'vomiting', 'upset stomach', 'stomach ache', 'abdominal pain', 'cramps', 'bloating',
    'diarrhea', 'constipation', 'indigestion', 'heartburn', 'gas', 'belching', 'burping',
    
    # Fatigue and energy
    'fatigue', 'tired', 'exhausted', 'sleepy', 'drowsy', 'lethargic', 'low energy', 'sluggish',
    'weakness', 'muscle weakness', 'muscle pain', 'joint pain', 'achy', 'aches', 'pain', 'back pain',
    
    # Mood and mental health
    'anxiety', 'anxious', 'panic attacks', 'depression', 'mood swings', 'irritable', 'agitation', 
    'nervous', 'restless', 'confusion', 'brain fog', 'trouble concentrating', 'forgetfulness', 'sadness',
    
    # Sleep-related issues
    'insomnia', 'trouble sleeping', 'difficulty sleeping', 'cant sleep', 'restless sleep', 'waking up at night', 
    'nightmares', 'vivid dreams', 'sleep disturbance', 'oversleeping', 'sleep too much', 'sleep paralysis',
    
    # Skin-related issues
    'rash', 'hives', 'itch', 'itching', 'redness', 'dry skin', 'flaky skin', 'acne', 'breakouts', 
    'eczema', 'swelling', 'inflammation', 'puffy', 'puffiness', 'skin irritation', 'bruising',
    
    # Weight and appetite
    'weight gain', 'weight loss', 'loss of appetite', 'increased appetite', 'overeating', 'cravings',
    'binge eating', 'bloating', 'water retention', 'swelling in legs', 'fluid retention',
    
    # Cardiovascular-related
    'palpitations', 'heart racing', 'fast heartbeat', 'slow heartbeat', 'chest pain', 'chest tightness',
    'high blood pressure', 'low blood pressure', 'hypertension', 'fainting', 'dizziness standing up',
    
    # Vision and eyes
    'blurry vision', 'vision changes', 'eye pain', 'dry eyes', 'watery eyes', 'sensitive to light', 'double vision',
    
    # Mouth, throat, and breathing
    'dry mouth', 'cotton mouth', 'thirsty', 'sore throat', 'cough', 'difficulty breathing', 'shortness of breath',
    'wheezing', 'congestion', 'runny nose', 'stuffed nose', 'nosebleeds', 'difficulty swallowing', 'hoarse voice',
    
    # Sexual and reproductive system
    'loss of libido', 'low sex drive', 'erectile dysfunction', 'impotence', 'painful intercourse', 'vaginal dryness',
    'menstrual changes', 'irregular periods', 'missed period', 'spotting', 'cramps', 'heavy periods', 'prolonged periods',
    'discharge', 'brown discharge', 'breast tenderness', 'breast pain', 'nipple soreness',
    
    # Allergy-related
    'allergic reaction', 'swelling of the face', 'swelling of lips', 'swelling of tongue', 'difficulty breathing',
    'hives', 'itching', 'anaphylaxis', 'rash', 'throat swelling',
    
    # Neurological and cognitive
    'tremors', 'shaking', 'numbness', 'tingling', 'pins and needles', 'seizures', 'convulsions', 'loss of balance',
    'dizziness', 'vertigo', 'coordination issues', 'memory loss', 'confusion',
    
    # Urinary and renal system
    'frequent urination', 'urgent urination', 'difficulty urinating', 'painful urination', 'kidney pain', 'dark urine',
    'blood in urine', 'urinary tract infection', 'UTI', 'incontinence', 'trouble holding urine',
    
    # Miscellaneous
    'fever', 'chills', 'sweating', 'night sweats', 'hair loss', 'brittle nails', 'ringing in the ears', 'tinnitus',
    'bad taste', 'metallic taste', 'dry lips', 'swollen lips', 'joint stiffness'
]

# Common negation words or phrases
negation_words = [
    # Single-word negations
    "no", "not", "never", "none", "nothing", "nowhere", "neither", "nobody", "without", "hardly", "barely", "scarcely",
    
    # Common contractions
    "dont", "doesnt", "didnt", "wont", "wouldnt", "isnt", "arent", "wasnt", "werent", "havent", "hasnt", 
    "hadnt", "cant", "couldnt", "shouldnt", "mustnt", "mightnt", "shant", "aint",
    
    # Colloquial and informal negations
    "aint", "nah", "nope", "nothin", "not a single", "not any", "didnt", "doesnt", "havent", "isnt", "arent", "wasnt", "werent",
    
    # Phrases indicating negation
    "by no means", "in no way", "on no account", "under no circumstances", "neither nor", "no longer", "no way", "not at all", 
    "not even", "not once", "not anymore", "far from", "seldom", "few if any", "least of all"
]