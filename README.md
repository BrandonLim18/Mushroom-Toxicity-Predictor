# 🍄 Mushroom Toxicity Predictor

A comprehensive, deep-learning powered web application designed to act as a digital field journal and toxicity screening tool for botanical specimens (mushrooms).

![Project Banner](https://images.unsplash.com/photo-1542385151-efd9000785a0?q=80&w=2000&auto=format&fit=crop) *(Placeholder banner - replace with an actual screenshot of the app)*

## 📖 Overview

The Botanical Toxicity Predictor is an enterprise-grade Flask application that evaluates the morphological, structural, and ecological traits of a mushroom to determine its safety for consumption. By utilizing a tuned Decision Tree classifier trained on 21 distinct botanical features, the application provides an immediate safety verdict and auto-generates a professional scientific field observation log.

**Key Features:**
*   **Comprehensive Assessment:** Evaluates 21 distinct features, ranging from cap morphology to spore print coloration and habitat.
*   **"Glassmorphism" UI:** A modern, highly immersive interface styled as a digital field journal.
*   **Smart Validation:** Custom JavaScript validation ensures complete data entry across multiple hidden tabs, guiding the user to missing inputs.
*   **Auto-Generated Field Notes:** Synthesizes user inputs into a 4-paragraph, scientifically accurate botanical observation report.
*   **Official Diagnostic Stamping:** The Python backend dynamically intercepts the generated field notes to append the final, official toxicity verdict.

## 🛠️ Technology Stack

*   **Backend:** Python 3, Flask
*   **Machine Learning:** Scikit-Learn (Decision Tree Classifier), Pandas
*   **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5.3
*   **Deployment:** GitHub

## 🧠 The Machine Learning Model

The core of the application is a Decision Tree Classifier (`decision_tree_master.pkl`).

*   **Pre-Processing:** The original dataset was cleaned to handle missing values (e.g., categorizing missing stalk roots as 'Unknown') and dropping variables with zero variance (e.g., `VeilType`).
*   **Tuning & Pruning:** The model was tuned and pre-pruned using the hyperparameter `max_depth=6` to prevent overfitting while handling 21 features, ensuring high accuracy and rapid inference.

## 🚀 How to Run Locally

To run this application on your local machine, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Botanical-Toxicity-Predictor.git](https://github.com/YOUR_USERNAME/Botanical-Toxicity-Predictor.git)
    cd Botanical-Toxicity-Predictor
    ```

2.  **Set Up a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    *(Note: Ensure you have `flask`, `pandas`, and `scikit-learn` installed)*
    ```bash
    pip install flask pandas scikit-learn
    ```

4.  **Start the Server:**
    ```bash
    python app.py
    ```

5.  **Open the Application:**
    Navigate to `http://127.0.0.1:5000` in your web browser.

## 🗂️ Project Structure
```text
Botanical-Toxicity-Predictor/
│
├── app.py                      # The Flask application backend
├── decision_tree_master.pkl    # The trained Decision Tree model
├── mushroom.csv                # The original dataset used for training
│
└── templates/                  
    └── index.html              # The frontend UI (Botanical Journal)
