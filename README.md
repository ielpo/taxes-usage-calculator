# taxes-usage-calculator
Website to compute usage of tax money by the Swiss government and cantons.

Similar implementation (using old data) available at: <https://www.srf.ch/news/schweiz/persoenlicher-steuerrechner-wofuer-zahle-ich-steuern>, code at <https://srfdata.github.io/2019-02-steuern/>.

## Goal of the project
Inform the public about the usage of tax money in a simple and clear interface. Additionally, we want to learn about the structure of the government and improve our software develoment skills.

## Data structure

### Expense data
The data of the confederation and of cantons is exported from the files `data/sources/bund.xlsx` and `data/sources/ktn_XX.xlsx`.
These are part of the archive made available by the federal administration at <https://www.efv.admin.ch/efv/en/home/themen/finanzstatistik/daten.html>.

The expenses are read from the sheet `ord_ausgaben_funk`, in which they are grouped by function. This is in order to be able to compare the confederation with individual cantons.

Each function has a unique ID identifying it and the corresponding labels are stored once.

The IDs are further splitted in category and subcategory, each category is a single digit ID between 0 and 9. The subcategories vary in number, but are represented by one subcategory digit between 1 and 9 appended to the category digit. For example the category "Social security" has ID 5, and its subcategory "Subsidized housing" has the ID 56.

The expenses are computed as a share of total expenditure of the Canton/Confederation and stored as a fractional number.

### GDP data

GDP data is exported from `data/sources/bip.csv`, available at <https://www.bfs.admin.ch/bfs/de/home/statistiken/kataloge-datenbanken/tabellen.assetdetail.27065234.html>.

| Name | Type | Content |
| --- | --- | --- |
| PERIOD | string | Year |
| VARIABLE | string | "GDP": Gross domestic product <br /> "GDPPC": Gross domestic product per capita |
| VALUE | float | Numeric value |
| UNIT_MEAS | string | "MCHF": Million CHF <br /> "AC": Annual change with current prices in % <br /> "ACPP": Annual change with prices of previous year in % |

### Processing
The input data is processed with the Pyhton script `data/process_data.py`.

### Output
The processed data is stored in one file per year `data/data_YYYY.json`.
The labels of the expenses are stored in `data/labels.json`
The files are structured as in the example file [structure.txt](structure.txt).
