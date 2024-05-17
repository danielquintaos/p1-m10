## Identificação do estudante: 
daniel quintao davila - EC M10

## BREVE descrição dos diretórios e os arquivos que fazem parte do repositório. 
```
p1-m10/
│
├── api/
│   ├── __init__.py
│   ├── main.py          # Main application file
│   └── resources/       # Directory for resource modules if using Flask-RESTful or similar
│       └── __init__.py
│   └── routes/
│       └── pedido_router.py
│
├── tests/
│   └── test_api.py     # Test scripts for the API
│
├── docs/
│   ├── openapi.yaml    # OpenAPI documentation
│   └── insomnia.json   # Insomnia collection for API testing
│   └── insomnia_get.json
│
├── docker-compose.yml
│
├── Dockerfile
│
├── requirements.txt    # Python package dependencies
└── README.md           # Project overview and setup instructions
```

## O procedimento para executar o projeto.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites:

You will need Python installed on your system. The project is tested with Python 3.9. Make sure you have `pip` and `virtualenv` installed to handle Python packages.

### Installation:

1. Clone the Repository

   Start by cloning the repository to your local machine:
   ```
   git clone https://github.com/danielquintaos/p1-m10
   cd mod10-pon1
   ```

2. Set up a Python Virtual Environment (Optional but recommended)

   To create a virtual environment, run:
   ```
   python3 -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```

3. Install Dependencies

   Install all dependencies that are required for the project by running:
   ```
   pip install -r requirements.txt
   ```

## Running the API:

1. Start the Application

   You can start the server using:
   ```
   python api/main.py
   ```


## Testing the API:

### Using Insomnia

   Import the `insomnia.json` file located in the `docs/` directory into Insomnia to test the API endpoints.
