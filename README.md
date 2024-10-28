
Blood Metrics Dashboard

Overview
The Blood Metrics Dashboard is a single-page React application developed to help healthcare providers quickly identify patients with concerning blood work values. This dashboard displays patient metrics in a color-coded table format, highlights any metrics falling outside normal ranges, and provides a summary of at-risk metrics. Additionally, the app integrates an Ollama LLM model via FastAPI to analyze data and deliver insightful summaries of each patient’s health status.

Features
1. Data Table: Displays patient blood metrics in a tabular format.
2. Risk Level Highlighting: Blood values are highlighted based on severity levels:
   - Normal: No highlight
   - Borderline: Yellow highlight
   - High Risk: Red highlight
3. Risk Summary: Provides a quick summary of at-risk metrics for each patient.
4. LLM Insights: Uses Ollama LLM (accessed via FastAPI) to analyze and provide insights into each patient's health based on their metrics, highlighting which patients are at higher risk.

## Risk Thresholds
The risk thresholds for each metric are as follows:
| Metric         | Borderline            | High Risk                 |
|----------------|-----------------------|----------------------------|
|   A1C          | ≥ 5.7%                | ≥ 6.5%                    |
|   LDL          | ≥ 130 mg/dL           | ≥ 160 mg/dL               |
|   Vitamin D    | ≤ 30 ng/mL            | < 20 ng/mL                |
|   Blood Pressure | ≥ 130/80 mmHg     | ≥ 140/90 mmHg             |
|   Glucose      | ≥ 100 mg/dL           | ≥ 126 mg/dL               |

## Installation and Setup

To set up and run the application locally, follow these steps:

### Prerequisites
- Ensure you have Node.js (v14 or higher) installed.
- Clone this repository to your local machine.

### Setup Instructions
1. Install Dependencies:
   ```bash
   npm install
   ```

2. Start the Application:
   ```bash
   npm start
   ```
   This command starts the application in development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

3. FastAPI Setup for LLM Integration:
   - Make sure the Ollama LLM is running.
   - Start the FastAPI server to handle data insights with Ollama.
   - Configure any necessary environment variables or endpoint URLs in `utils` for LLM communication.

### Directory Structure
- `public/`: Contains static files and icons.
- `src/`: The source code for the application.
  - `components/`: Reusable components for the dashboard.
    - `DataTable.js`: Component displaying the data table with risk highlights.
    - `RiskSummary.js`: Component summarizing at-risk metrics.
    - `LLMInsight.js`: Component that generates insights by analyzing data through Ollama LLM.
  - `data/`: Stores sample data (`sampleData.json`) used to populate the dashboard.
  - `utils/`: Contains helper functions for LLM requests and risk analysis.
  - `App.js`: Main application component, assembling all parts of the dashboard.
  - `index.js`: Entry point for the React application.

### Sample Data
The application uses sample data stored in `data/sampleData.json`, structured as shown below:
```json
[
  {
    "id": "001",
    "date": "2023-07-01",
    "a1c": 5.6,
    "ldl": 120,
    "vitaminD": 18,
    "bloodPressure": "120/80",
    "glucose": 98
  },
  {
    "id": "002",
    "date": "2023-06-15",
    "a1c": 6.1,
    "ldl": 145,
    "vitaminD": 25,
    "bloodPressure": "130/85",
    "glucose": 110
  }
]
```

## Assumptions
- Blood Metrics Interpretation: Thresholds and interpretation criteria are based on standard ranges.
- Ollama LLM Usage: Assumes LLM provides a summary of patient health based on JSON data input.
- UI Library: TailwindCSS was used to style components for consistency and responsiveness.

## Implementation Notes
1. Table and Highlighting Logic:
   - Each row represents a patient's data, with conditional formatting based on the predefined risk thresholds.
2. LLM Integration:
   - FastAPI serves as the middleware, facilitating data analysis and insight generation.
   - The `LLMInsight.js` component submits patient data to Ollama for interpretation, providing healthcare insights.
3. User Experience:
   - The application uses color-coded highlights to quickly convey risk levels.
   - Borderline and high-risk metrics are clearly differentiated to streamline review.
4. Error Handling:
   - Includes basic error handling for LLM API calls to ensure consistent user experience.

## Usage
Upon launching the application:
1. View the patient data in a color-coded table format.
2. Review the risk summary for each patient.
3. Access detailed insights via the LLM component for a more nuanced health overview.

## Future Improvements
- Dynamic Data: Implement data fetching from an external API or database.
- Interactive Filtering: Add options to filter by specific metrics or risk levels.
- Enhanced Error Handling: Implement more robust error handling for API and LLM integration.

## AI Prompt Engineering
The prompts for LLM were crafted to succinctly convey each patient’s health status based on data trends. Prompts include conditions and questions that enable the LLM to interpret and rank patient risk effectively. All prompt-engineering inputs and outputs are documented for transparency and reproducibility.

## Screenshots
_Add screenshots here if available._

## License
This project is open-source under the MIT License. See `LICENSE` for details.
