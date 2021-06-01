Although CSV is a very popular format of storing data, we find it so much easier to process JSON data in Python, since it's very similar to the dictionary data structure in Python.
Given a CSV file csv_file.txt with following format:
```
Manchester United,Manchester,UK
Real Madrid,Madrid,Spain
Juventus,Turin,Italy
```
Read and process the file and store its content in JSON format into json_file.txt . The according keys to each field in the CSV file are club, city, country.. Thus the output should be, according to the given sample CSV file, like this:
```
[{"club": "Manchester United", "city": "Manchester", "country": "UK"}, {"club": "Real Madrid", "city": "Madrid", "country": "Spain"}, {"club": "Juventus", "city": "Turin", "country": "Italy"}]
```
