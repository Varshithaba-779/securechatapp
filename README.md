Project Title : Secure Chat App
A secure real-time chat application that supports end-to-end encryption using AES, 3DES, and Blowfish algorithms. Built with WebSockets to ensure low-latency messaging.

1.Features
- Real-time chat using WebSockets
- End-to-end encryption (AES, 3DES, Blowfish)
- Secure message transmission
- Performance comparison of encryption algorithms

 2.Technologies Used
- Python (for server)
- JavaScript (for client)
- WebSockets
- Cryptography Libraries (e.g., pycryptodome)

3.Installation Instructions
1. Clone the repository:
   git clone https://github.com/yourusername/securechatapp.git

2. Navigate to the directory:
cd securechatapp

3. Install dependencies:
pip install -r requirements.txt


4. Run the server:
python server.py

5. Open the client in browser or terminal.



4.Encryption Details (since it's a crypto-focused project)
Encryption Algorithms
 *AES*: Strong, fast symmetric cipher
  *3DES*: Legacy standard, slower but supported
  *Blowfish*: Lightweight with variable key size

Each message is encrypted on the client side before being sent and decrypted on the receiving client.

5.Performance Evaluation
We compared AES, 3DES, and Blowfish based on:
- Encryption/decryption time
- Entropy
- Confusion and diffusion levels
