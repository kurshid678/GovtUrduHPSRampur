# Save this as server.py
import http.server
import socketserver

# Define the port you want to use
port = 1240

# Set up the handler
handler = http.server.SimpleHTTPRequestHandler


# Change this line in server.py
httpd = socketserver.TCPServer(("0.0.0.0", port), handler)


# Print a message indicating the server is running
print(f"Serving on port {port}")

# Start the server
httpd.serve_forever()
