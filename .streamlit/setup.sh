# setup.sh
#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run ibge_app.py
