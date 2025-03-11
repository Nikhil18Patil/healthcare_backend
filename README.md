# Healthcare Management API

## Overview
This API allows users to register, log in, and manage doctors, patients, and doctor-patient mappings. Only authenticated users can create doctors, patients, and mappings.

## Base URL
```
http://your-api-url.com/
```

---

## Authentication
The API requires authentication using a Bearer Token. Users must first register and log in to obtain a token.

Authentication APIs
POST /api/auth/register/ - Register a new user with name, email, and password.
POST /api/auth/login/ - Log in a user and return a JWT token.
2. Patient Management APIs
POST /api/patients/ - Add a new patient (Authenticated users only).
GET /api/patients/ - Retrieve all patients created by the authenticated user.
GET /api/patients/<id>/ - Get details of a specific patient.
PUT /api/patients/<id>/ - Update patient details.
DELETE /api/patients/<id>/ - Delete a patient record.
3. Doctor Management APIs
POST /api/doctors/ - Add a new doctor (Authenticated users only).
GET /api/doctors/ - Retrieve all doctors.
GET /api/doctors/<id>/ - Get details of a specific doctor.
PUT /api/doctors/<id>/ - Update doctor details.
DELETE /api/doctors/<id>/ - Delete a doctor record.
4. Patient-Doctor Mapping APIs
POST /api/mappings/ - Assign a doctor to a patient.
GET /api/mappings/ - Retrieve all patient-doctor mappings.
GET /api/mappings/<patient_id>/ - Get all doctors assigned to a specific patient.
DELETE /api/mappings/<id>/ - Remove a doctor from a patient.

```
---

## Notes
- All endpoints require authentication except for user registration and login.
- Make sure to include the Bearer Token in the Authorization header for protected routes.
- Replace `{id}` and `uuid` placeholders with actual values.
- Use proper validation for inputs to avoid errors.
- put, delete apis ar there as well
