from lattice_crypto import LWE, NTRU, Ring_LWE
from post_quantum import SPHINCS, Dilithium
from typing import List, Dict

class QuantumResistantDetector:
    def __init__(self):
        self.lattice_schemes = {
            'lwe': LWE(),
            'ntru': NTRU(),
            'ring_lwe': Ring_LWE()
        }
        self.signatures = {
            'sphincs': SPHINCS(),
            'dilithium': Dilithium()
        }

    async def analyze_quantum_threats(self, data: Dict) -> Dict:
        threats = []
        
        # Detect quantum-capable patterns
        for scheme in self.lattice_schemes.values():
            if scheme.detect_vulnerability(data):
                threats.append({
                    'type': 'quantum_vulnerability',
                    'scheme': scheme.name,
                    'risk_level': scheme.assess_risk(data)
                })

        # Verify post-quantum signatures
        for sig in self.signatures.values():
            if not sig.verify_signature(data):
                threats.append({
                    'type': 'signature_vulnerability',
                    'scheme': sig.name,
                    'recommendation': sig.get_mitigation()
                })

        return {
            'threats': threats,
            'quantum_safety_score': self._calculate_safety_score(threats)
        }

    def _calculate_safety_score(self, threats: List[Dict]) -> float:
        base_score = 1.0
        for threat in threats:
            if threat['type'] == 'quantum_vulnerability':
                base_score *= (1 - threat['risk_level'])
        return base_score