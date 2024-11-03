import lzma
import os

class PyCCA:
    @staticmethod
    def compress_file(file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError("Arquivo não encontrado.")

        try:
            with open(file_path, 'rb') as f:
                data = f.read()
                compressed_data = lzma.compress(data)

            compressed_file_path = f"{file_path}.cca"
            with open(compressed_file_path, 'wb') as f:
                f.write(compressed_data)

            return compressed_file_path
        except Exception as e:
            raise Exception(f"Erro ao compactar: {str(e)}")

    @staticmethod
    def decompress_file(file_path):
        if not file_path.endswith('.cca'):
            raise ValueError("Por favor, forneça um arquivo .cca.")

        try:
            with open(file_path, 'rb') as f:
                compressed_data = f.read()
                data = lzma.decompress(compressed_data)

            original_file_path = file_path[:-4]  # remove '.cca'
            with open(original_file_path, 'wb') as f:
                f.write(data)

            return original_file_path
        except Exception as e:
            raise Exception(f"Erro ao descompactar: {str(e)}")