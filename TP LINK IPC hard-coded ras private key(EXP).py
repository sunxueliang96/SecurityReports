pubkey = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC4D6i0oD/Ga5qb//RfSe8MrPVIrMIGecCxkcGWGj9kxxk74qQNq8XUuXoy2PczQ30BpiRHrlkbtBEPeWLpq85tfubTUjhBz1NPNvWrC88uaYVGvzNpgzZOqDC35961uPTuvdUa8vztcUQjEZy16WbmetRjURFIiWJgFCmemyYVbQIDAQAB
-----END PUBLIC KEY-----"""

prvkey = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC4D6i0oD/Ga5qb//RfSe8MrPVIrMIGecCxkcGWGj9kxxk74qQNq8XUuXoy2PczQ30BpiRHrlkbtBEPeWLpq85tfubTUjhBz1NPNvWrC88uaYVGvzNpgzZOqDC35961uPTuvdUa8vztcUQjEZy16WbmetRjURFIiWJgFCmemyYVbQIDAQABAoGAZ7lLVR7JUcPpyOegiuJbOEVvpJjWblfGY0rEURZRizU33yuFT77xKUOsvWLPS7BIjdlWsJ5r0NTUmGfLees71DqxfedQb3kSamBMErHu/jXeRi7MaGCLTyO9Ae+0+PFAHUdld1QjX50mAZD/+fbDPv7zUebNrMkFzbl99ctYznECQQDwiHNBP51VOF2f8pRmncr5QpZmWZb3ZNPw9Qc/97kn7Xs8zGz1NBEUA9SLcF25KXv6GpVdr6X7BuhXeB9HZpNTAkEAw+WYCnB1KjYz68FiIYkA63lrvnN2IG9pllkt+az6XFdXgOdqodoi3pWvmhkU55Z2N0okuGjm93qO1pebC3JcPwJAOsn+8Yms2LFoILnXj6UtgPLHc8id32Wjb5dT6EyR0rJ2louYbe4F5pBxGIukPKdpB94Ld9SAivRLQWW4r2jgxQJBAJo1+D1nj+Rd7PuPLXfmyRGVcQrpC7m22vDfXUDqOeBNZXX1Ns0Y0lBUl3sAeaNhn8ggls2QzxlMonstt4EIUrMCQCgOhLJ1SoUw1RE+b3x5hpuibFpiknX9MAjNxMJ1vHQFgsYTIVlD9LdHc/+nGbeXhzi0BJ2h3R5tmQmIseOs9f0=
-----END RSA PRIVATE KEY-----"""

import urllib
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from base64 import b64decode,b64encode
import sys

#cipher_text="K9jZtdFQkVUsHe%2BzFmv3TXrjvaNXB8oyP9B%2FyH68I96fKC0iw6JFGrF0I7gVuOMXNk6vwPUdwtFMVBukVTpgnhIxML75lpjdvOFEGmsNlL0pHKzvBhBfFps7Ku%2BibrfiXx6qsVnsNzsVYyXLyzqL9k07phwWcPKj%2BHWHyLmZLnw%3D"
cipher_text = b64decode(urllib.unquote(sys.argv[1]))
keyPriv = RSA.importKey(prvkey) 
cipher = Cipher_PKCS1_v1_5.new(keyPriv)
decrypt_text = cipher.decrypt(cipher_text, None).decode()
print "[+++] Decrypted New_Passwd ---->", decrypt_text

