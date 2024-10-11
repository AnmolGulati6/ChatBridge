# Multi-Client Chat Application

A Python-based multi-client chat application inspired by Messenger that enables real-time communication between 50+ users. The application includes a graphical user interface (GUI) built with Tkinter, allowing users to send and receive messages interactively in real time. This project demonstrates socket programming for handling multiple client connections, with a focus on scalability and ease of use.

## Features
- **Real-Time Communication**: Supports chat among 50+ users simultaneously.
- **Interactive GUI**: Built using Tkinter, providing an intuitive chat window for message input and display.
- **Scalable Architecture**: Handles multiple client connections through socket programming.
- **Broadcast Messaging**: Messages sent by one client are broadcast to all other connected clients.

## Project Structure
- `server.py`: The server-side script that manages client connections, message broadcasting, and overall communication.
- `client.py`: The client-side script that handles user interaction, GUI display, and communication with the server.

## Requirements
- Python 3.x
- `Tkinter` for GUI development (pre-installed with Python)
- `socket` library (part of Python's standard library)

## Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/multi-client-chat-app.git
cd multi-client-chat-app
```

### 2. Running the Server
Start the server by running the `server.py` file:
```bash
python server.py
```
The server will start listening for incoming client connections on `localhost:5000`.

### 3. Running the Client
Start the client by running the `client.py` file:
```bash
python client.py
```
Each client will be prompted to enter their nickname. After entering, a GUI window will appear, allowing them to send and receive messages.

### 4. Chatting
Once multiple clients have connected to the server, they can start chatting in real time. Each message will be broadcast to all connected clients.

## Customization
- **Server Configuration**: You can change the host and port in the `server.py` file to deploy on a remote server or change the local configuration.
- **UI Customization**: Modify the Tkinter-based GUI in `client.py` to enhance the appearance or add features such as message timestamps or user status indicators.

## Future Improvements
- Add private messaging between users.
- Implement message encryption for secure communication.
- Add user authentication and profiles.
- Improve the UI for a more polished look.

## Contributing
Feel free to open issues or submit pull requests if you have suggestions for improvements or encounter any bugs.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy using this real-time chat application! If you have any questions or suggestions, feel free to reach out.
