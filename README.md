# Out in the Open
Profile Parsing script for my blog post http://justdev.in/out-in-the-open.html

Outputs JSON like below:

```
{
  "id": 1,
  "name": "John Smith",
  "about": "male from Test Town, New York",
  "vital_medical_conditions": [
    {
      "condition": "test",
      "description": "test description"
    }
  ],
  "emergency_contacts": [
    {
      "name": "Jane Smith",
      "relationship": "wife",
      "phone_number": "1234567890",
      "alt_phone_number": "-"
    }
  ],
  "allergies": [],
  "physicians": [],
  "insurance_informations": [],
  "other_informations": [],
  "personal_information": {
    "name": "John Doe Smith",
    "phone": "123423536",
    "birth_date": "2015-1-10",
    "gender": "male",
    "hair": "black",
    "eye_color": "brown",
    "height": "5'0\"",
    "weight": "0 lbs",
    "blood_type": "Unknown"
  }
}
```
