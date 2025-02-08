import os
import spacy
import subprocess

# Create directory if it doesn't exist
os.makedirs('./data/models', exist_ok=True)

# Function to download and test models
def setup_and_test_model(model_name, test_text):
    print(f"\n=== Testing {model_name} ===")
    try:
        # Download model
        subprocess.run(['python', '-m', 'spacy', 'download', model_name], check=True)
        
        # Load model
        nlp = spacy.load(model_name)
        
        # Copy to custom directory
        print(f"Copying {model_name} to ./data/models/")
        nlp.to_disk(f'./data/models/{model_name}')
        
        # Test loading from custom directory
        print(f"Testing {model_name} from custom directory...")
        nlp_custom = spacy.load(f'./data/models/{model_name}')
        
        # Process test text
        doc = nlp_custom(test_text)
        
        # Print results
        print("\nTest Results:")
        print("Tokens and their POS tags:")
        for token in doc:
            print(f"{token.text:<10} {token.pos_}")
            
        print("\nNamed Entities:")
        for ent in doc.ents:
            print(f"{ent.text:<15} {ent.label_}")
            
        print(f"\n{model_name} test completed successfully!")
        
    except Exception as e:
        print(f"Error with {model_name}: {str(e)}")

# Test texts
english_test = "Apple Inc. is headquartered in Cupertino, California. Tim Cook is the CEO."
chinese_test = "苹果公司的总部在加利福尼亚州的库比蒂诺。蒂姆·库克是首席执行官。"

# List of models to test
models = {
    'en_core_web_sm': english_test,
    'zh_core_web_sm': chinese_test,
    'zh_core_web_md': chinese_test,
    'zh_core_web_lg': chinese_test
}

# Download and test each model
for model_name, test_text in models.items():
    setup_and_test_model(model_name, test_text)

print("\nAll models have been downloaded, stored, and tested!")

# Example of loading and using a specific model from the custom directory
print("\n=== Example Usage ===")
try:
    # Load Chinese large model from custom directory
    nlp = spacy.load('./data/models/zh_core_web_lg')
    
    # Process a new text
    test_text = "今天天气很好，我们去北京故宫博物院参观。"
    doc = nlp(test_text)
    
    print("\nProcessing new text with zh_core_web_lg:")
    print("Tokens and their POS tags:")
    for token in doc:
        print(f"{token.text:<5} {token.pos_}")
        
except Exception as e:
    print(f"Error in example usage: {str(e)}")
