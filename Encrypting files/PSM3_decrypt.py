import struct
from Crypto.Cipher import AES
import hvac
import base64

def decrypt_file(key, filename):
    chunk_size = 64*1024

    output_filename = "D:\Visual Studio_\Saves\PSM3\PSM3\decrypted_image.jpg"
	
	#open the encrypted file and read the file size and the initialization vector. 
	#The IV is required for creating the cipher.
    with open(filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
		
		#create the cipher using the key and the IV.
        decryptor = AES.new(key, AES.MODE_CBC, iv)
		
		#We also write the decrypted data to a verification file, 
		#so we can check the results of the encryption 
		#and decryption by comparing with the original file.
        with open(output_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunk_size)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
            

client = hvac.Client()

read_response = client.secrets.kv.read_secret_version(path='Key',raise_on_deleted_version=True)

key = read_response['data']['data']['password']
print("Секрет отриманий із серверу vault:", key, type(key))

#key = base64.b64decode(key.encode())
key = base64.b64decode(key)
print("Key: ", key)

decrypt_file(key, 'D:\Visual Studio_\Saves\PSM3\PSM3\encrypted_picture.jpg')
