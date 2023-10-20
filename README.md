# taxes-usage-calculator
Website to compute usage of tax money by the Swiss government and cantons.

Similar implementation (using old data) available at: <https://www.srf.ch/news/schweiz/persoenlicher-steuerrechner-wofuer-zahle-ich-steuern>, code at <https://srfdata.github.io/2019-02-steuern/>.

## Goal of the project
Inform the public about the usage of tax money in a simple and clear interface. Additionally, we want to learn about the structure of the government and improve our software develoment skills.

## Data structure
The data of the confederation and of cantons is exported from the files `data/bund.xlsx` and `data/ktn_XX.xlsx`.
These are part of the archive made available by the federal administration at <https://www.efv.admin.ch/efv/en/home/themen/finanzstatistik/daten.html>.

The expenses are read from the sheet `ord_ausgaben_funk`, in which they are grouped by function. This is in order to be able to compare the confederation with individual cantons.

Each function has a unique ID identifying it, so the labels are stored only once


GDP data is exported from `data/bip.csv`, available at <https://www.bfs.admin.ch/bfs/de/home/statistiken/kataloge-datenbanken/tabellen.assetdetail.27065234.html>.

| Name | Type | Content |
| --- | --- | --- |
| PERIOD | integer | year |
| VARIABLE | string | "GDP": Gross domestic product <br /> "GDPPC": Gross domestic product per capita |
| VALUE | float | Numeric value |
| UNIT_MEAS | string | "MCHF": Million CHF <br /> "AC": Annual change with current prices in % <br /> "ACPP": Annual change with prices of previous year in % |

The processed data is stored in one file per year `data/data_YYYY.json`.
The labels of the expenses are stored in `data/labels.json`
The files are structured as in the example file `structure.txt`.
