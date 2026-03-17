"""
Setup script for PowerPulse Enhanced
Initializes the project and copies your existing models and data
"""

import os
import shutil
import sys

def setup_project():
    """Set up the PowerPulse Enhanced project"""
    print("🚀 Setting up PowerPulse Enhanced...")
    
    # Create necessary directories
    directories = [
        'static',
        'static/plots',
        'logs',
        'temp'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    # Copy model files from parent directory
    source_model_path = "../"
    model_files = [
        'DELHI_rf_model.pkl', 'DELHI_lstm_model.pkl', 'DELHI_xgb_model.pkl',
        'BRPL_rf_model.pkl', 'BRPL_lstm_model.pkl', 'BRPL_xgb_model.pkl',
        'BYPL_rf_model.pkl', 'BYPL_lstm_model.pkl', 'BYPL_xgb_model.pkl',
        'NDPL_rf_model.pkl', 'NDPL_lstm_model.pkl', 'NDPL_xgb_model.pkl',
        'NDMC_rf_model.pkl', 'NDMC_lstm_model.pkl', 'NDMC_xgb_model.pkl',
        'MES_rf_model.pkl', 'MES_lstm_model.pkl', 'MES_xgb_model.pkl'
    ]
    
    copied_models = 0
    for model_file in model_files:
        source_path = os.path.join(source_model_path, model_file)
        dest_path = os.path.join('models', model_file)
        
        if os.path.exists(source_path):
            try:
                shutil.copy2(source_path, dest_path)
                print(f"✅ Copied model: {model_file}")
                copied_models += 1
            except Exception as e:
                print(f"❌ Error copying {model_file}: {e}")
        else:
            print(f"⚠️  Model file not found: {source_path}")
    
    print(f"📊 Copied {copied_models} model files")
    
    # Copy data files
    data_files = ['cleaned_electricity.csv', 'cleaned_weather.csv']
    copied_data = 0
    
    for data_file in data_files:
        source_path = os.path.join(source_model_path, data_file)
        dest_path = os.path.join('data', data_file)
        
        if os.path.exists(source_path):
            try:
                shutil.copy2(source_path, dest_path)
                print(f"✅ Copied data: {data_file}")
                copied_data += 1
            except Exception as e:
                print(f"❌ Error copying {data_file}: {e}")
        else:
            print(f"⚠️  Data file not found: {source_path}")
    
    print(f"📁 Copied {copied_data} data files")
    
    # Check Python dependencies
    print("\n📦 Checking dependencies...")
    required_packages = [
        'flask', 'pandas', 'numpy', 'scikit-learn', 
        'tensorflow', 'xgboost', 'matplotlib', 'requests', 'seaborn'
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} - installed")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} - missing")
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Install them with: pip install " + " ".join(missing_packages))
    else:
        print("\n🎉 All dependencies are installed!")
    
    print(f"\n✨ Setup complete! Your PowerPulse Enhanced project is ready.")
    print(f"🏃 Run the application with: python app.py")
    print(f"🌐 Then visit: http://localhost:5000")

if __name__ == "__main__":
    setup_project()
