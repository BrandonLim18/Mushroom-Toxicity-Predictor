from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the Master Model Pipeline directly
with open('decision_tree_master (2).pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_result = None
    botanist_note = None

    if request.method == 'POST':
        # A professional list of all 21 features in your dataset
        features = [
            'CapShape', 'CapSurface', 'CapColor', 'Bruises', 'Odor',
            'GillAttachment', 'GillSpacing', 'GillSize', 'GillColor',
            'StalkShape', 'StalkRoot', 'StalkSurfaceAboveRing', 'StalkSurfaceBelowRing',
            'StalkColorAboveRing', 'StalkColorBelowRing', 'VeilColor',
            'RingNumber', 'RingType', 'SporePrintColor', 'Population', 'Habitat'
        ]
        
        # Automatically grab all 21 inputs from the HTML form
        input_dict = {}
        for feat in features:
            raw_val = request.form.get(feat, "Unknown")
            input_dict[feat] = [raw_val.split(" ")[0]]
            
        input_data = pd.DataFrame(input_dict)
        botanist_note = request.form.get('botanist_note')

        # -------------------------------------------------------------
        # THE PIPELINE 
        pred = model.predict(input_data)[0]
        # -------------------------------------------------------------
        
        # STEP 3: THE OFFICIAL DIAGNOSTIC STAMP
        if pred == 1:
            prediction_result = "⚠️ TOXIC / POISONOUS"
            verdict_stamp = "\n\n====================================================\n[ OFFICIAL DIAGNOSIS ]: ⚠️ LETHAL TOXICITY CONFIRMED\nDo NOT eat. Specimen contains severe toxicological markers.\nHandle with extreme caution and wash hands immediately."
        else:
            prediction_result = "✅ SAFE / EDIBLE"
            verdict_stamp = "\n\n====================================================\n[ OFFICIAL DIAGNOSIS ]: ✅ SAFE FOR CONSUMPTION\nSpecimen aligns completely with edible morphology.\nApproved for foraging and culinary use."

        # Remove the "Awaiting..." placeholder and stamp the true verdict!
        if botanist_note:
            botanist_note = botanist_note.replace("STATUS: Field observation complete. Awaiting deep-learning diagnostic confirmation...", "")
            botanist_note += verdict_stamp
        # -------------------------------------------------------------

    return render_template('index.html', prediction=prediction_result, note=botanist_note)

if __name__ == '__main__':
    app.run(debug=True)