# Data dictionary | قاموس البيانات

## Main analytical dataset

File: `data/processed/field_month_economics.csv`

| Column | Meaning | المعنى |
|---|---|---|
| `field_name` | Reported UKCS field name | اسم الحقل المبلغ عنه |
| `field_region` | NSTA geographic region | المنطقة الجغرافية |
| `location` | Onshore/offshore flag | بري أو بحري |
| `operator` | Operator reported for that month | المشغل المسجل لذلك الشهر |
| `date` | First day of the reporting month | شهر التقرير |
| `oil_m3` | Monthly oil production, cubic metres | إنتاج النفط الشهري بالمتر المكعب |
| `oil_bbl` | Monthly oil production converted to barrels | الإنتاج الشهري محولاً إلى برميل |
| `associated_gas_ksm3` | Associated gas, thousand standard cubic metres | الغاز المصاحب، ألف متر مكعب قياسي |
| `dry_gas_ksm3` | Dry gas, thousand standard cubic metres | الغاز الجاف، ألف متر مكعب قياسي |
| `gas_flared_ksm3` | Gas flared, thousand standard cubic metres | الغاز المحروق |
| `gas_vented_ksm3` | Gas vented, thousand standard cubic metres | الغاز المنفّس |
| `water_injected_m3` | Injected water, cubic metres | الماء المحقون |
| `water_produced_m3` | Produced water, cubic metres | الماء المنتج |
| `brent_usd_per_bbl` | Monthly EIA Brent spot benchmark | سعر Brent الشهري المرجعي |
| `gross_revenue_proxy_usd` | Oil barrels × monthly Brent benchmark | البراميل × سعر Brent الشهري |
| `flaring_intensity_ksm3_per_1000m3_oil` | Flaring volume per 1,000 m³ oil | كثافة الحرق لكل 1,000 م³ نفط |
| `venting_intensity_ksm3_per_1000m3_oil` | Venting volume per 1,000 m³ oil | كثافة التنفيس لكل 1,000 م³ نفط |
| `water_oil_ratio_m3_per_m3` | Produced-water to oil ratio | نسبة الماء المنتج إلى النفط |

Undefined ratios are stored as blank/`NaN` when oil production is zero. The revenue proxy is not profit or valuation.

تُترك النسب فارغة عندما يكون إنتاج النفط صفراً. ومؤشر الإيراد ليس ربحاً ولا تقييماً للحقل.
