import argparse
import mysql.connector
import csv
import json

def export_to_tsv(username, password, host, db_name, table_name, columns, output_file, fields_enclosed_by=None):
	# MySQLに接続
	connection = mysql.connector.connect(
		user=username,
		password=password,
		host=host,
		database=db_name
	)

	cursor = connection.cursor()

	# カラムをカンマ区切りの文字列に変換
	columns_str = ', '.join(columns)

	# クエリの作成
	query = f"SELECT {columns_str} FROM {table_name}"

	# クエリの実行
	cursor.execute(query)

	# 結果を取得
	results = cursor.fetchall()

	# TSVファイルに書き込み
	with open(output_file, 'w', newline='', encoding='utf-8') as tsvfile:
		tsv_writer = csv.writer(tsvfile, delimiter='\t', quotechar=fields_enclosed_by, quoting=csv.QUOTE_MINIMAL)

		# カラム名を書き込み
		tsv_writer.writerow(columns)

		# データを書き込み
		tsv_writer.writerows(results)

	# 接続を閉じる
	cursor.close()
	connection.close()

def load_config_from_json(config_file):
	with open(config_file, 'r', encoding='utf-8') as json_file:
		config = json.load(json_file)
	return config

def main():
	parser = argparse.ArgumentParser(description='Export MySQL table to TSV file')
	parser.add_argument('--config', help='JSON config file with MySQL connection details and export options')

	args, remaining_args = parser.parse_known_args()

	if args.config:
		config = load_config_from_json(args.config)
	else:
		parser.add_argument('--user', required=True, help='MySQL username')
		parser.add_argument('--password', required=True, help='MySQL password')
		parser.add_argument('--host', required=True, help='MySQL host')
		parser.add_argument('--db', required=True, help='Database name')
		parser.add_argument('--table', required=True, help='Table name')
		parser.add_argument('--columns', nargs='+', required=True, help='Columns to export')
		parser.add_argument('--output', required=True, help='Output file name')
		parser.add_argument('--fields-enclosed-by', help='Character to enclose fields')

		config = vars(parser.parse_args(remaining_args))

	export_to_tsv(
		config['user'],
		config['password'],
		config['host'],
		config['db'],
		config['table'],
		config['columns'],
		config['output'],
		config.get('fields_enclosed_by')
	)

if __name__ == "__main__":
	main()


