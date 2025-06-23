from fastapi import FastAPI,Path,HTTPException,Query
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {'message':'Hello World'}

@app.get("/viewPatients")
def view_patients():
    data = load_data()
    return data

# patient_id is the path parameter:which is required

'''
The path function is used to provide metadata,validation,rules and documentation hints for the path parameter
ge,gt,le,lt - for numeric parameter
min_length
max_length
regex
... -> Path parameter is required

'''


@app.get("/viewPatients/{patient_id}")
def specific_patient(patient_id: str = Path(...,description="ID of the patient to retrieve",example="P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found")


'''
Query Parameter - /viewPatients ? name=John & age=30 - name and age are the query parameters(optional key-value pairs)

Also user can view the patients on basis of height/weight/bmi (SORT BY) and in which order (ASC/DESC) - Optional Parameters - not necessary user would mention this parameter
'''

@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort patients by this field height,weight or bmi", example="bmi"),
    order: str = Query("asc", description="Order of sorting: asc or desc", example="asc")
    # default sorting value is ascending order
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid sort field. Choose from {valid_fields}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order. Choose 'asc' or 'desc'")

    data = load_data()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_order)
    return sorted_data


# retrieve - GET(retrieve path and query params - and return desired data) | create(new user - get the request body from client) - POST | update - PUT
