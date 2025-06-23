from pydantic import BaseModel , EmailStr , Field, AnyUrl,field_validator
from typing import Optional, List, Dict, Annotated

class Patient(BaseModel):

    # Field - for custom data validation
    # Annotated - for adding metadata to the field and also constraints
    # FieldValidators - for custom validation logic(icic.com,hdfc.com for verifying if customer belongs to a specific bank)
    # Annotated -> datatype -> Field -> usme constraints , default value , metadata

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=False, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]
    allergy: Annotated[Optional[list[str]],Field(default=None,max_length=5,description='List of allergies the patient has',
    example=['pollen', 'nuts'])]

    # two modes before and after | only validates a single field at a time
    @field_validator('email')
    @classmethod
    # Convert a function to be a class method.
    def validate_email(cls,value):
        valid_domains = ['icici.com', 'aurionpro.com']

        # Extract the domain from the email
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid Email domain")
        return value




def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}}



patient1 = Patient(**patient_info)

update_patient_data(patient1)