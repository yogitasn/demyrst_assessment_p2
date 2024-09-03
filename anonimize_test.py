import csv
import hashlib
from concurrent.futures import ProcessPoolExecutor

def hash_value(value):
    """Hash the input value using SHA-256."""
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def process_chunk(chunk, output_file):
    """Process a chunk of data, anonymizing sensitive columns."""
    with open(output_file, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        for row in chunk:
            # Anonymize columns
            row[0] = hash_value(row[0])  # first_name
            row[1] = hash_value(row[1])  # last_name
            row[2] = hash_value(row[2])  # address
            writer.writerow(row)

def chunkify(filename, chunk_size):
    """Read CSV file in chunks."""
    with open(filename, 'r', newline='') as infile:
        reader = csv.reader(infile)
        header = next(reader)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

def main():
    input_file = 'input.csv'
    output_file = 'anonymized_data.csv'
    chunk_size = 2  # Number of rows per chunk

    # Write header to output file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])

    # Process chunks in parallel
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_chunk, chunk, output_file) for chunk in chunkify(input_file, chunk_size)]
        for future in futures:
            future.result()

if __name__ == '__main__':
    main()
