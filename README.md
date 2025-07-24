Project Title : Secure Chat App
A secure real-time chat application that supports end-to-end encryption using AES, 3DES, and Blowfish algorithms. Built with WebSockets to ensure low-latency messaging.

1.Features
- Features
- WebSocket-based real-time messaging
- Client-side encryption and decryption
- Selectable algorithms: AES, 3DES, Blowfish
- Performance comparison (encryption time, entropy, avalanche effect)
- Educational tool for learning cryptography


 2.Technologies Used
-  Python (backend with `asyncio`, `websockets`)
- HTML, CSS, JavaScript (frontend)
- Manual implementation of symmetric encryption
- `psutil` for performance analysi

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
