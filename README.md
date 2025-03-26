
# Certificate Generation Script

This repository contains a Python script that generates personalized certificates for participants in an event using LaTeX.

## Features
- Generate certificates for participants based on a CSV input file.
- Includes dummy event details, organizers, and dates.
- Automatically generates PDF certificates via `pdflatex`.

## Prerequisites
1. **Python 3.x** 
2. **LaTeX Environment** (install `pdflatex`):
   - For Linux: `sudo apt-get install texlive`
   - For macOS: `brew install texlive`
   - For Windows: [Download MiKTeX](https://miktex.org/)

3. **Required Python Package**: `pandas`
   ```bash
   pip install pandas
   ```

## Files
- **certificate_generator.py**: Python script for certificate generation.
- **FINAL.csv**: Sample CSV with participant details (`FirstName;LastName;Affiliation`).
- **LaTeX Template**: Embedded within the script.

## Usage
1. Prepare a CSV file (`FINAL.csv`) with the following columns: `FirstName`, `LastName`, `Affiliation`.
2. Run the script:
   ```bash
   python certificate_generator.py
   ```
   This will generate certificates as PDFs in the `certificates/` directory.

## Example Certificate
The generated certificates will include:
- Event name: `First Edition of the Dummy Event`
- Event date: `January 1-2, 2025`
- Certification date: `January 3, 2025`
- Organizers: `The Dummy Organizing Committee`

## License
MIT License

