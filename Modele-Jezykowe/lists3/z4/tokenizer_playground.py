model_name = "eryk-mazus/polka-1.1b"


class TokenizerAnalyzer:
    def __init__(self, tokenizer) -> None:
        self.tokenizer = tokenizer
        
    def analyze_token_format(self, text: str) -> None:
        """Analyze how the tokenizer handles different parts of text"""
        # Get raw tokens with all special characters preserved
        tokens = self.tokenizer.tokenize(text)
        # Get token IDs
        token_ids = self.tokenizer.encode(text)
        # Get decoded versions
        decoded_tokens = [self.tokenizer.decode([tid]) for tid in token_ids]
        
        print(f"\nAnalyzing text: '{text}'")
        print("-" * 60)
        print("Token analysis:")
        for i, (raw_token, token_id, decoded) in enumerate(zip(tokens, token_ids, decoded_tokens)):
            print(f"{i:2d}. Raw token: '{raw_token:15}' | ID: {token_id:5d} | Decoded: '{decoded}'")
            
    def analyze_word_boundaries(self) -> None:
        """Analyze how the tokenizer handles word boundaries"""
        test_cases = [
            "Hello world my name is",  # Basic space
            "Hello  world",  # Multiple spaces
            "Hello,world",  # No space, with punctuation
            "HelloWorld",   # No space, camel case
            "HELLO WORLD",  # All caps
            "hello.world",  # Period boundary
        ]
        
        for test in test_cases:
            self.analyze_token_format(test)
            
    def analyze_special_cases(self) -> None:
        """Analyze how tokenizer handles various special cases"""
        test_cases = [
            "Preprocessing",  # Single word that might be split
            "pre-processing", # Hyphenated
            "PRE_PROCESSING", # Underscore
            "preprocessing",  # Lowercase
            "PreProcessing",  # Camel case
        ]
        
        for test in test_cases:
            self.analyze_token_format(test)
            
    def analyze_vocabulary_sample(self, n_samples: int = 20) -> None:
        """Analyze a sample of vocabulary tokens"""
        print(f"\nAnalyzing {n_samples} random vocabulary tokens:")
        print("-" * 60)
        
        vocab_size = self.tokenizer.vocab_size
        # Sample some token IDs
        import random
        sample_ids = random.sample(range(vocab_size), min(n_samples, vocab_size))
        
        for tid in sample_ids:
            token = self.tokenizer.decode([tid])
            raw_tokens = self.tokenizer.tokenize(token)
            print(f"ID: {tid:5d} | Decoded: '{token:15}' | Raw: {raw_tokens}")

def run_tokenizer_analysis(model_name: str):


    """Run comprehensive tokenizer analysis for a given model"""
    from transformers import AutoTokenizer
    
    print(f"Analyzing tokenizer for model: {model_name}")
    print("=" * 60)
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    analyzer = TokenizerAnalyzer(tokenizer)

    print(10*"\n")
    
    print("\n1. Word Boundary Analysis")
    print("=" * 60)
    analyzer.analyze_word_boundaries()
    
    print("\n2. Special Cases Analysis")
    print("=" * 60)
    analyzer.analyze_special_cases()
    
    print("\n3. Vocabulary Sample Analysis")
    print("=" * 60)
    analyzer.analyze_vocabulary_sample(20)

run_tokenizer_analysis(model_name=model_name)