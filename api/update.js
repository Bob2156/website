// Variable to store the latest message
let message = "";

// API handler
export default function handler(req, res) {
    if (req.method === 'POST') {
        // Update the message
        const { command } = req.body;
        if (command === "/ping") {
            message = "!pong"; // Set the message
        }
        res.status(200).json({ success: true });
    } else if (req.method === 'GET') {
        // Return the latest message
        res.status(200).json({ message });
    } else {
        // Unsupported HTTP method
        res.status(405).json({ error: "Method Not Allowed" });
    }
}
