# DataVeilAPI

**DataVeilAPI** is a powerful and flexible API for data anonymization, designed to protect sensitive information across various data formats. The API implements a range of anonymization techniques to ensure the confidentiality and integrity of personal data. With support for a wide array of data types, DataVeilAPI is ideal for use in data engineering, data science, and machine learning projects.

## Features

- **Data Anonymization Techniques**: Masking, generalization, randomization, perturbation, pseudonymization, data swapping, and synthetic data generation.
- **Data Types**: Handles names, email addresses, phone numbers, Aadhaar numbers, Indian license numbers, voter IDs, PAN card numbers, passport numbers, and more.
- **Customizable**: Easily extendable to support additional data formats and anonymization techniques.

## Technical Stack

- **Framework**: Django
- **Language**: Python
- **Libraries**: 
  - **Faker**: For generating fake data.
  - **Regex**: For pattern matching and data manipulation.
- **Development Tools**: 
  - **Docker** (for containerization and consistent development environment).
  - **pytest** (for testing).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/DataVeilAPI.git
    cd DataVeilAPI
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

    The server will start at `http://127.0.0.1:8000/`.

## API Endpoints

### Anonymize Data

- **Endpoint**: `/anonymize/`
- **Method**: POST
- **Request Body**:

    ```json
    {
      "data": "John Doe, john.doe@example.com, 123-45-6789",
      "technique": "masking"
    }
    ```

- **Response**:

    ```json
    {
      "anonymized_data": "J******e, john.doe@example.com, 123-45-****"
    }
    ```

## Anonymization Techniques

- **Masking**: Replaces sensitive information with masked characters.
- **Generalization**: Replaces specific values with generalized values.
- **Randomization**: Replaces data with random characters or strings.
- **Perturbation**: Slightly alters the data while keeping it realistic.
- **Pseudonymization**: Replaces data with pseudonyms.
- **Data Swapping**: Swaps parts of the data with each other.
- **Synthetic Data**: Generates synthetic data with the same length as the original data.

## Contact

If you come across any issues, have suggestions for improvement, or want to discuss further enhancements, feel free to contact me at [jaya2004kra@gmail.com](mailto:jaya2004kra@gmail.com). Your feedback is greatly appreciated.

## License

All the code and resources in this repository are licensed under the Creative Commons Legal Code License. You are free to use, modify, and distribute the code under the terms of this license. However, I do not take responsibility for the accuracy or reliability of the programs.

## My Social Profiles:

- [**LINKEDIN**](https://www.linkedin.com/in/jayashrek/)