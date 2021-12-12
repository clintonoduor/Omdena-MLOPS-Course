from fastapi import FastAPI, Request
import uvicorn

from BMICalculator import calculate_bmi

app = FastAPI()

'''
A function to get the request using fast-api and 
return the calculated bmi.
'''
@app.get('/')
async def get_input(request:Request):

    packet = await request.json()
    weight = packet['weight']
    height = packet['height']
    bmi = calculate_bmi(weight, height)
    return jsonify(bmi) 

if __name__ == '__main__':
    uvicorn.run()