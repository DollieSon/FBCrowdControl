import asyncio
import websockets

# Define a WebSocket handler function
async def websocket_handler(websocket, path):
    while True:
        try:
            # Receive message from the client
            message = await websocket.recv()
            print(f"Received message from client: {message}")

            # Send message back to the client
            await websocket.send(f"Server received: {message}")

        except websockets.exceptions.ConnectionClosed:
            print("Client disconnected")
            break

# Start the WebSocket server
start_server = websockets.serve(websocket_handler, 'localhost', 8765)

# Run the server forever
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
