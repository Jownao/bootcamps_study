from csv_class import CsvProcessor

# Mostrando que cada instância da classe CsvProcessor é independente

arquivo_csv = './exemplo.csv'  # substitua 'dados.csv' pelo caminho do seu arquivo CSV

csv_processor = CsvProcessor(arquivo_csv)
csv_processor.load_csv()
print(csv_processor.filtrar_por(['estado', 'preço'], ['SP', '10,50']))


arquivo_csv = './exemplo2.csv'  # substitua 'dados.csv' pelo caminho do seu arquivo CSV

csv_processor = CsvProcessor(arquivo_csv)
csv_processor.load_csv()
print(csv_processor.filtrar_por(['estado'], ['DF']))