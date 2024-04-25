# CoffeeLog

## Overview

CoffeeLog is a journaling application to track details about the coffee you drink, and provided aggreated data and metrics.

## Details

### Database

**Tech** - Google Firestore [https://console.cloud.google.com/firestore/databases?referrer=search&hl=en&project=coffeelog-206](https://console.cloud.google.com/firestore/databases?referrer=search&hl=en&project=coffeelog-206)

**Database Name** - `coffeelog-metadata`

**[Database Attributes](https://www.notion.so/CoffeeLog-a85ea1b4728246d882816c12817bc87f?pvs=21)**

| Name | Type | Required | Examples | Notes |
| --- | --- | --- | --- | --- |
| Drink | String | Yes | Drip, Latte, Cold Brew |  |
| QuantityInFlOz | Number (int) | Yes | 12, 16, 20 |  |
| MilkOptions | String | No | Whole milk, half n half, oat milk |  |
| Additives | List<String> | No | [Vanilla syrup, cinnamon] |  |
| CoffeeBeans | Map | No | See CoffeeBeans table |  |
| Cafe | String | No | Victorola Cafe |  |
| EntryDatetime | Datetime | Yes | 2024-04-15 13:25 | Added by default, date, hour and minutes are saved |

**[CoffeeBeans Attributes](https://www.notion.so/CoffeeLog-a85ea1b4728246d882816c12817bc87f?pvs=21)**

| Name | Type | Required | Examples | Notes |
| --- | --- | --- | --- | --- |
| Producer | String | Yes | Caffe Vita, Onda Origins, Victorola Cafe |  |
| CountryOfOrigin | String | Yes | Brazil, Guatemala, Colombia |  |
| Name | String | No | Fiore Espresso, Midnight Drip |  |
| RoastLevel | Number (int), [1,10] | No | 1-Lightest, 5-Medium, 10-Darkest | Single select from list of numbers [1,10] |
| FlavorNotes | List<String> | No | [Caramel, Nutmeg, Cinnamon], [Raspberry, Rose, Lime Zest] |  |
| RoastDate | Date | No | 2024-04-15 |  |

## Future Goals/Ideas

|  | Feature | Notes |
| --- | --- | --- |
| 1. | Send users prompts/”horoscopes” based on coffee data | Example “you started everyday this week with the same type of drink (latte) - sunshine is upon you or you may die a horrible death” |
