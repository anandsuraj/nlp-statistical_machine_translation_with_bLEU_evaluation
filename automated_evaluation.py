
import json
from app import app

def run_evaluation():
    """
    Runs an automated evaluation of the SMT workflow across multiple languages.
    Uses Flask's test_client to simulate API requests without starting the server.
    """
    client = app.test_client()
    
    # Test Cases: Source Text, Target Lang, Reference Translations
    test_cases = [
        {
            "name": "English to Hindi",
            "source_text": "The weather is beautiful today.",
            "source_lang": "en",
            "target_lang": "hi",
            "references": [
                "आज मौसम बहुत सुंदर है।",
                "आज मौसम सुहावना है।",
                "आज का मौसम बहुत अच्छा है।",
                "आज मौसम ख़ूबसूरत है." 
            ]
        },
        {
            "name": "English to Hindi (Complex)",
            "source_text": "Artificial intelligence creates new opportunities for everyone.",
            "source_lang": "en",
            "target_lang": "hi",
            "references": [
                "कृत्रिम बुद्धिमत्ता सभी के लिए नए अवसर पैदा करती है।",
                "एआई सभी के लिए नए मौके बनाता है।",
                "आर्टिफिशियल इंटेलिजेंस सबके लिए नए अवसर लाता है।"
            ]
        },
        {
            "name": "English to French",
            "source_text": "Machine translation is useful.",
            "source_lang": "en",
            "target_lang": "fr",
            "references": [
                "La traduction automatique est utile.",
                "La traduction par machine est pratique."
            ]
        },
        {
            "name": "English to Spanish",
            "source_text": "I love learning new languages.",
            "source_lang": "en",
            "target_lang": "es",
            "references": [
                "Me encanta aprender nuevos idiomas.",
                "Amo aprender lenguas nuevas."
            ]
        },
        {
            "name": "English to German",
            "source_text": "This is a test of the system.",
            "source_lang": "en",
            "target_lang": "de",
            "references": [
                "Dies ist ein Test des Systems.",
                "Das ist eine Prüfung des Systems."
            ]
        },
        {
            "name": "English to Italian",
            "source_text": "I would like to order a large pizza please.",
            "source_lang": "en",
            "target_lang": "it",
            "references": [
                "Vorrei ordinare una pizza grande per favore.",
                "Mi piacerebbe ordinare una grande pizza per favore."
            ]
        },
        {
            "name": "English to Portuguese",
            "source_text": "Thank you very much for your help.",
            "source_lang": "en",
            "target_lang": "pt",
            "references": [
                "Muito obrigado pela sua ajuda.",
                "Obrigado por ajudar."
            ]
        }
    ]

    print("="*120)
    print(f"{'LANGUAGE PAIR':<25} | {'SOURCE TEXT':<40} | {'BLEU':<8} | {'STATUS':<10} | {'DETAILS'}")
    print("="*120)
    
    total_bleu = 0
    passed_tests = 0
    results_summary = []

    for i, case in enumerate(test_cases, 1):
        # Prepare payload
        payload = {
            "source_text": case['source_text'],
            "source_lang": case['source_lang'],
            "target_lang": case['target_lang'],
            "references": case['references']
        }
        
        try:
            # Send POST request to /translate_and_evaluate
            response = client.post('/translate_and_evaluate', 
                                 data=json.dumps(payload),
                                 content_type='application/json')
            
            if response.status_code == 200:
                result = response.get_json()
                bleu_data = result.get('bleu_evaluation', {})
                bleu_score = bleu_data.get('bleu_score', 0)
                
                status = "PASS" if bleu_score > 0.5 else ("LOW" if bleu_score > 0 else "FAIL")
                if bleu_score == 1.0: status = "PERFECT"
                
                precision_str = ", ".join([f"{k}:{v}" for k,v in bleu_data.get('precision_details', {}).items()])
                
                # Truncate source text for display if too long
                display_source = (case['source_text'][:37] + '...') if len(case['source_text']) > 40 else case['source_text']
                
                print(f"{case['name']:<25} | {display_source:<40} | {bleu_score:<8.4f} | {status:<10} | {precision_str}")
                
                total_bleu += bleu_score
                passed_tests += 1
                
                results_summary.append({
                    "pair": case['name'],
                    "input": case['source_text'],
                    "translation": result.get('translated_text'),
                    "bleu": bleu_score,
                    "status": status
                })
            else:
                print(f"{case['name']:<25} | {case['source_text']:<40} | ERROR    | FAIL       | API Error {response.status_code}")
                
        except Exception as e:
             print(f"{case['name']:<25} | {case['source_text']:<40} | ERROR    | FAIL       | {str(e)}")

    # Summary
    avg_bleu = total_bleu / len(test_cases) if test_cases else 0
    print("-" * 120)
    print(f"Total Tests: {len(test_cases)}")
    print(f"Successful Executions: {passed_tests}/{len(test_cases)}")
    print(f"Average BLEU Score: {avg_bleu:.4f}")
    print("="*80)

if __name__ == "__main__":
    run_evaluation()
