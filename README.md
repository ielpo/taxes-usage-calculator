# taxes-usage-calculator
Website to compute usage of tax money by the Swiss government and cantons.

Similar implementation (using old data) available at: <https://www.srf.ch/news/schweiz/persoenlicher-steuerrechner-wofuer-zahle-ich-steuern>, code at <https://srfdata.github.io/2019-02-steuern/>.

## Data structure
The data of the confederation and of cantons is exported from the files `data/bund.xlsx` and `data/ktn_xx.xlsx`.
These are part of the archive made available by the federal administration at <https://www.efv.admin.ch/efv/en/home/themen/finanzstatistik/daten.html>.

GDP data is exported from `data/bip.csv`, available at <https://www.bfs.admin.ch/bfs/de/home/statistiken/kataloge-datenbanken/tabellen.assetdetail.27065234.html>.

The processed data is saved in `data/data.json`

The data is structured in the following way (to be refined)

```
{
  "confederation": {
    "gdp": [
        {
          "year": "2010",
          "val": 45000000
        },
        {
          "year": "2011",
          "val": 47000000
        }
      ]
  },
  "cantons": [
    {
      "name": "ZH",
      "data": {
        "expenses": [
          {
            "id": "0",
            "share": [
              {
                "year": "2010",
                "val": 0.1
              }
            ]
          },
          {
            "id": "01",
            "share": [
              {
                "year": "2010",
                "val": 0.05
              }
            ]
          }
        ]
      }
    },
    {
      "name": "AG"
    },
    {
      "name": "TG"
    }
  ]
}
```
