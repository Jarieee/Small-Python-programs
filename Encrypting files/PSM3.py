import base64                       
from Crypto.Cipher import AES
from secrets import token_bytes
from hvac import Client
import os, struct
from Crypto import Random


def encrypt_file(key, filename):
    chunk_size = 64*1024

    output_filename = 'D:\Visual Studio_\Saves\PSM3\PSM3\encrypted_picture.jpg'

    # Random Initialization vector
    iv = Random.new().read(AES.block_size)

    #create the encryption cipher
    encryptor = AES.new(key, AES.MODE_CBC, iv)

    #Determine the size of the file
    filesize = os.path.getsize(filename)
	
	#Open the output file and write the size of the file. 
	#We use the struct package for the purpose.
    with open(filename, 'rb') as inputfile:
        with open(output_filename, 'wb') as outputfile:
            outputfile.write(struct.pack('<Q', filesize))
            outputfile.write(iv)
            
            while True:
                chunk = inputfile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += bytes(' ','utf-8') * (16 - len(chunk) % 16)

                outputfile.write(encryptor.encrypt(chunk))

key = token_bytes(16)
encrypt_file(key, 'D:\Visual Studio_\Saves\PSM3\PSM3\picture.jpg')
vault_url = 'http://127.0.0.1:8200'
token = os.environ.get('Vault_token')
client = Client(url=vault_url, token=token)
key = base64.b64encode(key).decode()
# Запис секрету
create_response = client.secrets.kv.v2.create_or_update_secret(
    path='Key',
    secret=dict(password=key),
)
