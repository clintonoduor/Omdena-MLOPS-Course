from app.flaskapp import app
from app.BMICalculator import calculate_bmi

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')