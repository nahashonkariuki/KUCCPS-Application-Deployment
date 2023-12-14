from flask import Flask, render_template, request
import numpy as np
import pickle 

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get student's cluster weight from the form
    student_cluster_weight = float(request.form['cluster_weight'])

    # Predict Next Year's Cut-Off
    predicted_cut_off = rf_model.predict([[student_cluster_weight]])

    # Define the condition to determine qualification (replace with your condition)
    qualification_condition = student_cluster_weight >= predicted_cut_off

    if qualification_condition:
        # Extracting qualified courses based on some condition (replace with your condition)
        qualified_courses = final_df_encoded[final_df_encoded['YOUR_CONDITION']]['PROGRAMME NAME']
        return render_template('result.html', qualification=True, courses=qualified_courses)
    else:
        return render_template('result.html', qualification=False)

if __name__ == '__main__':
    app.run(debug=True)
