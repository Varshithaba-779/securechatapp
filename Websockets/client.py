import asyncio
import websockets

async def communicate():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("Connected to server.")
        print("Supported algorithms: AES, DES, 3DES, Blowfish")

        while True:
            algo = input("\nEnter algorithm (or 'exit' to quit): ").strip()
            if algo.lower() == "exit":
                break

            message = input("Enter your message: ").strip()
            if not message:
                print("Message cannot be empty.")
                continue

            await websocket.send(f"{algo}|{message}")

            while True:
                response = await websocket.recv()
                if response == "END":
                    break
                print(response)

if __name__ == "__main__":
    asyncio.run(communicate())
