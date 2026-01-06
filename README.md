# Privacipher Secure Redaction

### Name: Bala Ravi Teja Mokhamatam

## Project Description

This project implements a secure text redaction system designed to identify and remove sensitive personal information from text documents. The redaction process targets personally identifiable information (PII), including names, dates, phone numbers, gender-identifying terms, and addresses. The objective is to protect privacy by ensuring such information is irreversibly masked before further use or distribution.

## Dependencies:

The project is implemented in Python and uses the following libraries.
-	black
-	numpy
-	nltk
-	commomregex
-	spacy

Dependency management is handled using Pipenv.

### Project Structure:
 
 The project follows the structure below.

├── 1.txt

├── 2.txt

├── 3.txt

├── 4.txt 

├── Pipfile

├── redactor.py

├── setup.cfg

├── setup.py

└── pytest.py

## Execution

### Running the Redaction tool

From the project root directory.

pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --output 'files/' \
                    --stats stderr

This command processes all matching text files, applies the selected redactions, writes redacted outputs to the specified directory, and reports redaction statistics.

### Running Tests

pipenv run python -m pytest


## Dataset

The project is evaluated using email data from the Enron corpus, available at the Carnegie Mellon University repository. The dataset is provided as a compressed archive and must be extracted prior to use

## Core Functionality

The system is organized into modular redaction functions, each responsible for a specific category of sensitive information:

- Names Redaction:

Names_red(text): Identifies and redacts personal names using natural language processing techniques.

- Dates Redaction:

red_date(text): Detects and redacts date patterns using predefined regular expressions.

- Phone Number Redaction:

red_phnum(data): Matches and redacts phone numbers based on common formatting patterns.

- Gender Redaction:

red_gender(text): Redacts gender-identifying terms using a controlled vocabulary of pronouns.

- Address Redaction:

red_add(data):Identifies address patterns using commonregex and applies redaction.

Redacted content is written to new files with a .redacted extension, and summary statistics are generated for each execution.

## Testing

The test suite validates:

- Correct identification and redaction of each sensitive data category

- Accurate counting of redacted elements

- Consistency between total redactions and individual category counts

### Assumptions and Limitations

- Input files must be accessible from the execution path.

- Pattern-based detection may not capture all possible variations of dates, addresses, or gender-identifying terms.

- Gender redaction is limited to predefined pronouns.

- Address detection accuracy depends on the limitations of the commonregex library.

- Required NLP models (e.g., en_core_web_sm) must be installed prior to execution.
