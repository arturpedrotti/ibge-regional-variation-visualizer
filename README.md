# 📈 IBGE Regional Variation Visualizer

This is a **Streamlit-powered web application** for exploring regional and categorical variation data from the [Brazilian Institute of Geography and Statistics (IBGE)](https://www.ibge.gov.br/). The app provides **interactive data visualizations** such as line charts, bar plots, and scatter plots, enabling users to filter by **region (area)** or **category (group)**.

🔗 **Live Demo**: [Streamlit App](https://arturpedrotti-ibge-graficos-grafico-0fv9dz.streamlit.app/)

---

## 🚀 Features

- 📍 View regional and group-wise variations from IBGE's public dataset
- 📊 Interactive visualizations with support for:
  - Line charts
  - Bar charts
  - Scatter plots
- ✅ Filter by area or group
- 🌐 Built with Streamlit for fast and accessible web deployment

---

## 📁 Project Structure

| File / Folder       | Description                                     |
|---------------------|-------------------------------------------------|
| `grafico.py`        | Streamlit application source code               |
| `variacao.csv`      | Dataset containing IBGE variation data          |
| `requirements.txt`  | Python dependencies for running the app         |

---

## 📦 Installation

### ✅ Clone and Setup Locally

```bash
# 1. Clone the repository
git clone https://github.com/arturpedrotti/ibge-regional-variation-visualizer.git
cd ibge-regional-variation-visualizer

# 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run grafico.py
```

---

## 🛠 Technologies

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [NumPy](https://numpy.org/)

---

## 📊 Data Source

The dataset (`variacao.csv`) is derived from official IBGE data sources and contains regional variation information formatted for visualization.

---

## 📌 Example Visual Output

The app renders interactive plots showing variation metrics across cities or categories. It includes options for:
- Full dataset visualization
- Filtering by **region** or **group**
- Custom chart types

---

## 👨‍💻 Author

Developed by **Artur Pedrotti**  
Powered by data from [IBGE](https://www.ibge.gov.br/)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).  
Feel free to fork, modify, and contribute.
