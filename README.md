scrapy crawl cards -o test.json

$json = gc .\test.json -raw | ConvertFrom-Json
$json | ? {$_.deck -eq "Amonkhet"} | Export-Csv test.csv -UseCulture -NoTypeInformation -Encoding "UTF8"