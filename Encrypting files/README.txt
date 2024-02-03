These scripts are used for encrypting different types of files with AES (CBC mode).

We use local server "Vault" from HashiCorp for saving key in it. 
The key is created before encrypting a file. 
It is used for encoding and decoding our information.
After our file is encrypted we send the key to vault
To access the vault, we need to know the token, 
which is created when the local server is launched.
We need to set a variable for vault server token in the environment through which
our scripts will be executed. Scripts will take token from this environment variable
to send and take the key for encryption and decryption.

First, we need to launch a vault server with Command Prompt.
For simplicity and clarity, this is done using the following command
      vault -dev server
This will launch simple server in development mode.
In another Command Prompt window we should
create a variable for token copied from Command Prompt
with server working. 
          set Vault_token=hvs.nNV5VtxkoKQaqRVKuDVW7Z7I
This variable is used to save and get
cipher key to and from vault server.

After that we need to execute encrypt.py from the
Command Prompt window where we created the Vault_token variable.
This will take the original file and encrypt it.
Next, decrpypt.py takes an encrypted file and decrypts it
with cipher key, which is taken from vault server
The resulting file is our original file.
