"""from Crypto.Cipher import AES
import hvac
import base64


def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('utf-8')
    except:
        return False

client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='hvs.h97NXU30ZMbLstxM5CSHGmdJ',
)
key = b"1\xa0\xa9\xf1'\xc9\xd8\xda\xec(\x9ex\xc0\xdd\xdc\xe5.J\x0f$\xfe\x9a6\xfci\xbb\xa3\xd1\xc4\xba0\x1f"
tag = b'\xb5e\xae}\xf6\xfa\xf8\x05a\x9d\xf5\x96\xdd\xc4\r\xae'
nonce = b'\xc2\xbb\xfe\x87\xf6.\x04A\\=\xf9\xd9\xc64`\x14'

read_response = client.secrets.kv.read_secret_version(path='Lab3',raise_on_deleted_version=True)
password = read_response['data']['data']['password']
plaintext = decrypt(nonce,password,tag)
print(plaintext)"""



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
for attribute in dir(client):
    print(attribute, getattr(client, attribute))
read_response = client.secrets.kv.read_secret_version(path='Key',raise_on_deleted_version=True)

key = read_response['data']['data']['password']
print("Секрет отриманий із серверу vault:",key, type(key))

#key = base64.b64decode(key.encode())
key = base64.b64decode(key)
print("Key: ", key)

decrypt_file(key, 'D:\Visual Studio_\Saves\PSM3\PSM3\encrypted_picture.jpg')
