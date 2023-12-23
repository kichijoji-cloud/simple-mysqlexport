## Summary
The `mysqlexport.py` script is a command-line tool written in Python for exporting data from a MySQL table to a tab-separated values (TSV) file. It supports two modes of operation: loading configuration from a JSON file using the `--config` option or directly specifying MySQL connection details and export options through command-line arguments.

----

## Asset
- **mysqlexport.py**: The Python script for exporting MySQL table data to a TSV file.


----

## Details

### Usage

#### Using a JSON Config File
```bash
python mysqlexport.py --config config.json
```

#### Directly Specifying Options
```bash
python mysqlexport.py --user your_username --password your_password --host your_host --db your_db --table your_table --columns column1 column2 --output output_file.tsv
```

### Options
- `--config`: Path to a JSON config file with MySQL connection details and export options.
- `--user`: MySQL username.
- `--password`: MySQL password.
- `--host`: MySQL host.
- `--db`: Database name.
- `--table`: Table name.
- `--columns`: Columns to export (multiple columns can be specified).
- `--output`: Output file name for the TSV file.
- `--fields-enclosed-by`: Character to enclose fields.(optional)

### Example JSON Config File
```json
{
  "user": "your_username",
  "password": "your_password",
  "host": "your_host",
  "db": "your_db",
  "table": "your_table",
  "columns": ["column1", "column2"],
  "output": "output_file.tsv",
  "fields_enclosed_by": ""
}
```

----
## Disclaimer
This script is provided as-is without any warranties. Use it at your own risk. The authors are not responsible for any damages or losses arising from the use of this script.


----
## License
This script is released under the [MIT License](LICENSE). Feel free to modify and distribute it according to the terms of the license.

Please make sure to include the actual `LICENSE` file in your repository with the text of the MIT License.
