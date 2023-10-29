# RSA Factoring Challenge

## Author - Kevin Kipkoech

### RSA (cryptosystem)

Developed in the 1970s RSA-(Rivest-Shamir-Adleman) is a public key cryptosystem though one of the oldest to date as its been used widely over the internet for secure communications using a secure socket layer(SSL). 

Its an asymemetric public-private key crptosystem in which the public key can be known by everyone and is used for encryption. The private key is known by only the owner and is used for decryption. Both keys are different.

It is very difficult to factorize large numbers and thus this is it depends for its security, sounds good, using the problem as a way to secure itself.

#### How it works:

1. Choose two large prime number, p and q. Then compute n = pq. n is known as the modulus
2. The totient of n is then computed 
3. Then choose an integer e such that 1 < e < n(totient) and gcd(e, n(totient)) = 1. e is the public exponent and is used to encrypt the message.
4. compute d such that ed = 1 mod totient(n). d is called the private exponent and it is ed to decyrpt the message.

<please refer to this for further understanding>

https://jaredatandi.hashnode.dev/rsa-factoring
https://en.wikipedia.org/wiki/RSA_(cryptosystem%29

