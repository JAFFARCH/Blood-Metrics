from services.llm_chain import chain

def handle_conversation(data):
    question = '''
        Digest the data and have an overview of how the health of each record looks like and how it can be interpreted. Also, predict which patient has more risk.
        Risk Thresholds:
        --------------
        Metric       | Borderline   | High Risk
        -------------|--------------|-----------
        A1C          | ≥ 5.7%       | ≥ 6.5%
        LDL          | ≥ 130 mg/dL  | ≥ 160 mg/dL
        Vitamin D    | ≤ 30 ng/mL   | < 20 ng/mL
        Blood Pressure | ≥ 130/80 mmHg | ≥ 140/90 mmHg
        Glucose      | ≥ 100 mg/dL  | ≥ 126 mg/dL
    '''
    
    result = chain.invoke({"data": data, "question": question})
    return result
